import json
import itertools

interactions = []

# Helper to add interactions
def add_interaction(drug_group1, drug_group2, severity, desc_ar, desc_en):
    desc = f"{desc_ar}<div style='direction: ltr; text-align: left; margin-top: 8px; font-size: 12.5px; opacity: 0.85; border-top: 1px solid rgba(0,0,0,0.06); padding-top: 6px; font-family: sans-serif;'>{desc_en}</div>"
    for d1 in drug_group1:
        for d2 in drug_group2:
            if d1 != d2:
                # Avoid duplicate pairings
                pair = sorted([d1, d2])
                if not any(i["drugs"] == pair for i in interactions):
                    interactions.append({
                        "drugs": pair,
                        "severity": severity,
                        "desc": desc
                    })

# 1. NSAIDs vs themselves (Duplicate Therapy)
nsaids = ["IBUPROFEN", "DICLOFENAC", "NAPROXEN", "KETOPROFEN", "MELOXICAM", "PIROXICAM", "CELECOXIB", "ETORICOXIB", "INDOMETHACIN", "LORNOXICAM", "TENOXICAM", "ACECLOFENAC", "DEXKETOPROFEN", "FLURBIPROFEN", "MEFENAMIC ACID", "NABUMETONE", "SULINDAC"]
for d1, d2 in itertools.combinations(nsaids, 2):
    desc_ar = "الجمع بين مسكنين من عائلة NSAIDs يضاعف خطر قرحة ونزيف المعدة والفشل الكلوي دون فائدة إضافية مسكنة."
    desc_en = "Combining two NSAIDs doubles the risk of stomach ulcers, gastrointestinal bleeding, and acute renal failure with no therapeutic benefit."
    desc = f"{desc_ar}<div style='direction: ltr; text-align: left; margin-top: 8px; font-size: 12.5px; opacity: 0.85; border-top: 1px solid rgba(0,0,0,0.06); padding-top: 6px; font-family: sans-serif;'>{desc_en}</div>"
    interactions.append({
        "drugs": sorted([d1, d2]),
        "severity": "خطير جداً 🔴",
        "desc": desc
    })

# 2. NSAIDs vs Anticoagulants & Antiplatelets
anticoagulants = ["WARFARIN", "RIVAROXABAN", "APIXABAN", "DABIGATRAN", "HEPARIN", "ENOXAPARIN", "CLOPIDOGREL", "TICAGRELOR", "PRASUGREL", "ASPIRIN"]
add_interaction(nsaids, anticoagulants, "خطير جداً 🔴", 
                "المسكنات مع مميعات الدم أو مضادات الصفائح تؤدي لارتفاع شديد في خطر النزيف الداخلي والنزيف الهضمي الحاد.",
                "NSAIDs with anticoagulants or antiplatelets lead to a high risk of internal bleeding and acute gastrointestinal hemorrhage.")

# 3. NSAIDs vs ACE/ARBs
ace_arbs = ["PERINDOPRIL", "RAMIPRIL", "ENALAPRIL", "LISINOPRIL", "CAPTOPRIL", "VALSARTAN", "LOSARTAN", "CANDESARTAN", "TELMISARTAN", "IRBESARTAN", "OLMESARTAN", "AZILSARTAN", "FOSINOPRIL", "TRANDOLAPRIL"]
add_interaction(nsaids, ace_arbs, "تداخل متوسط 🟡", 
                "المسكنات تقلل من فاعلية أدوية الضغط بشكل ملحوظ وتزيد من خطر الفشل الكلوي الحاد بالتأثير على شرايين الكلية.",
                "NSAIDs significantly reduce the efficacy of antihypertensive drugs and increase the risk of acute kidney injury by affecting renal perfusion.")

# 4. NSAIDs vs Corticosteroids
corticosteroids = ["PREDNISOLONE", "DEXAMETHASONE", "METHYLPREDNISOLONE", "HYDROCORTISONE", "BETAMETHASONE", "PREDNISONE", "DEFLAZACORT", "TRIAMCINOLONE", "FLUDROCORTISONE"]
add_interaction(nsaids, corticosteroids, "خطير جداً 🔴", 
                "الاستخدام المشترك يزيد من خطر تقرحات ونزيف الجهاز الهضمي بشكل كبير جداً (يجب إضافة حامي معدة PPI).",
                "Concurrent use significantly increases the risk of gastrointestinal ulceration and bleeding (PPI co-prescription recommended).")

# 5. ACE/ARBs vs Potassium Sparing Diuretics & Potassium supplements
potassium_sparing = ["SPIRONOLACTONE", "EPLERENONE", "AMILORIDE", "POTASSIUM", "POTASSIUM CHLORIDE", "TRIAMTERENE"]
add_interaction(ace_arbs, potassium_sparing, "تداخل خطير 🔴", 
                "كلا الدواءين يرفعان نسبة البوتاسيوم في الدم، والجمع بينهما قد يسبب فرط بوتاسيوم الدم وتوقف مفاجئ للقلب.",
                "Both drugs increase serum potassium. The combination may cause severe hyperkalemia and cardiac arrest.")

# 6. PDE5 Inhibitors vs Nitrates
pde5 = ["SILDENAFIL", "TADALAFIL", "VARDENAFIL", "AVANAFIL"]
nitrates = ["ISOSORBIDE DINITRATE", "ISOSORBIDE MONONITRATE", "NITROGLYCERIN", "PENTAERYTHRITIL TETRANITRATE"]
add_interaction(pde5, nitrates, "تفاعل قاتل 🔴", 
                "الجمع بين منشطات القدرة الجنسية وأدوية النترات الموسعة للشرايين يؤدي لهبوط حاد وقاتل في ضغط الدم.",
                "Combining PDE5 inhibitors and vasodilating nitrates causes severe, life-threatening hypotension.")

# 7. PDE5 Inhibitors vs Alpha blockers
alpha_blockers = ["TAMSULOSIN", "DOXAZOSIN", "PRAZOSIN", "TERAZOSIN", "ALFUZOSIN", "SILODOSIN"]
add_interaction(pde5, alpha_blockers, "تداخل متوسط 🟡", 
                "قد يؤدي الجمع بينهما إلى انخفاض إضافي في ضغط الدم والدوخة عند الوقوف (يفضل أخذ الجرعات بفاصل 4 ساعات).",
                "The combination may cause additive blood pressure reduction and orthostatic hypotension (administer at least 4 hours apart).")

# 8. Warfarin vs Broad Antibiotics / Antifungals
macrolides = ["CLARITHROMYCIN", "ERYTHROMYCIN", "AZITHROMYCIN", "ROXITHROMYCIN"]
fluoroquinolones = ["CIPROFLOXACIN", "LEVOFLOXACIN", "MOXIFLOXACIN", "OFLOXACIN", "NORFLOXACIN", "LOMEFLOXACIN"]
azoles = ["FLUCONAZOLE", "ITRACONAZOLE", "KETOCONAZOLE", "MICONAZOLE", "VORICONAZOLE", "POSACONAZOLE"]
add_interaction(["WARFARIN"], macrolides + fluoroquinolones + azoles + ["METRONIDAZOLE", "TINIDAZOLE", "CO-TRIMOXAZOLE"], "تداخل خطير 🔴", 
                "هذه المضادات تمنع استقلاب الوارفارين وترفع تركيزه بشدة، مما يسبب نزيفاً تلقائياً.",
                "These agents inhibit warfarin metabolism, significantly increasing INR and the risk of spontaneous bleeding.")

# 9. Minerals vs Quinolones / Tetracyclines / Thyroid
minerals = ["CALCIUM", "IRON", "MAGNESIUM", "ZINC", "ALUMINUM", "FERROUS SULPHATE", "CALCIUM CARBONATE", "MAGNESIUM OXIDE", "SUCRALFATE", "BISMUTH SUBSALICYLATE"]
antibiotics_chelation = fluoroquinolones + ["DOXYCYCLINE", "TETRACYCLINE", "MINOCYCLINE"]
add_interaction(antibiotics_chelation, minerals, "فشل العلاج 🔴", 
                "المعادن ومضادات الحموضة ترتبط بالمضاد الحيوي في المعدة وتمنع امتصاصه. افصل بـ 2-4 ساعات.",
                "Multivalency cations chelate with antibiotics, preventing their absorption. Separate administration by 2-4 hours.")
add_interaction(["LEVOTHYROXINE"], minerals, "فشل العلاج 🔴", 
                "المعادن والكالسيوم والحديد ومضادات الحموضة ترتبط بهرمون الغدة وتمنع امتصاصه كلياً. يجب الفصل بـ 4 ساعات.",
                "Minerals, calcium, iron, and antacids bind to thyroid hormone and inhibit its absorption. Separate by 4 hours.")

# 10. PPIs vs Clopidogrel
ppis = ["OMEPRAZOLE", "ESOMEPRAZOLE", "LANSOPRAZOLE", "DEXLANSOPRAZOLE", "RABEPRAZOLE"]
add_interaction(["CLOPIDOGREL"], ppis, "تداخل خطير 🔴", 
                "مضادات الحموضة (PPI) تعطل الإنزيم المسؤول عن تفعيل البلافيكس، مما يقلل فاعليته في منع الجلطات.",
                "PPIs (especially omeprazole/esomeprazole) inhibit CYP2C19, reducing active clopidogrel metabolite and antiplatelet efficacy.")

# 11. Statins vs CYP3A4 inhibitors (Macrolides, Azoles, CCBs)
statins_cyp3a4 = ["ATORVASTATIN", "SIMVASTATIN", "LOVASTATIN"]
inhibitors_cyp3a4 = ["CLARITHROMYCIN", "ERYTHROMYCIN", "ITRACONAZOLE", "KETOCONAZOLE", "VERAPAMIL", "DILTIAZEM", "AMIODARONE"]
add_interaction(statins_cyp3a4, inhibitors_cyp3a4, "خطير جداً 🔴", 
                "يرتفع تركيز الستاتين لدرجة سمية مسبباً تكسر العضلات (Rhabdomyolysis) وآلام شديدة قد تؤدي لفشل كلوي.",
                "CYP3A4 inhibition increases statin levels, elevating the risk of myopathy, rhabdomyolysis, and acute kidney injury.")
add_interaction(["SIMVASTATIN", "ROSUVASTATIN", "ATORVASTATIN", "PRAVASTATIN"], ["GEMFIBROZIL"], "تداخل خطير 🔴", 
                "تداخل شديد يرفع خطر تكسر العضلات وضعفها الشديد.",
                "Gemfibrozil inhibits statin glucuronidation, raising statin blood levels and the risk of myopathy/rhabdomyolysis.")

# 12. Digoxin vs Diuretics / Amiodarone / CCBs / Spironolactone
loop_thiazide = ["FUROSEMIDE", "TORSEMIDE", "HYDROCHLOROTHIAZIDE", "INDAPAMIDE", "CHLORTHALIDONE"]
add_interaction(["DIGOXIN"], loop_thiazide, "تداخل خطير 🔴", 
                "مدرات البول تخفض البوتاسيوم في الدم، مما يرفع خطر تسمم الديجوكسين بشكل خطير على نبضات القلب.",
                "Diuretics cause hypokalemia, which sensitizes the myocardium and increases the risk of life-threatening digoxin toxicity.")
add_interaction(["DIGOXIN"], ["AMIODARONE", "VERAPAMIL", "DILTIAZEM", "SPIRONOLACTONE"], "تداخل خطير 🔴", 
                "ترفع هذه الأدوية مستوى الديجوكسين في الدم بشكل سام (يجب خفض جرعة الديجوكسين للنصف).",
                "These drugs increase digoxin serum concentration. Digoxin dose should be reduced by 30-50%.")

# 13. Lithium vs NSAIDs, Thiazides, ACEI, ARB
add_interaction(["LITHIUM"], nsaids + ["HYDROCHLOROTHIAZIDE", "CHLORTHALIDONE", "INDAPAMIDE"] + ace_arbs, "تسمم ليثيوم 🔴", 
                "ترفع هذه الأدوية تركيز الليثيوم للحد السام، مما يسبب رجفة شديدة وتسمم عصبي وفشل كلوي.",
                "These agents decrease lithium clearance, raising serum levels to toxic ranges, leading to neurotoxicity and nephrotoxicity.")

# 14. SSRIs/SNRIs vs Tramadol/MAOIs/Triptans (Serotonin Syndrome)
ssris = ["FLUOXETINE", "SERTRALINE", "CITALOPRAM", "ESCITALOPRAM", "PAROXETINE", "VENLAFAXINE", "DULOXETINE", "DESVENLAFAXINE", "FLUVOXAMINE", "AMITRIPTYLINE", "IMIPRAMINE", "CLOMIPRAMINE", "MIRTAZAPINE", "NORTRIPTYLINE"]
triptans = ["SUMATRIPTAN", "ZOLMITRIPTAN", "RIZATRIPTAN", "ELETRIPTAN", "ALMOTRIPTAN"]
add_interaction(ssris, ["TRAMADOL", "LINEZOLID", "SELEGILINE", "PHENELZINE", "MOCLOBEMIDE"] + triptans, "متلازمة السيروتونين 🔴", 
                "الجمع بينهما قد يؤدي إلى تراكم السيروتونين لدرجة مميتة (ارتفاع حرارة، تشنجات، تسارع قلب).",
                "Combining serotonergic agents increases the risk of Serotonin Syndrome, a life-threatening state.")

# 15. SSRIs vs Antiplatelets / Anticoagulants
add_interaction(ssris, ["ASPIRIN", "CLOPIDOGREL", "WARFARIN", "RIVAROXABAN", "APIXABAN", "DABIGATRAN", "TICAGRELOR"], "خطر النزيف 🟡", 
                "مضادات الاكتئاب تؤثر على وظيفة الصفائح الدموية وتزيد من خطر النزيف عند جمعها مع مميعات الدم.",
                "SSRIs impair platelet serotonin reuptake, increasing bleeding risk when combined with blood thinners.")

# 16. Methotrexate vs NSAIDs/Penicillins/PPIs
add_interaction(["METHOTREXATE"], nsaids + ["AMOXICILLIN", "AMPICILLIN", "PENICILLIN", "PIPERACILLIN", "CEPHALEXIN", "CEFUROXIME"] + ppis, "تسمم خطير 🔴", 
                "تمنع هذه الأدوية الكلى من إخراج الميثوتريكسيت مما يؤدي لتسمم النخاع الشوكي وقمع المناعة الحاد.",
                "These agents compete for renal excretion, raising methotrexate levels to toxic levels (bone marrow suppression).")

# 17. OCPs (Oral Contraceptives) vs Broad Antibiotics / Antiepileptics
ocps = ["ESTROGEN", "PROGESTERONE", "ESTRADIOL", "LEVONORGESTREL", "DROSPIRENONE", "ETHINYLESTRADIOL"]
antiepileptics = ["CARBAMAZEPINE", "PHENYTOIN", "PHENOBARBITAL", "TOPIRAMATE", "PRIMIDONE", "OXCARBAZEPINE"]
add_interaction(ocps, antiepileptics + ["RIFAMPIN", "AMOXICILLIN", "CEPHALEXIN", "DOXYCYCLINE", "TETRACYCLINE"], "فشل منع الحمل 🔴", 
                "تفرز هذه الأدوية مضادات أو تنشط إنزيمات الكبد لتكسير هرمونات منع الحمل بسرعة، مما يفشل مفعول الحبوب.",
                "Enzyme inducers accelerate estrogen/progesterone clearance, compromising contraceptive efficacy.")

# 18. Clarithromycin vs Colchicine
add_interaction(["CLARITHROMYCIN", "ERYTHROMYCIN", "ITRACONAZOLE", "KETOCONAZOLE", "VERAPAMIL", "DILTIAZEM", "CYCLOSPORINE"], ["COLCHICINE"], "تفاعل قاتل 🔴", 
                "يمنع تكسير الكولشيسين مما يسبب تسمماً عصبياً وعضلياً حاداً وقاتلاً (خاصة لمرضى الكبد والكلى).",
                "CYP3A4/P-gp inhibition by clarithromycin leads to fatal colchicine toxicity (neuromyopathy, bone marrow failure).")

# 19. Tamoxifen vs SSRIs
add_interaction(["TAMOXIFEN"], ["FLUOXETINE", "PAROXETINE", "BUPROPION", "SERTRALINE"], "فشل العلاج 🔴", 
                "تمنع هذه الأدوية تحول التاموكسيفين إلى مادته الفعالة (Endoxifen) مما يقلل فاعليته المضادة للسرطان.",
                "CYP2D6 inhibitors prevent tamoxifen activation to endoxifen, reducing its breast cancer therapy efficacy.")

# 20. QT Prolongation
qt_drugs = ["AMIODARONE", "SOTALOL", "CLARITHROMYCIN", "AZITHROMYCIN", "MOXIFLOXACIN", "LEVOFLOXACIN", "HALOPERIDOL", "QUETIAPINE", "ONDANSETRON", "CITALOPRAM", "DOMPERIDONE", "CHLORPROMAZINE", "RISPERIDONE", "OLANZAPINE", "ZIPRASIDONE", "ERYTHROMYCIN"]
for d1, d2 in itertools.combinations(qt_drugs, 2):
    desc_ar = "الجمع بين دواءين يطيلان فترة QT في تخطيط القلب قد يسبب تسارع بطيني قاتل (Torsades de Pointes)."
    desc_en = "Concomitant use of QT-prolonging drugs increases the risk of life-threatening ventricular arrhythmias."
    desc = f"{desc_ar}<div style='direction: ltr; text-align: left; margin-top: 8px; font-size: 12.5px; opacity: 0.85; border-top: 1px solid rgba(0,0,0,0.06); padding-top: 6px; font-family: sans-serif;'>{desc_en}</div>"
    interactions.append({
        "drugs": sorted([d1, d2]),
        "severity": "اضطراب القلب 🔴",
        "desc": desc
    })

# 21. Beta blockers vs Verapamil/Diltiazem
beta_blockers = ["BISOPROLOL", "METOPROLOL", "ATENOLOL", "PROPRANOLOL", "NEBIVOLOL", "CARVEDILOL", "LABETALOL", "SOTALOL"]
add_interaction(beta_blockers, ["VERAPAMIL", "DILTIAZEM"], "تداخل خطير 🔴", 
                "الجمع يسبب هبوطاً شديداً في ضربات القلب (Bradycardia) وضعفاً في انقباض عضلته قد يؤدي لتوقف القلب.",
                "Concurrent use causes additive negative inotropic and chronotropic effects, risking severe bradycardia or heart block.")

# 22. Allopurinol vs Azathioprine
add_interaction(["ALLOPURINOL", "FEBUXOSTAT"], ["AZATHIOPRINE", "MERCAPTOPURINE"], "تداخل قاتل 🔴", 
                "يمنع تكسير دواء المناعة (Azathioprine) مما يسبب تسمم نخاع العظم الحاد ونقص كريات الدم البيضاء الشديد.",
                "Xanthine oxidase inhibition by allopurinol elevates azathioprine active metabolites, causing life-threatening myelosuppression.")

# 23. Benzodiazepines & Sedative Antihistamines vs Opioids & Alcohol
benzos = ["ALPRAZOLAM", "DIAZEPAM", "LORAZEPAM", "CLONAZEPAM", "BROMAZEPAM", "MIDAZOLAM", "ZOLPIDEM", "ZOPICLONE"]
sedatives = ["HYDROXYZINE", "CHLORPHENIRAMINE", "DIPHENHYDRAMINE", "PROMETHAZINE", "CYPROHEPTADINE"]
options_group = ["TRAMADOL", "CODEINE", "MORPHINE", "OXYCODONE", "HYDROCODONE", "FENTANYL", "METHADONE", "BUPRENORPHINE"]
add_interaction(benzos + sedatives, options_group, "تثبيط تنفسي 🔴", 
                "الجمع بين المهدئات ومسكنات الألم الأفيونية يسبب خمولاً شديداً وتثبيطاً لمركز التنفس في المخ قد يؤدي للوفاة.",
                "Concurrent use of CNS depressants causes additive respiratory depression, profound sedation, coma, or death.")

# 24. Ciprofloxacin vs Theophylline
add_interaction(["CIPROFLOXACIN", "NORFLOXACIN"], ["THEOPHYLLINE", "AMINOPHYLLINE"], "تداخل خطير 🔴", 
                "المضاد الحيوي يمنع تكسير الثيوفيلين ويرفع تركيزه للحد السام مسبباً تشنجات واضطراب نبضات القلب.",
                "Ciprofloxacin inhibits CYP1A2, raising theophylline levels and increasing risks of seizures and arrhythmias.")

# 25. Warfarin vs Thyroid Hormone (Levothyroxine)
add_interaction(["WARFARIN"], ["LEVOTHYROXINE"], "تداخل متوسط 🟡", 
                "هرمون الغدة يزيد من تكسير عوامل التجلط مما يزيد من فاعلية الوارفارين وخطر النزيف عند بدء علاج الغدة.",
                "Thyroid hormone increases clotting factor catabolism, enhancing warfarin effect and increasing bleeding risk.")

# 26. NSAIDs vs Cyclosporine / Tacrolimus
add_interaction(nsaids, ["CYCLOSPORINE", "TACROLIMUS"], "تسمم كلوي 🔴", 
                "الجمع يسبب تضيقاً شديداً في شرايين الكلية ويرفع سمية أدوية المناعة على الكليتين.",
                "NSAIDs cause renal vasoconstriction, synergistically exacerbating calcineurin inhibitor nephrotoxicity.")

# 27. Metformin vs Contrast Media (Iodinated)
add_interaction(["METFORMIN"], ["IODINATED CONTRAST", "CONTRAST MEDIA"], "حموضة لاكتية 🔴", 
                "صبغات الأشعة قد تسبب فشل كلوي مؤقت يؤدي لتراكم الميتفورمين وحدوث حموضة لاكتية قاتلة. يجب إيقاف الميتفورمين 48 ساعة.",
                "Iodinated contrast may cause acute kidney injury, leading to metformin accumulation and fatal lactic acidosis.")

# 28. Acid reducers vs Azole Antifungals & Iron
acid_reducers = ppis + ["FAMOTIDINE", "RANITIDINE", "CIMETIDINE"]
add_interaction(azoles + ["IRON", "FERROUS SULPHATE"], acid_reducers, "فشل العلاج 🟡", 
                "هذه المركبات تحتاج بيئة حمضية للامتصاص، وتقليل حموضة المعدة يفشل علاج الفطريات أو نقص الحديد.",
                "Decreased gastric acidity impairs dissolution and absorption of ketoconazole, itraconazole, and oral iron.")

# 29. Levodopa vs Iron
add_interaction(["LEVODOPA"], ["IRON", "FERROUS SULPHATE"], "فشل العلاج 🟡", 
                "يرتبط الحديد بالليفودوبا ويقلل امتصاصه ومفعوله بشكل كبير لدى مرضى الشلل الرعاش.",
                "Iron chelates with levodopa in the gastrointestinal tract, significantly reducing its bioavailability and clinical efficacy.")

# 30. Aminoglycosides vs Loop Diuretics
aminoglycosides = ["GENTAMICIN", "AMIKACIN", "TOBRAMYCIN", "NEOMYCIN", "STREPTOMYCIN"]
add_interaction(aminoglycosides, ["FUROSEMIDE", "TORSEMIDE", "BUMETANIDE"], "سمية سمعية وكلوية 🔴", 
                "الجمع بينهما يزيد بشدة من خطر حدوث الصمم الدائم والفشل الكلوي الحاد.",
                "Co-administration increases the risk of additive nephrotoxicity and irreversible ototoxicity.")

# 31. Valproate vs Lamotrigine
add_interaction(["VALPROIC ACID", "SODIUM VALPROATE"], ["LAMOTRIGINE"], "تفاعل جلدي خطير 🔴", 
                "يثبط الفالبروات تكسير اللاموتريجين مما يرفع مستواه للضعف ويزيد من خطر الطفح الجلدي المميت (متلازمة ستيفنز جونسون).",
                "Valproate inhibits lamotrigine glucuronidation, doubling its half-life and increasing the risk of Stevens-Johnson syndrome.")

# 32. Antidiabetics vs Beta blockers
diabetics_hypo = ["GLIMEPIRIDE", "GLICLAZIDE", "GLIBENCLAMIDE", "REPAGLINIDE", "NATEGLINIDE", "METFORMIN"]
add_interaction(diabetics_hypo, beta_blockers, "إخفاء الأعراض 🟡", 
                "حاصرات بيتا تخفي أعراض هبوط السكر التحذيرية (مثل ضربات القلب السريعة والرجفة) وقد تؤخر التعافي من الهبوط.",
                "Beta-blockers mask hypoglycemic warning signs (tremor, tachycardia) and can delay recovery from hypoglycemia.")

# 33. Methadone vs CYP3A4 inhibitors
add_interaction(["METHADONE"], ["CLARITHROMYCIN", "KETOCONAZOLE", "ITRACONAZOLE", "FLUCONAZOLE", "AMIODARONE"], "تداخل خطير 🔴", 
                "يزيد تركيز الميثادون في الدم مما يرفع خطر النعاس الشديد، هبوط التنفس واضطراب نبضات القلب.",
                "CYP3A4 inhibitors decrease methadone clearance, increasing risk of respiratory depression and QT prolongation.")

# Write to file
with open(r'c:\Users\HP\testmono\interactions_db\drug_drug.json', 'w', encoding='utf-8') as f:
    json.dump(interactions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated massive drug_drug.json with {len(interactions)} unique interactions!")

const fs = require('fs');
const path = require('path');

const timeline = {};

const groups = [
    // NSAIDs
    {
        drugs: ["IBUPROFEN", "DICLOFENAC", "NAPROXEN", "KETOPROFEN", "MELOXICAM", "PIROXICAM", "CELECOXIB", "ETORICOXIB", "INDOMETHACIN", "LORNOXICAM", "TENOXICAM", "ACECLOFENAC", "DEXKETOPROFEN", "FLURBIPROFEN", "MEFENAMIC ACID", "NABUMETONE", "SULINDAC", "TOLMETIN", "DIFLUNISAL", "OXAPROZIN"],
        timeline: "⏰ مسكنات ومضادات التهاب (NSAIDs): بعد الأكل مباشرة مع كوب ماء كبير لمنع تهيج وتقرحات المعدة."
    },
    // PPIs and H2 Blockers
    {
        drugs: ["OMEPRAZOLE", "PANTOPRAZOLE", "ESOMEPRAZOLE", "LANSOPRAZOLE", "RABEPRAZOLE", "DEXLANSOPRAZOLE"],
        timeline: "⏰ أدوية المعدة (PPIs): على الريق صباحاً قبل الإفطار بـ 30 إلى 60 دقيقة للوصول لأقصى فاعلية."
    },
    {
        drugs: ["FAMOTIDINE", "RANITIDINE", "CIMETIDINE", "NIZATIDINE"],
        timeline: "⏰ مضادات حموضة (H2): قبل النوم أو قبل الوجبة بـ 15-30 دقيقة."
    },
    // Antacids
    {
        drugs: ["ALUMINUM HYDROXIDE", "MAGNESIUM HYDROXIDE", "CALCIUM CARBONATE", "SODIUM BICARBONATE"],
        timeline: "⏰ مضادات الحموضة الموضعية: بعد الأكل بساعة إلى ساعتين، وتفصل عن أي دواء آخر بساعتين."
    },
    // Statins and Fibrates
    {
        drugs: ["ATORVASTATIN", "ROSUVASTATIN", "SIMVASTATIN", "PRAVASTATIN", "LOVASTATIN", "FLUVASTATIN", "PITAVASTATIN"],
        timeline: "⏰ أدوية الكوليسترول (Statins): مساءً قبل النوم للحصول على أعلى فاعلية لأن الكبد يصنع الكوليسترول ليلاً."
    },
    {
        drugs: ["FENOFIBRATE", "GEMFIBROZIL", "BEZAFIBRATE"],
        timeline: "⏰ خافضات الدهون (Fibrates): مع الوجبة لزيادة الامتصاص وتقليل ألم المعدة."
    },
    {
        drugs: ["EZETIMIBE"],
        timeline: "⏰ إيزيتيميب: في أي وقت من اليوم، مع أو بدون طعام."
    },
    // Antidiabetics
    {
        drugs: ["METFORMIN"],
        timeline: "⏰ مساعد السكر (Metformin): وسط الوجبة الرئيسية أو بعدها مباشرة لتجنب المغص والانتفاخ واضطراب الأمعاء."
    },
    {
        drugs: ["GLIBENCLAMIDE", "GLIMEPIRIDE", "GLICLAZIDE", "GLIPIZIDE", "REPAGLINIDE", "NATEGLINIDE"],
        timeline: "⏰ محفزات الإنسولين: قبل الإفطار أو أول وجبة رئيسية بـ 15-30 دقيقة لتجنب هبوط السكر المفاجئ."
    },
    {
        drugs: ["EMPAGLIFLOZIN", "DAPAGLIFLOZIN", "CANAGLIFLOZIN", "VILDAGLIPTIN", "SITAGLIPTIN", "LINAGLIPTIN", "SAXAGLIPTIN", "ALOGLIPTIN"],
        timeline: "⏰ أدوية السكر الحديثة: مرة واحدة يومياً في الصباح، مع أو بدون طعام."
    },
    {
        drugs: ["PIOGLITAZONE", "ROSIGLITAZONE"],
        timeline: "⏰ بيوجليتازون: مرة واحدة يومياً، مع أو بدون طعام."
    },
    {
        drugs: ["ACARBOSE", "MIGLITOL"],
        timeline: "⏰ أكاربوز: مع أول لقمة من الوجبة لتقليل امتصاص النشويات."
    },
    {
        drugs: ["LIRAGLUTIDE", "DULAGLUTIDE", "SEMAGLUTIDE", "EXENATIDE"],
        timeline: "⏰ حقن السكر للتخسيس (GLP-1): تؤخذ في أي وقت بغض النظر عن الوجبات، ويفضل تثبيت الموعد (يومياً أو أسبوعياً حسب النوع)."
    },
    // Antihypertensives (ACE, ARB, CCB, Beta Blockers, Diuretics)
    {
        drugs: ["PERINDOPRIL", "RAMIPRIL", "ENALAPRIL", "LISINOPRIL", "FOSINOPRIL", "TRANDOLAPRIL", "BENAZEPRIL", "QUINAPRIL"],
        timeline: "⏰ مثبطات الإنزيم المحول (ACE): يفضل في الصباح الباكر لتحقيق أقصى تحكم في ضغط الدم."
    },
    {
        drugs: ["CAPTOPRIL"],
        timeline: "⏰ كابتوبريل: قبل الأكل بساعة أو بعده بساعتين (الطعام يقلل امتصاصه بشكل كبير)."
    },
    {
        drugs: ["VALSARTAN", "LOSARTAN", "CANDESARTAN", "TELMISARTAN", "IRBESARTAN", "OLMESARTAN", "AZILSARTAN", "EPROSARTAN"],
        timeline: "⏰ مضادات مستقبلات الأنجيوتنسين (ARBs): مرة واحدة يومياً في نفس الوقت، مع أو بدون طعام."
    },
    {
        drugs: ["BISOPROLOL", "METOPROLOL", "ATENOLOL", "CARVEDILOL", "PROPRANOLOL", "NEBIVOLOL", "SOTALOL", "LABETALOL", "PINDOLOL", "TIMOLOL"],
        timeline: "⏰ حاصرات بيتا (Beta Blockers): يفضل صباحاً مع أو بدون طعام. (إذا سببت أحلام مزعجة تجنب أخذها ليلاً)."
    },
    {
        drugs: ["AMLODIPINE", "NIFEDIPINE", "DILTIAZEM", "VERAPAMIL", "FELODIPINE", "LERCANIDIPINE", "NIMODIPINE", "NICARDIPINE"],
        timeline: "⏰ حاصرات قنوات الكالسيوم: مرة واحدة يومياً، في نفس الوقت مع أو بدون طعام."
    },
    {
        drugs: ["FUROSEMIDE", "TORSEMIDE", "HYDROCHLOROTHIAZIDE", "INDAPAMIDE", "CHLORTHALIDONE", "BUMETANIDE"],
        timeline: "⏰ مدرات البول: صباحاً (أو الجرعة الأخيرة قبل الساعة 4 عصراً) لتجنب الاستيقاظ ليلاً للتبول."
    },
    {
        drugs: ["SPIRONOLACTONE", "EPLERENONE", "AMILORIDE", "TRIAMTERENE"],
        timeline: "⏰ مدر بول حافظ للبوتاسيوم: صباحاً أو ظهراً لتجنب إدرار البول ليلاً. يفضل مع الطعام لزيادة امتصاصه."
    },
    {
        drugs: ["DOXAZOSIN", "PRAZOSIN", "TERAZOSIN", "TAMSULOSIN", "ALFUZOSIN", "SILODOSIN"],
        timeline: "⏰ حاصرات ألفا (للضغط والبروستاتا): الجرعة الأولى يجب أن تؤخذ عند النوم لتجنب الدوخة وهبوط الضغط المفاجئ، (تاسمولوسين يؤخذ بعد العشاء بنصف ساعة)."
    },
    {
        drugs: ["CLONIDINE", "METHYLDOPA"],
        timeline: "⏰ أدوية الضغط المركزية: تنقسم الجرعات، وتؤخذ أكبر جرعة ليلاً لتجنب النعاس نهاراً."
    },
    // Endocrine & Hormones
    {
        drugs: ["LEVOTHYROXINE", "EUTHYROX", "THYROXINE", "LIOTHYRONINE"],
        timeline: "⏰ هرمون الغدة الدرقية: فور الاستيقاظ على معدة فارغة تماماً مع كوب ماء فقط، والانتظار 45-60 دقيقة قبل أي طعام أو شرب قهوة."
    },
    {
        drugs: ["CARBIMAZOLE", "METHIMAZOLE", "PROPYLTHIOURACIL"],
        timeline: "⏰ مضادات الغدة الدرقية: مع الطعام في نفس الوقت يومياً، وتقسم على مدار اليوم للحفاظ على المستوى."
    },
    {
        drugs: ["PREDNISOLONE", "DEXAMETHASONE", "METHYLPREDNISOLONE", "HYDROCORTISONE", "PREDNISONE", "BETAMETHASONE", "DEFLAZACORT"],
        timeline: "⏰ الكورتيزون: يجب أخذه في الصباح الباكر (بين 7-9 صباحاً) ليتوافق مع الإفراز الطبيعي للجسم، وبعد الإفطار لحماية المعدة."
    },
    // Minerals and Vitamins
    {
        drugs: ["IRON", "FERROUS SULPHATE", "FERROUS FUMARATE", "FERRIC", "FERROUS GLUCONATE", "IRON POLYMALTOSE"],
        timeline: "⏰ مكملات الحديد: على معدة فارغة (ساعة قبل الأكل) مع عصير برتقال لزيادة الامتصاص. تجنب الشاي والحليب لساعتين."
    },
    {
        drugs: ["CALCIUM", "CALCIUM CARBONATE"],
        timeline: "⏰ مكملات الكالسيوم: مع وجبة الطعام لزيادة امتصاصه بفعل حمض المعدة."
    },
    {
        drugs: ["CALCIUM CITRATE"],
        timeline: "⏰ مكملات الكالسيوم (سترات): يمكن أخذها مع أو بدون طعام (لا تتأثر بحمض المعدة)."
    },
    {
        drugs: ["VITAMIN D3", "CHOLECALCIFEROL", "ALFACALCIDOL", "CALCITRIOL"],
        timeline: "⏰ فيتامين د: مع وجبة دسمة تحتوي على دهون (مثل الإفطار أو الغداء) لضمان الامتصاص الكامل."
    },
    {
        drugs: ["VITAMIN C", "ASCORBIC ACID", "VITAMIN B", "B-COMPLEX", "ZINC", "THIAMINE", "PYRIDOXINE", "CYANOCOBALAMIN", "FOLIC ACID"],
        timeline: "⏰ الفيتامينات الذائبة في الماء والزنك: يمكن أخذها في أي وقت، لكن يفضل مع الطعام لتجنب اضطراب المعدة."
    },
    {
        drugs: ["MAGNESIUM", "MAGNESIUM CITRATE", "MAGNESIUM OXIDE", "MAGNESIUM GLYCINATE"],
        timeline: "⏰ المغنيسيوم: يفضل مساءً أو قبل النوم حيث يساعد على استرخاء العضلات وتحسين جودة النوم."
    },
    // Antihistamines
    {
        drugs: ["LORATADINE", "DESLORATADINE", "FEXOFENADINE", "BILASTINE", "RUPATADINE"],
        timeline: "⏰ مضادات الحساسية (لا تسبب النعاس): مرة واحدة يومياً في أي وقت، يفضل صباحاً. البیلاستین يؤخذ على معدة فارغة."
    },
    {
        drugs: ["CETIRIZINE", "LEVOCETIRIZINE", "CHLORPHENIRAMINE", "DIPHENHYDRAMINE", "HYDROXYZINE", "KETOTIFEN", "CLEMASTINE", "CYPROHEPTADINE"],
        timeline: "⏰ مضادات الحساسية (قد تسبب النعاس): يفضل أخذها مساءً قبل النوم."
    },
    // Antibiotics
    {
        drugs: ["AMOXICILLIN", "AMOXICILLIN+CLAVULANATE", "AMPICILLIN", "PENICILLIN V", "FLUCLOXACILLIN", "DICLOXACILLIN", "OXACILLIN", "CLOXACILLIN", "PIPERACILLIN"],
        timeline: "⏰ البنسلينات: يفضل مع بداية الوجبة أو بعدها لتقليل اضطراب الأمعاء والمعدة. الفلوكلوكساسيلين يؤخذ على معدة فارغة."
    },
    {
        drugs: ["CEFUROXIME", "CEFIXIME", "CEFDINIR", "CEPHALEXIN", "CEFADROXIL", "CEFPODOXIME", "CEFACLOR", "CEFTIBUTEN", "CEFDITOREN", "CEFPROZIL"],
        timeline: "⏰ السيفالوسبورينات: يفضل تناولها مع الطعام لتجنب الغثيان والمغص."
    },
    {
        drugs: ["CIPROFLOXACIN", "LEVOFLOXACIN", "MOXIFLOXACIN", "NORFLOXACIN", "OFLOXACIN", "LOMEFLOXACIN", "GEMIFLOXACIN"],
        timeline: "⏰ الفلوروكينولون (مضاد حيوي): قبل الأكل بساعة أو بعده بساعتين. افصل بينها وبين منتجات الألبان والمعادن بـ 4 ساعات."
    },
    {
        drugs: ["AZITHROMYCIN"],
        timeline: "⏰ أزيثروميسين: الكبسولات والسائل تؤخذ على معدة فارغة. الأقراص يمكن أخذها مع الطعام."
    },
    {
        drugs: ["CLARITHROMYCIN", "ERYTHROMYCIN", "ROXITHROMYCIN"],
        timeline: "⏰ الماكرولايد (مثل كلاريثرومايسين): يمكن تناوله مع أو بدون طعام، ويفضل مع الطعام لتقليل الغثيان (الاريثرومايسين يفضل على معدة فارغة)."
    },
    {
        drugs: ["METRONIDAZOLE", "TINIDAZOLE", "ORNIDAZOLE", "SECNIDAZOLE"],
        timeline: "⏰ مطهرات الأمعاء (فلاجيل وأخواته): مع الأكل أو بعده لتخفيف الطعم المعدني. (تحذير صارم: يمنع تناول الكحوليات أثناء الكورس)."
    },
    {
        drugs: ["DOXYCYCLINE", "TETRACYCLINE", "MINOCYCLINE"],
        timeline: "⏰ التتراسيكلينات (دوكسي سايكلين): مع كوب ماء كبير والجلوس أو الوقوف لمدة 30 دقيقة. تجنب الحليب والمعادن بـ ساعتين."
    },
    {
        drugs: ["CLINDAMYCIN", "LINCOMYCIN"],
        timeline: "⏰ الكليندامايسين: مع كوب كامل من الماء لمنع تهيج المريء، يمكن أخذه مع الطعام."
    },
    {
        drugs: ["NITROFURANTOIN"],
        timeline: "⏰ نيتروفورانتوين (لمسالك البول): مع الحليب أو الطعام لزيادة الامتصاص ومنع الغثيان الشديد."
    },
    {
        drugs: ["TRIMETHOPRIM", "SULFAMETHOXAZOLE", "CO-TRIMOXAZOLE"],
        timeline: "⏰ السلفا (سبترين): يجب شرب كميات وفيرة من الماء على مدار اليوم لتجنب تكون حصوات الكلى."
    },
    // Antifungals & Antivirals
    {
        drugs: ["FLUCONAZOLE", "KETOCONAZOLE", "VORECONAZOLE", "MICONAZOLE", "TERBINAFINE", "GRISEOFULVIN"],
        timeline: "⏰ مضادات الفطريات: فلوكونازول بأي وقت. الكيتوكونازول والتيربينافين والجريسيوفولفين مع وجبة دهنية."
    },
    {
        drugs: ["ITRACONAZOLE"],
        timeline: "⏰ إيتراكونازول: يجب أخذه مباشرة بعد وجبة كاملة مع مشروب حمضي (مثل الكولا أو البرتقال)."
    },
    {
        drugs: ["ACYCLOVIR", "VALACYCLOVIR", "FAMCICLOVIR", "OSELTAMIVIR", "ZANAMIVIR"],
        timeline: "⏰ مضادات الفيروسات: تؤخذ على فترات متساوية. أوسيلتاميفير (تاميفلو) يؤخذ مع الطعام لمنع القيء."
    },
    // Anticoagulants and Antiplatelets
    {
        drugs: ["ASPIRIN"],
        timeline: "⏰ أسبرين الأطفال: يفضل بعد الغداء أو العشاء مباشرة مع كوب ماء كبير."
    },
    {
        drugs: ["CLOPIDOGREL", "TICAGRELOR", "PRASUGREL", "CILOSTAZOL", "DIPYRIDAMOLE"],
        timeline: "⏰ مضادات التجلط والصفائح: في نفس الموعد يومياً، سيلوستازول يؤخذ على معدة فارغة."
    },
    {
        drugs: ["WARFARIN", "RIVAROXABAN", "APIXABAN", "DABIGATRAN", "EDOXABAN"],
        timeline: "⏰ مميعات الدم: الوارفارين مساءً. ريفاروكسابان (15/20 ملغ) يجب أخذه مع وجبة دسمة. دابيجاتران مع كوب ماء كبير."
    },
    // Erectile Dysfunction
    {
        drugs: ["SILDENAFIL", "VARDENAFIL", "TADALAFIL", "AVANAFIL"],
        timeline: "⏰ المنشطات: قبل النشاط بـ 1 ساعة. (سيلدينافيل يتأثر بالوجبات الدسمة ويؤخر المفعول، تادالافيل لا يتأثر)."
    },
    // Osteoporosis and Gout
    {
        drugs: ["ALENDRONATE", "RISEDRONATE", "IBANDRONATE", "ZOLEDRONIC ACID", "PAMIDRONATE", "ETIDRONATE"],
        timeline: "⏰ هشاشة العظام (Biphosphonates): فور الاستيقاظ على معدة فارغة مع كوب ماء كامل، والجلوس أو الوقوف مستقيماً لمدة 30-60 دقيقة وتجنب الأكل."
    },
    {
        drugs: ["ALLOPURINOL", "FEBUXOSTAT", "PROBENECID"],
        timeline: "⏰ أدوية النقرس: يفضل بعد الأكل لتجنب التهاب المعدة. مع شرب كميات كبيرة من الماء يومياً."
    },
    {
        drugs: ["COLCHICINE"],
        timeline: "⏰ الكولشيسين (النقرس الحاد): يؤخذ مع أو بدون طعام، وبمجرد حدوث إسهال شديد يجب التوقف فوراً."
    },
    // Autoimmune and Rheumatic
    {
        drugs: ["METHOTREXATE", "LEFLUNOMIDE", "HYDROXYCHLOROQUINE", "SULFASALAZINE", "AZATHIOPRINE", "CYCLOSPORINE", "TACROLIMUS", "MYCOPHENOLATE"],
        timeline: "⏰ أدوية المناعة: ميثوتريكسيت جرعة أسبوعية فقط. هيدروكسي كلوروكين مع الأكل. الالتزام الصارم بالموعد وتجنب الجريب فروت للمثبطات القوية."
    },
    // Respiratory
    {
        drugs: ["SALBUTAMOL", "FORMOTEROL", "SALMETEROL", "ALBUTEROL", "TERBUTALINE"],
        timeline: "⏰ موسعات الشعب الهوائية: البخاخات سريعة المفعول عند اللزوم، بينما طويلة المفعول مرتين يومياً صباحاً ومساءً (تأثيرها يستمر 12 ساعة)."
    },
    {
        drugs: ["FLUTICASONE", "BUDESONIDE", "BECLOMETASONE", "MOMETASONE", "CICLESONIDE"],
        timeline: "⏰ كورتيزون استنشاقي: يجب المضمضة بالماء وبصق الماء بعد كل استخدام لتجنب الفطريات الفموية (الكانديدا)."
    },
    {
        drugs: ["MONTELUKAST", "ZAFIRLUKAST"],
        timeline: "⏰ مونتيلوكاست (حساسية الصدر): جرعة واحدة مساءً للمساعدة على منع نوبات الربو الليلية."
    },
    {
        drugs: ["THEOPHYLLINE", "AMINOPHYLLINE"],
        timeline: "⏰ الثيوفيلين: يجب تثبيت طريقة الأكل مع الجرعة لأن التغيير المفاجئ في الأكل (خاصة اللحوم المشوية) يغير تركيز الدواء بالدم."
    },
    // Gastrointestinal
    {
        drugs: ["DOMPERIDONE", "METOCLOPRAMIDE", "ONDANSETRON", "MECLIZINE", "PROMETHAZINE", "GRANISETRON", "PALONOSETRON"],
        timeline: "⏰ مضادات القيء والغثيان: تؤخذ قبل الأكل بـ 15-30 دقيقة لمنع الغثيان قبل وصول الطعام للمعدة."
    },
    {
        drugs: ["LOPERAMIDE", "DIPHENOXYLATE", "BISMUTH SUBSALICYLATE"],
        timeline: "⏰ أدوية الإسهال: كبسولتين عند أول نوبة إسهال، ثم كبسولة بعد كل نوبة. مع شرب سوائل كثيرة لتعويض الجفاف."
    },
    {
        drugs: ["BISACODYL", "SENNA", "LACTULOSE", "MACROGOL", "PSYLLIUM", "METHYLCELLULOSE", "DOCUSATE", "GLYCERIN"],
        timeline: "⏰ الملينات: بيساكوديل وسنا تؤخذ قبل النوم لتعمل في الصباح (تستغرق 6-12 ساعة). الملينات الليفية يجب شربها مع كمية ضخمة من الماء."
    },
    {
        drugs: ["HYOSCINE", "MEBEVERINE", "OTILONIUM", "DROTAVERINE", "ALVERINE", "TRIMEBUTINE"],
        timeline: "⏰ مضادات التقلصات (للقولون): تؤخذ قبل الوجبات بـ 20 دقيقة لتجنب التقلصات التي تحدث مع دخول الطعام."
    },
    {
        drugs: ["URSODEOXYCHOLIC ACID"],
        timeline: "⏰ أدوية المرارة: تؤخذ مع الطعام وأثناء أو بعد الوجبات للحصول على أفضل امتصاص وتأثير."
    },
    // Cardiovascular specifics
    {
        drugs: ["ISOSORBIDE DINITRATE", "ISOSORBIDE MONONITRATE", "NITROGLYCERIN"],
        timeline: "⏰ النترات (للذبحة): يجب ترك فترة خالية من النترات (8-12 ساعة ليلاً) لمنع تعود الجسم عليها وضعف تأثيرها."
    },
    {
        drugs: ["DIGOXIN"],
        timeline: "⏰ ديجوكسين (مضخة القلب): في نفس الموعد يومياً. تجنب تغيير كمية الألياف في طعامك فجأة لأن الألياف تقلل الامتصاص."
    },
    {
        drugs: ["AMIODARONE", "FLECAINIDE", "PROPAFENONE"],
        timeline: "⏰ مضادات اضطراب النظم: الأميودارون يفضل مع الطعام لتقليل اضطراب المعدة. الالتزام الصارم بوقت الجرعة ضروري."
    },
    // Analgesics (Non-NSAID)
    {
        drugs: ["PARACETAMOL", "ACETAMINOPHEN"],
        timeline: "⏰ باراسيتامول: عند اللزوم لتخفيف الألم أو الحرارة، بفاصل 4-6 ساعات، والحد الأقصى 4 جرام يومياً (أو أقل لمرضى الكبد)."
    },
    {
        drugs: ["TRAMADOL", "CODEINE", "MORPHINE", "OXYCODONE", "HYDROCODONE", "FENTANYL", "BUPRENORPHINE", "METHADONE", "TAPENTADOL"],
        timeline: "⏰ المسكنات الأفيونية (Narcotics): مع أو بدون طعام. تحذير قوي: تسبب النعاس والإمساك، وينصح بملينات احترازية وشرب ماء وفير."
    },
    // Neurological & Psychiatric
    {
        drugs: ["AMITRIPTYLINE", "IMIPRAMINE", "CLOMIPRAMINE", "DOXEPIN", "NORTRIPTYLINE"],
        timeline: "⏰ مضادات الاكتئاب الثلاثية (TCAs): تسبب النعاس الشديد، يجب أخذ الجرعة بالكامل مساءً قبل النوم."
    },
    {
        drugs: ["FLUOXETINE", "SERTRALINE", "CITALOPRAM", "ESCITALOPRAM", "PAROXETINE", "FLUVOXAMINE"],
        timeline: "⏰ مضادات الاكتئاب (SSRIs): تؤخذ صباحاً لأنها قد تسبب الأرق (باستثناء الفلوفوكسامين والباروكستين قد يسببان النعاس فيفضل ليلاً)."
    },
    {
        drugs: ["VENLAFAXINE", "DULOXETINE", "DESVENLAFAXINE"],
        timeline: "⏰ مضادات الاكتئاب (SNRIs): يفضل مع الطعام لتقليل الغثيان، والجرعة عادة تكون في الصباح."
    },
    {
        drugs: ["MIRTAZAPINE"],
        timeline: "⏰ ميرتازابين: يسبب نعاس شديد وفتح الشهية، يؤخذ قبل النوم مباشرة."
    },
    {
        drugs: ["ALPRAZOLAM", "DIAZEPAM", "LORAZEPAM", "CLONAZEPAM", "BROMAZEPAM", "CHLORDIAZEPOXIDE"],
        timeline: "⏰ المهدئات (Benzodiazepines): تؤخذ عند اللزوم أو قبل النوم حسب وصف الطبيب. يحذر القيادة أو التعامل مع الآلات."
    },
    {
        drugs: ["ZOLPIDEM", "ZOPICLONE", "ESZOPICLONE"],
        timeline: "⏰ أدوية النوم (Z-drugs): تؤخذ في السرير قبل النوم مباشرة، ويجب توفر 7-8 ساعات كاملة للنوم بعد الجرعة."
    },
    {
        drugs: ["QUETIAPINE", "OLANZAPINE", "CLOZAPINE", "CHLORPROMAZINE", "HALOPERIDOL", "RISPERIDONE", "ARIPIPRAZOLE"],
        timeline: "⏰ مضادات الذهان: الأدوية التي تسبب نعاساً (كيوتيابين، أولانزابين) تؤخذ مساءً. الأريبيبرازول يؤخذ صباحاً عادةً."
    },
    {
        drugs: ["LITHIUM"],
        timeline: "⏰ الليثيوم (مثبت المزاج): يجب شرب 2-3 لتر ماء يومياً والحفاظ على مستوى ثابت من الملح في الطعام."
    },
    {
        drugs: ["VALPROIC ACID", "CARBAMAZEPINE", "PHENYTOIN", "LAMOTRIGINE", "LEVETIRACETAM", "TOPIRAMATE", "GABAPENTIN", "PREGABALIN"],
        timeline: "⏰ أدوية الصرع والتهاب الأعصاب: يجب تثبيت موعد الجرعات بشكل صارم جداً لمنع التشنجات. يمكن مع الطعام لتقليل الغثيان."
    },
    {
        drugs: ["DONEPEZIL", "RIVASTIGMINE", "GALANTAMINE", "MEMANTINE"],
        timeline: "⏰ أدوية الزهايمر: دونيبيزيل يؤخذ مساءً. يجب تناول الدواء بانتظام وبنفس التوقيت مع وجبة خفيفة لتخفيف الغثيان."
    },
    {
        drugs: ["LEVODOPA", "CARBIDOPA", "ROPINIROLE", "PRAMIPEXOLE", "ENTACAPONE", "SELEGILINE", "RASAGILINE"],
        timeline: "⏰ أدوية الشلل الرعاش (Parkinson's): ليفودوبا تؤخذ على معدة فارغة أو مع وجبة خالية من البروتين الثقيل لضمان الامتصاص السريع للحركة."
    },
    // Triptans (Migraine)
    {
        drugs: ["SUMATRIPTAN", "ZOLMITRIPTAN", "RIZATRIPTAN", "ELETRIPTAN", "ALMOTRIPTAN"],
        timeline: "⏰ أدوية الصداع النصفي (Triptans): تؤخذ حبة واحدة عند بداية الشعور بالصداع فوراً، مع الراحة في غرفة مظلمة هادئة."
    },
    // Thyroid and Hormones
    {
        drugs: ["ESTROGEN", "PROGESTERONE", "ESTRADIOL", "NORGESTREL", "LEVONORGESTREL", "DROSPIRENONE"],
        timeline: "⏰ حبوب منع الحمل والهرمونات: يجب تثبيت الساعة التي تؤخذ فيها الحبة يومياً (مثلاً 9 مساءً) لضمان الفاعلية القصوى ومنع الحمل."
    },
    {
        drugs: ["CLOMIPHENE", "LETROZOLE", "ANASTROZOLE", "TAMOXIFEN"],
        timeline: "⏰ أدوية الخصوبة والأورام الهرمونية: الالتزام الحرفي بالجرعة والتوقيت اليومي ضروري، مع أو بدون طعام."
    },
    {
        drugs: ["SILDENAFIL", "VARDENAFIL", "TADALAFIL", "AVANAFIL"],
        timeline: "⏰ المنشطات: قبل النشاط بـ 1 ساعة. (سيلدينافيل يتأثر بالوجبات الدسمة ويؤخر المفعول، تادالافيل لا يتأثر)."
    }
];

groups.forEach(group => {
    group.drugs.forEach(drug => {
        timeline[drug] = group.timeline;
    });
});

fs.writeFileSync('c:/Users/HP/testmono/interactions_db/admin_timeline.json', JSON.stringify(timeline, null, 2));
console.log('Successfully generated extremely massive admin_timeline.json with ' + Object.keys(timeline).length + ' distinct active ingredients.');

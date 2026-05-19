import json

data = {
    "METFORMIN": {
        "foodInteraction": "🍊 يؤخذ مع الوجبات لتقليل اضطرابات المعدة. (نقص فيتامين ب12 محتمل ويحتاج مكملات)."
    },
    "GLIMEPIRIDE": {
        "foodInteraction": "🍊 يؤخذ مع أو بدون طعام (يفضل مع الإفطار)."
    },
    "GLICLAZIDE": {
        "foodInteraction": "🍊 يؤخذ مع الإفطار لتقليل خطر هبوط السكر."
    },
    "SITAGLIPTIN": {
        "foodInteraction": "🍊 مع أو بدون طعام. الإكثار من شرب الماء لتقليل التهاب المسالك البولية."
    },
    "LINAGLIPTIN": {
        "foodInteraction": "🍊 مع أو بدون طعام. الإكثار من شرب الماء لتقليل التهاب المسالك البولية."
    },
    "VILDAGLIPTIN": {
        "foodInteraction": "🍊 مع أو بدون طعام. الإكثار من شرب الماء لتقليل التهاب المسالك البولية."
    },
    "EMPAGLIFLOZIN": {
        "foodInteraction": "🍊 مرة واحدة صباحاً، مع أو بدون طعام."
    },
    "DAPAGLIFLOZIN": {
        "foodInteraction": "🍊 مرة واحدة صباحاً، مع أو بدون طعام."
    },
    "REPAGLINIDE": {
        "foodInteraction": "🍊 يؤخذ خلال 30 دقيقة قبل الوجبة. إذا تخطيت الوجبة يجب تخطي الجرعة لمنع هبوط السكر."
    },
    "SEMAGLUTIDE": {
        "foodInteraction": "🍊 الأقراص (Rybelsus): على معدة فارغة قبل أول أكل/شرب بـ 30-60 دقيقة مع 120 مل ماء فقط. الحقن (Ozempic): مع أو بدون طعام."
    },
    "LIRAGLUTIDE": {
        "foodInteraction": "🍊 مع أو بدون طعام."
    },
    "INSULIN ASPART": {
        "foodInteraction": "🍊 سريع المفعول: 5-15 دقيقة قبل الأكل أو حتى 20 دقيقة بعد الأكل."
    },
    "INSULIN LISPRO": {
        "foodInteraction": "🍊 سريع المفعول: 5-15 دقيقة قبل الأكل أو حتى 20 دقيقة بعد الأكل."
    },
    "INSULIN REGULAR": {
        "foodInteraction": "🍊 قصير المفعول: 30 دقيقة قبل الطعام."
    },
    "INSULIN GLARGINE": {
        "foodInteraction": "🍊 طويل المفعول (Lantus/Toujeo): مرة واحدة يومياً، مع أو بدون طعام."
    },
    "INSULIN DEGLUDEC": {
        "foodInteraction": "🍊 طويل المفعول (Tresiba): مع أو بدون طعام."
    },
    "ORLISTAT": {
        "foodInteraction": "🍊 خلال أو حتى ساعة بعد وجبة تحتوي على دهون. افصله عن الفيتامينات الذائبة في الدهون بساعتين."
    },
    "HYDROCHLOROTHIAZIDE": {
        "foodInteraction": "🍊 صباحاً. استهلك أطعمة غنية بالبوتاسيوم (موز/برتقال). قلل من الصوديوم لتحسين التحكم بالضغط."
    },
    "FUROSEMIDE": {
        "foodInteraction": "🍊 مع الطعام لتقليل اضطراب المعدة. يحتاج لتعويض البوتاسيوم في الغذاء وتقليل الصوديوم."
    },
    "SPIRONOLACTONE": {
        "foodInteraction": "🍊 مع الطعام. ⚠️ تجنب الأطعمة الغنية جداً بالبوتاسيوم (موز، سبانخ، طماطم) لتفادي الارتفاع الحاد، وتجنب الجريب فروت."
    },
    "LISINOPRIL": {
        "foodInteraction": "🍊 مع أو بدون طعام. ⚠️ تجنب الإكثار من الأطعمة الغنية بالبوتاسيوم."
    },
    "ENALAPRIL": {
        "foodInteraction": "🍊 مع أو بدون طعام. ⚠️ تجنب الإكثار من الأطعمة الغنية بالبوتاسيوم."
    },
    "CAPTOPRIL": {
        "foodInteraction": "🍊 قبل الأكل بساعة أو بعده بساعتين (الطعام يقلل امتصاصه). قد يسبب نقص الزنك ويغير التذوق."
    },
    "LOSARTAN": {
        "foodInteraction": "🍊 مع أو بدون طعام. ⚠️ تجنب الإكثار من الأطعمة الغنية بالبوتاسيوم."
    },
    "METOPROLOL": {
        "foodInteraction": "🍊 يجب تناوله مع الطعام أو مباشرة بعد الوجبات. تجنب الكافيين الكثير."
    },
    "CARVEDILOL": {
        "foodInteraction": "🍊 يجب تناوله مع الطعام أو مباشرة بعد الوجبات لتقليل الدوخة. تجنب الكافيين الكثير."
    },
    "PROPRANOLOL": {
        "foodInteraction": "🍊 الوجبات الغنية بالدهون تزيد امتصاصه. تجنب الكافيين الكثير."
    },
    "AMLODIPINE": {
        "foodInteraction": "🍊 مع أو بدون طعام."
    },
    "VERAPAMIL": {
        "foodInteraction": "🍊 خذه مع الطعام. (Isoptin SR يؤخذ مع الطعام). الأطعمة الغنية بالمغنيسيوم تدعم مفعوله. ⚠️ يمنع الجريب فروت."
    },
    "NIFEDIPINE": {
        "foodInteraction": "🍊 مع أو بدون طعام. ⚠️ الجريب فروت يزيد تركيزه وأعراضه الجانبية."
    },
    "ATORVASTATIN": {
        "foodInteraction": "🍊 يمكن أخذه بأي وقت (يفضل مساءً). ⚠️ يمنع الجريب فروت."
    },
    "SIMVASTATIN": {
        "foodInteraction": "🍊 مساءً. ⚠️ يمنع الجريب فروت نهائياً."
    },
    "ROSUVASTATIN": {
        "foodInteraction": "🍊 يمكن أخذه بأي وقت مع أو بدون طعام."
    },
    "PRAVASTATIN": {
        "foodInteraction": "🍊 يعمل بشكل أفضل على معدة فارغة."
    },
    "ASPIRIN": {
        "foodInteraction": "🍊 مع كوب ماء لتقليل اضطراب المعدة. تجنب الكاري/العرقسوس بكميات كبيرة لاحتوائها على ساليسيلات."
    },
    "CLOPIDOGREL": {
        "foodInteraction": "🍊 مع أو بدون طعام. ⚠️ يمنع الجريب فروت (يقلل من مفعول الدواء وتجلط الدم)."
    },
    "RIVAROXABAN": {
        "foodInteraction": "🍊 الجرعات 15 ملغ و 20 ملغ يجب أخذها مع الطعام (يفضل العشاء). الجرعات الصغيرة 10 ملغ مع أو بدون طعام."
    },
    "WARFARIN": {
        "foodInteraction": "🍊 ⚠️ حافظ على كمية ثابتة يومياً من فيتامين K (خضروات ورقية خضراء). تجنب عصير الجريب فروت والتوت البري."
    },
    "ALLOPURINOL": {
        "foodInteraction": "🍊 بعد الأكل مع شرب كميات كبيرة من السوائل (لإخراج لترين بول يومياً وتقليل تهيج المعدة)."
    },
    "ALENDRONATE": {
        "foodInteraction": "🍊 على الريق تماماً قبل الأكل بـ 30 دقيقة مع ماء عادي فقط. الأكل، القهوة، والعصائر تمنع امتصاصه."
    },
    "TERIPARATIDE": {
        "foodInteraction": "🍊 مع أو بدون طعام في أي وقت."
    },
    "METHIMAZOLE": {
        "foodInteraction": "🍊 مع أو بدون طعام. تجنب الأطعمة الغنية باليود (الأعشاب البحرية، الملح باليود، الأسماك البحرية)."
    },
    "LEVOTHYROXINE": {
        "foodInteraction": "🍊 ⚠️ على الريق قبل الفطور بـ 30-60 دقيقة. افصله بـ 4 ساعات عن: الحليب/الكالسيوم، الحديد، الألياف العالية، والصويا."
    },
    "TOLTERODINE": {
        "foodInteraction": "🍊 بعد الطعام لزيادة امتصاصه 53%. ⚠️ تجنب الجريب فروت."
    },
    "SOLIFENACIN": {
        "foodInteraction": "🍊 مع أو بدون طعام. ⚠️ تجنب الجريب فروت."
    },
    "TROSPIUM": {
        "foodInteraction": "🍊 على معدة فارغة (ساعة قبل الأكل). الوجبة الدهنية تقلل امتصاصه. تجنب الكحول."
    },
    "SILDENAFIL": {
        "foodInteraction": "🍊 الوجبات عالية الدهون تؤخر الامتصاص. ⚠️ الجريب فروت يزيد الأعراض الجانبية."
    },
    "TADALAFIL": {
        "foodInteraction": "🍊 لا يتأثر بالطعام. ⚠️ الجريب فروت يزيد الأعراض الجانبية."
    },
    "VARDENAFIL": {
        "foodInteraction": "🍊 الوجبات عالية الدهون تقلل الامتصاص وتؤخره. ⚠️ الجريب فروت ممنوع."
    },
    "DAPOXETINE": {
        "foodInteraction": "🍊 1-3 ساعات قبل العلاقة. ⚠️ تجنب الجريب فروت."
    },
    "QUETIAPINE": {
        "foodInteraction": "🍊 العادي: مع أو بدون طعام. الممتد المفعول (XR): بدون طعام أو مع وجبة خفيفة مساءً."
    },
    "ARIPIPRAZOLE": {
        "foodInteraction": "🍊 مع أو بدون طعام."
    },
    "LURASIDONE": {
        "foodInteraction": "🍊 يجب أن يؤخذ مع وجبة تحتوي على 350 سعرة حرارية على الأقل لزيادة الامتصاص بمقدار 3 أضعاف. ⚠️ تجنب الجريب فروت."
    },
    "PHENYTOIN": {
        "foodInteraction": "🍊 يقلل امتصاص حمض الفوليك، وفيتامين B و D والكالسيوم. تحتاج لتعويض غذائي."
    },
    "CARBAMAZEPINE": {
        "foodInteraction": "🍊 مع الأكل. ⚠️ الجريب فروت يزيد تركيزه السام."
    },
    "TOPIRAMATE": {
        "foodInteraction": "🍊 نظام كيتو الغذائي قد يزيد خطر حصوات الكلى أو الحموضة."
    },
    "RACECADOTRIL": {
        "foodInteraction": "🍊 يفضل قبل الوجبات."
    },
    "DIOSMECTITE": {
        "foodInteraction": "🍊 بين الوجبات. افصله بساعتين عن الأدوية الأخرى والطعام ليمنع امتصاصها."
    },
    "BISACODYL": {
        "foodInteraction": "🍊 مع الماء. لا تأخذه خلال ساعة من تناول مضادات الحموضة أو الحليب."
    },
    "SENNA": {
        "foodInteraction": "🍊 على معدة فارغة لأفضل امتصاص. افصله بساعتين عن الأكل والأدوية."
    },
    "PSYLLIUM": {
        "foodInteraction": "🍊 مع الأكل (يفضل الزبادي) ومعه ربع لتر ماء على الأقل."
    },
    "MACROGOL": {
        "foodInteraction": "🍊 على معدة فارغة. تجنب الطعام الصلب وقت التحضير (قبل المنظار)."
    },
    "OMEPRAZOLE": {
        "foodInteraction": "🍊 على معدة فارغة. (الاستخدام الطويل يقلل امتصاص B12، الكالسيوم، والمغنيسيوم)."
    },
    "ESOMEPRAZOLE": {
        "foodInteraction": "🍊 على معدة فارغة. ⚠️ تجنب عصير الجريب فروت (الباودر يمكن خلطه بعصير التفاح)."
    },
    "DEXLANSOPRAZOLE": {
        "foodInteraction": "🍊 مع أو بدون طعام. يمكن رش الحبيبات على زبادي أو تفاح مهروس."
    },
    "MESALAMINE": {
        "foodInteraction": "🍊 مع الوجبات. حافظ على شرب ماء كافٍ لتجنب حصوات الكلى."
    },
    "MEBEVERINE": {
        "foodInteraction": "🍊 قبل الوجبات بـ 20 دقيقة. (القرص لا يمضغ)."
    },
    "FEXOFENADINE": {
        "foodInteraction": "🍊 ⚠️ الوجبات الغنية بالدهون أو عصائر الفاكهة (تفاح، برتقال، جريب فروت) تقلل امتصاصه بـ 50%. افصله عنها بـ 4 ساعات."
    },
    "BILASTINE": {
        "foodInteraction": "🍊 ساعة قبل الأكل أو ساعتين بعد الأكل/العصير."
    },
    "RUPATADINE": {
        "foodInteraction": "🍊 ⚠️ تجنب عصير الجريب فروت (يرفع التركيز 3.5 أضعاف)."
    },
    "MONTELUKAST": {
        "foodInteraction": "🍊 مع أو بدون أكل. الأكياس تخلط مع تفاح مهروس/زبادي/آيس كريم (بدرجة حرارة الغرفة)."
    },
    "BUDESONIDE": {
        "foodInteraction": "🍊 الكبسولات (للمعدة): قبل الأكل بساعة. ⚠️ الجريب فروت يضاعف تركيزه. البخاخ: مضمضة لغسل الفم."
    },
    "PREDNISOLONE": {
        "foodInteraction": "🍊 بعد الأكل أو مع الحليب لحماية المعدة. ينصح بزيادة البوتاسيوم/الكالسيوم في الغذاء وتقليل الملح."
    },
    "DEXAMETHASONE": {
        "foodInteraction": "🍊 بعد الأكل لحماية المعدة. ينصح بزيادة البوتاسيوم/الكالسيوم وتقليل الملح."
    },
    "AMOXICILLIN+CLAVULANATE": {
        "foodInteraction": "🍊 مع الأكل لزيادة الامتصاص ومنع اضطراب المعدة."
    },
    "CEFUROXIME": {
        "foodInteraction": "🍊 مع الأكل لزيادة الامتصاص."
    },
    "SULFAMETHOXAZOLE": {
        "foodInteraction": "🍊 مع الأكل لتحسين الامتصاص وتقليل اضطراب المعدة."
    },
    "NITROFURANTOIN": {
        "foodInteraction": "🍊 مع الأكل لتحسين الامتصاص وتقليل اضطراب المعدة."
    },
    "CIPROFLOXACIN": {
        "foodInteraction": "🍊 ⚠️ يمنع مع منتجات الألبان (الكالسيوم/الحديد/الزنك يمنع الامتصاص). عصير البرتقال يقلل الامتصاص. الكافيين يتضاعف تأثيره."
    },
    "LEVOFLOXACIN": {
        "foodInteraction": "🍊 ⚠️ يمنع مع منتجات الألبان (الكالسيوم/الحديد/الزنك يمنع الامتصاص)."
    },
    "DOXYCYCLINE": {
        "foodInteraction": "🍊 افصله بـ ساعتين عن منتجات الألبان، مدعمات الكالسيوم والحديد."
    },
    "AZITHROMYCIN": {
        "foodInteraction": "🍊 الكبسولات والدواء الشرب: يفضل ساعة قبل الأكل أو ساعتين بعده. الأقراص: مع أو بدون طعام."
    },
    "CEFDINIR": {
        "foodInteraction": "🍊 افصله عن الحديد ومضادات الحموضة بـ ساعتين."
    },
    "MINOCYCLINE": {
        "foodInteraction": "🍊 مع أو بدون طعام. خذه مع ماء كافي، افصله عن الحديد."
    },
    "METRONIDAZOLE": {
        "foodInteraction": "🍊 مع الأكل لتجنب اضطراب المعدة."
    },
    "FLUCONAZOLE": {
        "foodInteraction": "🍊 مع أو بدون طعام."
    },
    "ITRACONAZOLE": {
        "foodInteraction": "🍊 ⚠️ الأقراص: بعد وجبة كاملة دسمة لضمان الامتصاص. حافظ على تناول أو ترك الجريب فروت بانتظام."
    },
    "IRON": {
        "foodInteraction": "🍊 ⚠️ الشاي، القهوة، البيض، الحليب (الكالسيوم)، الحبوب الكاملة تمنع الامتصاص. الأفضل أخذه مع عصير برتقال (فيتامين C)."
    },
    "CALCIUM": {
        "foodInteraction": "🍊 ⚠️ الكربونات: بعد وجبة دسمة أو أكبر وجبة باليوم. الأطعمة الغنية بالأوكسايلات تقلل امتصاصه."
    },
    "VITAMIN D3": {
        "foodInteraction": "🍊 يؤخذ مع وجبة دهنية لضمان الامتصاص الجيد."
    }
}

with open(r'c:\Users\HP\testmono\interactions_db\drug_food.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully written drug_food.json with all PDF data!")

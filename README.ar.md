<div dir="rtl">

# المشروع الختامي: اطلق أداة حقيقية باختبارات وCI وDocker


> **ملخص درسي قصير عن قصد.** الدرس في التطبيق بيعرض خطوات ضغط مختصرة. الـ README ده بيحفظ الأوامر الكاملة وإصلاح الأخطاء والخلفية لكل مرحلة — افتح قسم **المرحلة N** لما تحتاج تفاصيل.

ابنِ أداة درجات وغياب معلّم يقدر يستخدمها: Python بالاختبار أولًا، وCLI بـ Typer وتقرير HTML بلغتين، وGitHub Actions بحد تغطية، وصورة Docker، وإصدار موسوم.

[English](README.md)

## هتقدر تعمل إيه

- تشغّل أدوات حقيقية مجانية من اللابتوب أو Codespaces
- تخلّص خمس مراحل، كل مرحلة ليها فحص تقدر تتأكد منه بنفسك
- تطلع بقطعة بورتفوليو: تقرير أو عرض أو أداة بإصدار v1.0
- **درسي مش بيشغّل كودك أبدًا** — بيقرا الرابط وملف الفحص وبمراجعة استشارية

## ثبّت مرة واحدة

### ويندوز

١. ثبّت Python 3.12: افتح PowerShell واكتب winget install Python.Python.3.12
٢. ثبّت Git: winget install Git.Git
٣. ثبّت VS Code من https://code.visualstudio.com مجانًا
٤. على GitHub افتح https://github.com/darsi-org/code-capstone واضغط Use this template، وبعدين Clone نسختك
٥. جوّه فولدر المشروع شغّل:
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python check.py

### ماك

١. ثبّت Homebrew من https://brew.sh لو مش متثبت
٢. brew install python@3.12 git
٣. ثبّت VS Code من https://code.visualstudio.com
٤. على GitHub افتح https://github.com/darsi-org/code-capstone → Use this template → Clone نسختك
٥. جوّه فولدر المشروع شغّل:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py

### Codespaces / Colab

معندكش كمبيوتر؟ استخدم GitHub Codespaces: افتح نسختك → Code → Codespaces → Create codespace. كل حاجة هتتثبت هناك. أو افتح دفتر في Google Colab، شغّل أول خلية بتنسخ الريبو، وبعدين python check.py. الاتنين بيشتغلوا من لابتوب مستعار؛ ومتصفح الموبايل يكفي تقرا النتائج.

## البداية

اضغط **Use this template** على https://github.com/darsi-org/code-capstone، Clone نسختك، وبعدين اتبع المرحلة ١.

## المراحل

### m1: خطّط كفريق (2 ساعات)

## ليه ده مهم
البرمجيات الحقيقية بتبدأ بمين معمولة له وإيه مش هتعمله أبدًا — خصوصًا مع بيانات التلاميذ.

## الأدوات للمرحلة دي
- **GitHub Issues / docs/STORIES.md** — ست قصص مستخدم. هتجيبه من: free on GitHub
- **sample.csv** — ٣٠ تلميذ مختلق. هتجيبه من: scripts/make_sample.py

## اعمل كده
1. Clone https://github.com/darsi-org/code-capstone، جهّز venv، شغّل: python scripts/make_sample.py
2. اكتب ست قصص مستخدم في docs/STORIES.md وكمان Issues: مين، إيه، ليه.
3. README: بتعمل إيه، تتشغّل إزاي في ≤٣ أوامر، وإيه مش هتعمله أبدًا (مفيش درجات حقيقية تخرج من جهاز المعلّم).
4. شغّل python check.py --milestone m1.

## هتبقى خلصت لما
- sample.csv موجود
- STORIES.md فيه ٦ قصص
- m1 ناجحة

## لو حاجة وقفت
- **القصص مجرد أسماء ميزات** → عيد الكتابة: بصفتي معلّم، عايز… عشان…
- **أسماء تلاميذ حقيقية في العينة** → عيد التوليد بـ make_sample.py؛ متلصقوش قوايم فصول

## إيه اللي لازم تفهمه
تقدر تخطّط لأداة بقصص وحدود خصوصية قاسية قبل ما تكتب كود.

**المطلوب تسليمه:** ست قصص، وREADME، وsample.csv، وdarsi-check.json بيجتاز m1.

### m2: اللب، الاختبارات أولًا (4 ساعات)

## ليه ده مهم
اكتب الاختبار، شوفه يفشل، وبعدين خلّيه ينجح. الحالات الحدّية هي فين الأخطاء بتتخبّى.

## الأدوات للمرحلة دي
- **pytest + pytest-cov** — اختبارات وتغطية. هتجيبه من: in requirements.txt
- **ruff** — فاحص أسلوب سريع. هتجيبه من: in requirements.txt

## اعمل كده
1. في marks/core.py نفّذ load وaverages وat_risk وclean_id — بس اكتب اختبارات بتفشل في tests/test_core.py الأول.
2. غطّي الحواف: معرّف فاضي، مكرر، درجة ١٠٥، أسماء عربي، ملف فاضي.
3. شغّل: pytest --cov=marks --cov-fail-under=80 && ruff check . && python check.py --milestone m2

## هتبقى خلصت لما
- ≥٨ اختبارات أساسية
- تغطية ≥٨٠٪
- m2 ناجحة

## لو حاجة وقفت
- **التغطية تحت ٨٠** → زوّد اختبارات لفروع except والمدخل الفاضي
- **درجة ١٠٥ بتكسر** → بلّغ عن الصف الغلط؛ استبعده من المتوسطات

## إيه اللي لازم تفهمه
تقدر تنمّي منطق اللب بالاختبار أولًا وترفض بيانات غلط صامتة.

**المطلوب تسليمه:** marks/core.py، والاختبارات، وتقرير التغطية، وdarsi-check.json بيجتاز m2.

### m3: سطر أوامر وتقرير بلغتين (4 ساعات)

## ليه ده مهم
أداة محدش غيرك يقدر يشغّلها مش مكتملة. تقارير عربي RTL محتاجة اتجاه وعزل.

## الأدوات للمرحلة دي
- **Typer** — بيبني CLI فيه --help. هتجيبه من: in requirements.txt
- **CliRunner** — بيختبر الـ CLI. هتجيبه من: from typer.testing

## اعمل كده
1. في marks/cli.py زوّد: marks summary وmarks report --lang ar.
2. تقرير HTML: متوسطات، ومعرّضون للخطر، dir=rtl للعربي، و<bdi> للقطع المختلطة.
3. احفظ examples/report-en.html وexamples/report-ar.html. اختبر بـ CliRunner. شغّل pytest && python check.py --milestone m3.

## هتبقى خلصت لما
- CLI بـ Typer موجود
- تقريرين نموذجيين
- m3 ناجحة

## لو حاجة وقفت
- **أسماء عربي مقلوبة جنب الأرقام** → اضبط dir=rtl وغلّف القطع المختلطة في <bdi>
- **أمر marks مش موجود** → pip install -e . عشان نقطة الدخول تتثبت

## إيه اللي لازم تفهمه
تقدر تطلق CLI وتقرير واعي بـ RTL معلّم يقدر يفتحه.

**المطلوب تسليمه:** marks/cli.py، وتقارير نموذجية، واختبارات CLI، وdarsi-check.json بيجتاز m3.

### m4: تكامل مستمر على GitHub Actions (2 ساعات)

## ليه ده مهم
روبوت بيفحص كل رفع بيحافظ على شبكة الأمان متترقاش.

## الأدوات للمرحلة دي
- **GitHub Actions** — بيشغّل ruff وpytest بحد تغطية. هتجيبه من: free for public repos

## اعمل كده
1. عدّل ci.yml: على push/PR ثبّت، ruff، pytest بحد تغطية ٨٠.
2. ارفع تغيير بيكسر اختبار عمدًا، شوف الأحمر، صلّح للأخضر. زوّد شارة CI في README.
3. شغّل python check.py --milestone m4.

## هتبقى خلصت لما
- ci.yml فيه cov-fail-under وruff
- m4 ناجحة

## لو حاجة وقفت
- **Actions مش شغال** → Settings → Actions → allow؛ ارفع على الفرع الافتراضي
- **تغطية متقلبة** → ثبّت البذرة ومتعتمدش على ترتيب dict

## إيه اللي لازم تفهمه
تقدر تخلي كل رفع يثبت إن الفحص والاختبارات لسه ناجحين.

**المطلوب تسليمه:** ci.yml، وروابط أحمر ثم أخضر، والشارة، وdarsi-check.json بيجتاز m4.

### m5: Docker والإصدار v1.0 (3 ساعات)

## ليه ده مهم
Docker بيخلّص جملة «شغّال على جهازي». سجل التغييرات بيخلّي الناس تعرف v1.0 يعني إيه.

## الأدوات للمرحلة دي
- **Docker** — صورة python:3.12-slim بتشغّل marks. هتجيبه من: Dockerfile in the starter

## اعمل كده
1. كمّل Dockerfile. اختبر: docker build وdocker run مع volume.
2. زوّد مهمة CI بتبني الصورة. اكتب CHANGELOG.md. اقفل القصص الخلصانة. حط v1.0.
3. شغّل python check.py --milestone m5. اشرح على درسي.

## هتبقى خلصت لما
- Dockerfile فيه ENTRYPOINT
- CHANGELOG.md موجود
- m5 ناجحة

## لو حاجة وقفت
- **أخطاء صلاحيات Docker على Windows** → شارك الدرايف في إعدادات Desktop؛ استخدم المسار بحذر في PowerShell
- **الصورة ناقصة بيانات العينة** → اربط volume؛ متخبزش بيانات حقيقية جوّه الصورة

## إيه اللي لازم تفهمه
تقدر تعلّب أداة عشان أي حد يشغّل نفس الأمر ويشير لنسخة.

**المطلوب تسليمه:** Dockerfile، وبناء صورة أخضر، وCHANGELOG.md، وv1.0، وdarsi-check.json بيجتاز m5، وشرحك.

## الفحص

شغّل `python check.py` أو `python check.py --milestone m2`. بيقرا الملفات بس، بيكتب `darsi-check.json`، وبيطبّع بالإنجليزي والعربي. مش بيرفع حاجة.

## المراجعة على درسي

ابعت رابط الريبو و`darsi-check.json` مع كل مرحلة على درسي. درسي بيقرا آخر تشغيل Actions والإصدار من واجهة GitHub العامة، بيضيف مراجعة استشارية بالذكاء الاصطناعي، وبعدين معلّمك أو فريق درسي بيراجع. **درسي مش بيشغّل كودك.**

## الترخيص

MIT — شوف [LICENSE](LICENSE).

</div>

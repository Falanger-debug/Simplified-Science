from flask import Flask, render_template, request, jsonify

import appAPI

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        link = request.form.get('link')  # Użyj get() dla bezpieczeństwa
        knowledge = request.form.get('poziom-wiedzy')
        title = "Profilowanie transkrypcyjne wątroby myszy biorących udział w misji Rodent Research Reference Mission-1 (RRRM-1)"
        test_object = "Obiektem badań w eksperymencie Rodent Research Reference Mission (RRRM-1) były myszy, w tym 40 samic BALB/cAnNTac w dwóch grupach wiekowych: 20 młodych myszy w wieku 10-12 tygodni oraz 20 starszych myszy w wieku 32 tygodni."
        experiment_goal = "Celem eksperymentu Rodent Research Reference Mission (RRRM-1) było zbadanie wpływu lotu kosmicznego na organizmy myszy, w szczególności w odniesieniu do różnic wynikających z wieku. W tym celu porównywano efekty lotu kosmicznego u młodych (10-12 tygodni) i starszych (32 tygodnie) myszy."
        #experiment_group_kind = "Sztywny rodzaj grupy eksperymentalnej"
        experiment_environment = """Eksperyment Rodent Research Reference Mission (RRRM-1) został przeprowadzony w starannie kontrolowanym środowisku w kilku etapach zarówno na Ziemi, jak i na pokładzie Międzynarodowej Stacji Kosmicznej (ISS). Oto szczegóły dotyczące otoczenia i narzędzi użytych w trakcie eksperymentu: Przygotowanie myszy na Ziemi: Myszy (BALB/cAnNTac) pochodziły z Taconic Biosciences (Germantown, NY) i zostały przetransportowane do NASA Kennedy Space Center (KSC) na około 4 tygodnie przed startem. Były one oznakowane za pomocą chipów RFID (IMI-500). Myszom zapewniono standardowe warunki w obiekcie opieki nad zwierzętami (Animal Care Facility, ACF) w NASA KSC. Były trzymane w cyklu świetlnym 12:12 (12 godzin światła, 12 godzin ciemności), co było zsynchronizowane z cyklem świetlnym używanym w Transporterach i Habitatów na czas lotu kosmicznego. Zwierzęta były umieszczone w klatkach (5 myszy na klatkę) i początkowo karmione standardową karmą laboratoryjną i wodą, która była zmieniana dwa razy w tygodniu. Miały również standardowe wzbogacenie środowiskowe w postaci igloo w klatkach. Na trzy tygodnie przed startem, myszy przeniesiono na podłogę z siatki, aby symulować warunki panujące w Transporterach i Habitatów kosmicznych.
        Warunki kosmiczne i kontrolne: Myszy kosmiczne oraz kontrolne na Ziemi były trzymane w specjalnych Transporterach i Habitatach zaprojektowanych na potrzeby lotu kosmicznego. Myszy były karmione specjalnym jedzeniem NASA Nutrient-Upgraded Rodent Foodbars (NuRFB) i dostarczano im wodę przez systemy lixit, identyczne do tych używanych w warunkach lotu kosmicznego. W trakcie lotu i w warunkach kontrolnych na Ziemi, klatki z myszami były wymieniane na nowe jedzenie raz w tygodniu. Myszy kontrolne na Ziemi były trzymane w dwóch grupach: Habitat Ground Control (HGC) i Vivarium Ground Control (VGC). Grupy te miały różne warunki bytowania, jednak starano się odwzorować warunki kosmiczne, jak najdokładniej w grupie HGC.
        Mold contamination i problemy techniczne: Zarówno myszy kosmiczne, jak i Habitat Ground Control miały problem z zanieczyszczeniem jedzenia pleśnią, co mogło wywołać dodatkowy stres u zwierząt. Karmy w niektórych klatkach HGC odpadły i spadły na dno, co było stresujące dla zwierząt, ale nie uniemożliwiło im dostępu do pożywienia.
        Zabiegi na myszach po powrocie: Myszom, które wróciły żywe na Ziemię, usunięto wątroby, które następnie poddano analizie RNA-seq. Tkanki były przechowywane w ciekłym azocie, a RNA i DNA ekstrahowano i analizowano przy użyciu zestawów AllPrep DNA/RNA Mini Kit (Qiagen)."""
        experiment_method = """
Eksperyment Rodent Research Reference Mission (RRRM-1) został przeprowadzony w kilku etapach, zarówno na Ziemi, jak i na pokładzie Międzynarodowej Stacji Kosmicznej (ISS). Proces obejmował następujące kluczowe kroki:

1. **Przygotowanie myszy przed lotem:**
   Myszom (BALB/cAnNTac) zapewniono warunki w NASA Kennedy Space Center (KSC) w obiekcie opieki nad zwierzętami (Animal Care Facility). Myszy były oznakowane chipami RFID i stopniowo przyzwyczajane do warunków, które naśladowały warunki panujące w Transporterach i Habitatów kosmicznych, w tym karmienie specjalnym jedzeniem NASA Nutrient-Upgraded Rodent Foodbars (NuRFB) i wodą dostarczaną przez systemy lixit.

2. **Przeprowadzenie eksperymentu na ISS:**
   Część myszy została umieszczona na pokładzie ISS, gdzie były narażone na warunki mikrograwitacji przez 22-23 dni (grupa ISS Terminal, ISS-T) lub 40 dni (grupa Live Animal Return, LAR). Po 22-23 dniach niektóre myszy zostały uśmiercone na orbicie w celu zbadania efektów lotu kosmicznego bezpośrednio po jego zakończeniu. Inne myszy wróciły na Ziemię po 40 dniach lotu i przeszły 2-dniowy okres regeneracji, po czym również zostały uśmiercone.

3. **Grupy kontrolne:**
   Eksperyment obejmował także grupy kontrolne: Habitat Ground Control (HGC), Vivarium Ground Control (VGC) i Baseline Control, które znajdowały się na Ziemi w warunkach imitujących lot kosmiczny, z tą różnicą, że nie były narażone na mikrograwitację.

4. **Proces eutanazji i zbieranie próbek:**
   Myszy zostały poddane eutanazji przez pobranie krwi z serca (punkcja serca) i wykonanie podwójnej torakotomii. Wątroby zostały usunięte, zważone, rozdzielone na płaty i natychmiast zamrożone w ciekłym azocie. Tkanki przechowywano w temperaturze -80°C lub niższej podczas transportu i przechowywania.

5. **Analiza molekularna:**
   Z wątrób myszy wyizolowano RNA przy użyciu zestawu AllPrep DNA/RNA Mini Kit (Qiagen). Tkanki homogenizowano w roztworze buforowym (Buffer RLT z dodatkiem beta-merkaptoetanolu) za pomocą systemu Bullet Blender Gold 24 (Next Advance) w temperaturze 4°C. RNA zostało oczyszczone i analizowane pod kątem jakości przy użyciu Qubit 3.0 Fluorometer oraz Agilent 2100 Bioanalyzer. Proces ten umożliwił ocenę zmian molekularnych w tkankach po ekspozycji na warunki kosmiczne.
"""
        object_effect = object_effect = """
W trakcie eksperymentu Rodent Research Reference Mission (RRRM-1) zaobserwowano szereg zmian fizjologicznych i molekularnych u myszy narażonych na warunki lotu kosmicznego. Kluczowe obserwacje obejmowały:

1. **Zmiany w masie ciała i narządów:**
   Myszom regularnie mierzono masę ciała, zarówno w trakcie pobytu na ISS, jak i po powrocie na Ziemię. U niektórych myszy zaobserwowano utratę masy ciała, co mogło być spowodowane stresem wywołanym przez warunki mikrograwitacji, ograniczony dostęp do pożywienia (z powodu pleśni na karmie) oraz różnice w sposobie pobierania pokarmu.

2. **Zmiany w wątrobie:**
   Szczególne zmiany molekularne zidentyfikowano w wątrobie, której tkanki zostały poddane analizie RNA-seq. Wyniki wykazały zmiany w ekspresji genów związanych z metabolizmem lipidów, stresem oksydacyjnym oraz funkcjonowaniem mitochondriów. Te zmiany mogą sugerować zaburzenia w homeostazie metabolicznej spowodowane warunkami mikrograwitacji i innymi czynnikami stresowymi występującymi podczas lotu kosmicznego.

3. **Wpływ stresu środowiskowego:**
   Zmiany środowiskowe, takie jak narażenie na pleśń w pożywieniu oraz problem z unoszeniem się karmy w stanie nieważkości, mogły prowadzić do dodatkowego stresu fizjologicznego u myszy. Obserwowano również różnice w poziomie stresu między myszami powracającymi na Ziemię (grupa Live Animal Return) a tymi, które zostały poddane eutanazji na orbicie (grupa ISS Terminal). Długotrwały stres mógł wpłynąć na układ odpornościowy, jak również na funkcjonowanie narządów wewnętrznych, takich jak wątroba i serce.

4. **Zmiany w adaptacji do mikrograwitacji:**
   Myszom, które spędziły 40 dni na ISS, udało się częściowo zaadaptować do warunków mikrograwitacji, co zaobserwowano w ich zachowaniu oraz funkcjonowaniu układów fizjologicznych. Jednak po powrocie na Ziemię, myszy wymagały 2 dni regeneracji, co sugeruje, że długotrwała ekspozycja na mikrograwitację miała wyraźny wpływ na ich zdolność do adaptacji do warunków grawitacyjnych na Ziemi.

5. **Różnice między grupami wiekowymi:**
   Zaobserwowano pewne różnice w reakcjach na lot kosmiczny między młodszymi (10-12 tygodni) a starszymi (32 tygodnie) myszami. Starsze myszy wykazywały większe zmiany w funkcjonowaniu metabolicznym oraz silniejsze oznaki stresu komórkowego, co sugeruje, że wiek mógł być czynnikiem wpływającym na reakcje fizjologiczne w trakcie lotu kosmicznego.
"""
        experiment_result = """
W eksperymencie Rodent Research Reference Mission (RRRM-1) uzyskano następujące wyniki:

1. **Zmiany masy ciała:**
   U myszy narażonych na warunki mikrograwitacji zaobserwowano zmiany w masie ciała, w tym utratę masy u części myszy zarówno w grupie ISS Terminal (ISS-T), jak i Live Animal Return (LAR).

2. **Zmiany w metabolizmie wątrobowym:**
   Analiza RNA-seq wątroby wykazała zmiany w ekspresji genów związanych z metabolizmem lipidów, stresem oksydacyjnym oraz funkcjonowaniem mitochondriów. Wzorce ekspresji genów różniły się między myszami, które były narażone na mikrograwitację, a myszami z grup kontrolnych.

3. **Problemy ze stresem środowiskowym:**
   Myszom kosmicznym i grupom Habitat Ground Control (HGC) podawano jedzenie, które było częściowo zanieczyszczone pleśnią. Mogło to mieć wpływ na ich zdrowie oraz wyniki fizjologiczne. Dodatkowo, luźne batony żywnościowe (food bars) w warunkach mikrograwitacji mogły powodować stres u myszy, co nie miało miejsca w grupach Vivarium Ground Control (VGC) i Baseline Control.

4. **Zmiany adaptacyjne w mikrograwitacji:**
   U myszy, które spędziły 40 dni na ISS, zaobserwowano zmiany w zachowaniu i funkcjonowaniu fizjologicznym, co może wskazywać na adaptację do warunków mikrograwitacji. Proces regeneracji po powrocie na Ziemię wymagał 2 dni.

5. **Różnice między młodszymi a starszymi myszami:**
   Starsze myszy wykazywały większe zmiany w ekspresji genów i metabolizmie wątroby w porównaniu do młodszych myszy. Obie grupy doświadczyły zmian w reakcji na lot kosmiczny, ale starsze osobniki były bardziej podatne na efekty związane z ekspozycją na mikrograwitację.
"""
        experiment_conclusions = """
Wnioski z eksperymentu Rodent Research Reference Mission (RRRM-1) sugerują, że warunki mikrograwitacji wpływają na organizmy myszy na kilku poziomach fizjologicznych:

1. **Wpływ mikrograwitacji na metabolizm:**
   Zmiany w ekspresji genów związanych z metabolizmem lipidów i funkcjonowaniem mitochondriów w wątrobie myszy wskazują, że warunki lotu kosmicznego mają znaczący wpływ na procesy metaboliczne. Szczególnie stres oksydacyjny i zmiany w funkcjonowaniu energetycznym komórek mogą odgrywać istotną rolę w adaptacji organizmów do warunków kosmicznych.

2. **Stres środowiskowy jako dodatkowy czynnik:**
   Dodatkowe czynniki stresogenne, takie jak zanieczyszczenie jedzenia pleśnią i trudności z pobieraniem pokarmu w stanie nieważkości, mogły nasilić efekty wywołane mikrograwitacją. Te problemy mogły wpływać na zdrowie i dobrostan zwierząt, co może sugerować konieczność lepszego zabezpieczenia żywienia podczas przyszłych misji.

3. **Znaczenie wieku w reakcji na mikrograwitację:**
   Starsze myszy wykazały silniejsze zmiany fizjologiczne, co może oznaczać, że wiek ma wpływ na zdolność adaptacji do warunków kosmicznych. Starsze zwierzęta były bardziej podatne na stres komórkowy i zmiany metaboliczne, co sugeruje, że wiek organizmów należy brać pod uwagę przy planowaniu długoterminowych lotów kosmicznych.

4. **Adaptacja do warunków kosmicznych:**
   Myszy, które spędziły 40 dni w mikrograwitacji, wykazywały zdolność do pewnej adaptacji, ale proces regeneracji po powrocie na Ziemię trwał 2 dni, co może wskazywać na długotrwały wpływ lotu kosmicznego na organizmy. Zdolność do adaptacji do warunków grawitacyjnych po długim czasie w mikrograwitacji wymaga dalszych badań.
"""

        title = appAPI.getTitle(link)
        test_object = appAPI.getTestObject(link)
        experiment_goal = appAPI.getExperimentGoal(link)
        #experiment_group_kind = appAPI.getExperimentGroupKind(link)
        #experiment_goal = appAPI.getExperimentGoal(link)
        #experiment_environment = appAPI.getExperimentEnvironment(link)

        # Zwracamy szablon streszczenie.html, przekazując zmienne
        return render_template('streszczenie.html', link=link, knowledge=knowledge, title=title,
                               test_object=test_object, experiment_goal=experiment_goal,
                               #experiment_group_kind=experiment_group_kind,
                               experiment_environment=experiment_environment,
                               experiment_method=experiment_method,
                               object_effect=object_effect,
                               experiment_result=experiment_result,
                               experiment_conclusions=experiment_conclusions)

    # Przy metodzie GET wyświetlaj index.html
    return render_template('index.html')

@app.route('/streszczenie', methods=['POST'])
def about():
    return render_template('streszczenie.html')

@app.route('/chat_message', methods=['POST'])
def chat_message():
    message = request.form['message']
    response = appAPI.askChat(message)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

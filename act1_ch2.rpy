image bg hotel3_night = "mod_assets/places/hotel3-b.png"
image bg restaurant_c = "mod_assets/places/restaurant_c.png"
image bg sky = "mod_assets/places/sky.png"
image orange = "#ffa500"
label dust:
 show y_cg2_dust1 zorder 100
 show y_cg2_dust2 zorder 101
 show y_cg2_dust3 zorder 103
 show y_cg2_dust4 zorder 104
return

transform bg_zoom:
  zoom 2.45
  yalign 0.15 xalign 0.6
default m_aff = 0
transform face_window(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.304
    yoffset y
    zoom z*2.00
style kt_text_b:
    font "mod_assets/theme/kt.ttf"
    size 36
    color "#000"
    outlines []

style kt_text_jp:
  font "mod_assets/theme/kt_jp.ttf"
  size 25
  color "#000"
  outlines []

image kt_text_b = ParameterizedText(style="kt_text_b", xalign=0.5)
image kt_text_jp = ParameterizedText(style="kt_text_jp", xalign=0.5)

image kt_jp_t1:
  xalign 0.65
  yalign 0.1
  Text("2017年6月23日", style="kt_text_jp")
image kt_homework1:
  xalign 0.4
  yalign 0.18
  Text("x-3 = 3-x", style="kt_text_b")
image kt_homework2:
  xalign 0.4
  yalign 0.31
  Text("  3x + 1 = 3-(2-2x)", style="kt_text_b")
image kt_homework3:
  xalign 0.4
  yalign 0.38
  Text("     3x/2 + 2x/3 = 1+3x/2", style="kt_text_b")
image kt_homework4:
  xalign 0.4
  yalign 0.50
  Text("       2(2+x)-(6-7x)=13x-(1+4x)", style="kt_text_b")
image kt_homework5:
  xalign 0.4
  yalign 0.58
  Text("       5(x-1)-(1-x)=2(x-1)-4(1-x)", style="kt_text_b")
image kt_homework6:
  xalign 0.4
  yalign 0.70
  Text("         1-(3-2(x+1))=3x+2(x-(3+2x))", style="kt_text_b")
label act1_ch2:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    show intro_logo:
        menu_logo_move_b
    show menu_particles_b:
        xpos 640
        ycenter 510
        time 1.920
    show text("{size=100}{color=#6debab}{b}Arco 1, Capitolo 2{/b}{/size}{/color}\n{size=60}La ragazza coi capelli rosa{/size}\n{size=60}e la sua testardaggine.{/size}"):
        yalign 0.8
    with Dissolve(1.0)
    pause 4.0
    scene black
    with dissolve_scene_full

    scene black
    with dissolve_scene_full
    play sound clock
    pause 5.0
    
    scene bg bedroom
    with dissolve_scene_full
    
    "..."
    "Dio mio, sono già le 7:20?"
    pause 2.0
    "Hm, Monika non è nel letto."
    mc "Monika?"
    "Nessuna risposta. Decido di scendere."
    scene bg mc_lr
    with wipedown
    mc "Monika?"
    "..."
    "Dov'è Monika?"
    play sound steps_st
    "Proprio nel mezzo del mio pensiero, sento Monika venire giù dalle scale."
    "Ed eccola lì, con la sua uniforme addosso."
    play music tmonika_b fadein 4.0
    show monika 1a at t11 zorder 1
    mc "Hey Monika! Buongiorno."
    show monika 1b at t11 zorder 1
    m "Buongiorno [player]~"
    m "Dormito bene?"
    show monika 1a at t11 zorder 1
    mc "Abbastanza dai. Tu?"
    show monika 2k at t11 zorder 1
    m "Io ho dormito {i}molto{/i} bene. Ahaha!~"
    mc "Perchè?"
    show monika 5a at t11 zorder 1
    m "Te l'ho detto ieri. {w=0.5}Sono felice perchè hai dormito affianco a me~"
    show monika 2a at t11 zorder 1
    mc "O-oh... {w=0.5}Capisco."
    show monika 3b at t11 zorder 1
    m "Quindi, {w=0.5}vai a metterti la tua uniforme, {w=0.5} io farò la colazione."
    show monika 3a at t11 zorder 1
    mc "S-{w=0.5}sei sicura? {w=0.5}Non hai bisogno di un aiutino?"
    show monika 5a at t11 zorder 1
    m "No, è tutto a posto~ E poi, {w=0.5} faremmo tardi a scuola, {w=0.5} e dobbiamo presentare Kotonoha al preside."
    show monika 3k at t11 zorder 1
    m "Non ti ricordi?"
    show monika 3a at t11 zorder 1
    mc "Oh, già. {w=0.5}Comunque, Kotonoha saprà dove si trova la nostra scuola?"
    show monika 4b at t11 zorder 1
    m "Kotonoha è anche migliore di me ad utilizzare la console, ma possiamo andare a \"casa\" sua e portarla con noi, se vuoi."
    show monika 4a at t11 zorder 1
    mc "Mi piace questo piano. {w=0.5}Dunque, {w=0.5}ritorno in camera mia."
    show monika 5a at t11 zorder 1
    m "Non metterci troppo~"
    show monika 1a at t11 zorder 1
    mc "Sì. {w=0.5}Torno presto."
    "Detto questo, {w=0.5}mi dirigo in camera mia."
    scene black
    with wipeleft
    scene bedroom
    with wipeleft
    mc "Hm..."
    "Ho più uniformi puliti che vestiti puliti."
    "Perchè ho una selezione di vestiti così noiosa?"
    stop music fadeout 2.0
    "No [player], non pensare niente di stupido. Oggi sarà una lunga giornata."
    "Dio... {w=0.5}Sono preouccpato per come reagirà Natsuki quando vedrà Monika di nuovo. {w=0.5}Non aiuto di certo ma sono tormentato dall'ansia."
    play sound rphone
    "All'improvviso, {w=0.5}il telefono inizia a squillare."
    "Hm, {w=0.5}chi può essere che mi chiama così presto di mattina?"
    mc "Pronto?"
    $ kt_name = "???"
    kt "{i}Hey, [player].{/i}"
    mc "Uh, {w=0.5}Kotonoha?"
    play music tkotonoha_b fadein 3.0
    $ kt_name = "Kotonoha"
    kt "{i}Sì, sono io.{/i}"
    mc "Ciao, come va lì?"
    kt "{i}Beh, mi sono appena alzata.{/i}"
    kt "{i}Monika mi ha riferito che avete dormito insieme.{/i}"
    mc "Uh... {w=0.5}Non proccuparti di questo, devo farti una domanda."
    kt "{i}Sì?{/i}"
    mc "Come hai avuto il mio numero di telefono?"
    kt "{i}E' divertente il fatto che me lo stai chiedendo. {w=0.5}Ho usato la console per prenderlo.{/i}"
    mc "..."
    mc "Potevi chiedermelo ieri."
    kt "{i}Già, {w=0.5}ma mi sono dimenticata.{/i}"
    mc "Comunque, {w=0.5}allora, {w=0.5}qual è il problema?"
    kt "{i}Oh, {w=0.5}già, {w=0.5}mi stavo chiedendo se avreste potuto accompagnarmi a scuola. {w=0.5}Io non so dove sia.{/i}"
    mc "Era proprio ciò di cui stavamo parlando prima io e Monika. {w=0.5}Lei pensava che sapessi già come arrivarci, {w=0.5}dato che sei più brava di lei ad usare la console."
    kt "{i}Posso teletrasportarmi direttamente là, {w=0.5}ma ho deciso che non userò la console se non in situazioni di seria emergenza.{/i}"
    kt "{i}Mi sembra come se stessi barando.{/i}"
    mc "Va bene... {w=0.5}A me piacerebbe saper usare la console come te e Monika."
    kt "{i}Ti insegneremo  più tardi. {w=0.5}Prima dobbiamo sistemare tutta questa faccenda.{/i}"
    kt "{i}Dobbiamo parlare con Natsuki prima di iniziare ad agire.{/i}"
    mc "Già, {w=0.5}non potrei essere più d'accordo."
    kt "{i}Quindi, {w=0.5}come sta andando?{/i}"
    mc "Riguardo a cosa?"
    "Questo potrebbe prenderle un pò più di tempo, quindi, nel mentre che aspetto la sua risposta, mi vesto."
    "Sembra essere più serena di ieri. Non voglio litigare nuovamente con lei, quindi faccio attenzione a cosa le dico, e a come glielo dico."
    kt "{i}Riguardo alla tua \"relazione\" con lei.{/i}"
    mc "Andiamo, {w=0.5}non le ho ancora chiesto di essere la mia ragazza. {w=0.5}Ma se vuole essere chiamata \"la mia ragazza\", {w=0.5}non m'importa per niente."
    kt "{i}Uhuhu~{/i}"
    mc "Perchè stai ridendo in quel modo?"
    kt "{i}Non lo so.{/i}"
    mc "Hm."
    "Appena finito di mettermi l'uniforme, {w=0.5}sento Monika chiamarmi. {w=0.5}Il suo tempismo non potrebbe essere più perfetto."
    m "{b}[player], {w=0.5}la colazione è pronta!~ {w=0.5}Vieni giù!{/b}"
    mc "{b}Sì! {w=0.5}Solo un minuto, {w=0.5}sto parlando con Kotonoha!{/b}"
    kt "{i}Huh? {w=0.5}Monika ha preparato la colazione per tutti e due? {w=0.5}Sembrate proprio una coppietta sposata e felice.{/i}"
    mc "Sì, {w=0.5}forse."
    m "{b}[player], faremo tardi a scuola! Muoviti!{/b}"
    mc "{b}Ok! Sarò lì in un attimo!{/b}"
    kt "{i}Dai su, vai giù. Ci vediamo al mio hotel.{/i}"
    mc "Va bene! Ci vediamo."
    kt "{i}Certo. A dopo~{/i}"
    "Dio, Kotonoha sta diventando davvero una signorina. Sono davvero stupito."
    "Non so cosa avrei dovuto fare se fossi stato in lei."
    "Prima di andare giù in cucina, decido di andare fuori sul balcone."
    
    scene black
    with wipeleft

    scene bg mc_bn
    with wipeleft
    "Ahhhhh! Che bella giornata!"
    "Aspetta, quella era Sayori?"
    mc "Hey, Sayori!"
    "..."
    "Hm, non so se mi abbia ignorato o se non mi ha semplicemente sentito."
    mc "Sayori! Quassopra!"
    s "..."
    "Sayori mi stava per rispondere, però poi si rigira, probabilemente si dirige verso scuola."
    "La lascerò stare per ora. La incontrerò a scuola comunque."
    "Monika probabilmente sta iniziando ad innervosirsi. Dovrei andare ora."

    scene black
    with wipeleft
    #pause 1.0

    scene bg bedroom
    with wipeleft
    #pause 1.0
    scene black
    with wipeleft

    scene bg kitchen
    with wipeleft

    mc "Hey Monika, sono to--"
    show monika 4q at t11 zorder 1
    pause 1.0
    stop music fadeout 1.0
    show monika 4i at t11 zorder 1
    m "[player], {w=0.5}devi essere più responsabile d'ora in poi."
    m "Sai che ore sono?"
    show monika 4h at t11 zorder 1
    "..."
    mc "Scusami Monika, {w=0.5}stavo parlando con Kotonoha a proposito della scuola."
    mc "Ci ha chiesto di---"
    show monika 4q at t11 zorder 1
    pause 1.0
    show monika 4i at t11 zorder 1
    m "Lo so [player], {w=0.5}non c'è bisogno che mi spieghi tutto."
    m "Voglio solo che tu sia più responsabile quando si parla della tua vita scolastica."
    show monika 4h at t11 zorder 1
    mc "Lo so. D'ora in poi sarò più responsabile, {w=0.5}madame."
    show monika 5a at t11 zorder 1
    m "Va bene!~ Così va meglio! Anche se l'ultima parte era un pochino... CRINGE ZI'."
    mc "{w=0.5}G-{w=0.5}già{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}"
    m "Ahaha!~"
    show monika 3b at t11 zorder 1
    mc "Su, ora mangiamo."
    
    scene black
    with wipeleft

    scene bg kitchen
    with wipeleft
    play music nday fadein 4.0
    "La cucina di Monika è deliziosa!"
    "Non sono vegetariano come lei, però quelle sue piccole mani fanno buon uso di quegli ingredienti comunque."
    "20 minuti dopo finimmo di far colazione."
    show monika 1a at t11 zorder 1
    mc "Wow Monika, la tua cucina è davvero buona! Grazie per aver fatto la colazione!"
    show monika 5a at t11 zorder 1
    m "Ahaha!~ Grazie [player]! Dicono che quando fai qualcosa per la persona che ami, quel qualcosa sarà fatto con amore."
    m "Quindi sì! L'ho fatto con l'amore che provo per te~"
    mc "Che carina che sei, Monika. Quindi, dovremmo andare?"
    show monika 3b at t11 zorder 1
    m "Già! Andiamo."
    show monika 3a at t11 zorder 1
    mc "Lasciami prendere lo zaino, credo di averlo lasciato in soggiorno."
    show monika 4b at t11 zorder 1
    m "Ti aspetterò nell'atrio."
    scene bg mc_lr with wipeleft
    "Sospiro." #aqui
    mc "Oggi sarà un gran giorno."
    "Prendo il mio zaino e dirigo nell'atrio, dove mi sta aspettando Monika."
    scene bg mc_hw with wipeleft
    mc "Andiamo, Monika."
    show monika 5a at t11 zorder 1
    m "Forza~"
    scene black
    with wipeleft
    pause 2.0
    play sound closet_open

    scene bg house
    with wipeleft
    pause 2.0
    play sound closet_close
    "Come siamo usciti di casa, Monika mi prende per il polso."
    show monika 1n at t11 zorder 1
    m "Uhm... {w=0.5}[player]."
    mc "Sì?"
    show monika 1m at t11 zorder 1
    m "Posso... {w=0.5}tenerti per mano mentre {w=0.5}andiamo a casa di Kotonoha?"
    mc "Certo. Forza."
    show monika 1k at h11 zorder 1
    "E senza pensarci due volte, Monika afferra la mia mano. La sua mano è così piccola e calorosa. Potrei stare così tutto il giorno."
    show monika at thide
    hide monika
    scene bg street with wipeleft
    "E' così bello vedere le persone che camminano per strada, {w=0.5}i bambini che corrono {w=0.5}Natsuki che è davanti a noi, {cps=2}le macchine--{/cps}"
    stop music fadeout 2.0
    "Aspetta, cosa?!"
    show natsuki 1a at t11 zorder 1
    "Natsuki è {w=0.5}davanti a noi?!"
    "Dio... così non va bene..."
    show natsuki at thide
    hide natsuki
    "Monika, che ancora mi tiene per mano, deve aver notato che un'ondata di panico mi sta assalendo."
    show monika 1f at t11 zorder 1 # aquí 25/09/2019
    m "Uh, {w=0.5}[player], {w=0.5}è troppo per te?"
    mc "C-{w=0.5}cosa? No! {w=0.5}Mi piace, m-{w=0.5}ma, {w=0.5}uh, {w=0.5}mi sono ricordato che questa è la strada più lunga per andare a casa di Kotonoha."
    show monika 3g at t11 zorder 1
    m "Uh, [player], la casa di Kotonoha è più vicina se passiamo per di qua. Che succede?"
    mc "Oh, no, niente. Di qua."
    "Punto verso l'altra parte della strada."
    show monika 2q at t11 zorder 1
    pause 0.5
    show monika 2i at t11 zorder 1
    m "E' per Natsuki?"
    mc "Natsuki? {w=0.5}Dov'è?"
    m "[player], lo so che l'hai vista davanti a noi. L'ho vista anche io."
    show monika 4i at t11 zorder 1
    m "Lo so che tu e Kotonoha state cercando di proteggermi. {w=0.5}Ma voglio sistemare questa faccenda anche io."
    show monika 3f at t11 zorder 1
    m "Ma se voi due continuate a proteggermi eccessivamente, mi sento solo intuile. {w=0.5}Non fraintendermi, mi iace il fatto che ti preoccupi così tanto per me."
    m "Ma devo pensarci io a questo. {w=0.5}i sento al sicuro stando con te. {w=0.5}Sento di poter sistemare tutto con i miei amici grazie a voi."
    show monika 3g at t11 zorder 1
    m "Perfavore, smettetela di iperproteggermi, [player]. Io starò bene."
    show monika 3k at t11 zorder 1
    m "Se sono con te, {w=0.5}è un vantaggio in più~"
    "Immediatamente dopo aver deto questo, Monika si alza in punta di piedi e mi bacia la fronte."
    show monika 5a at t11 zorder 1
    m "Andiamo, Kotonoha ci sta aspettando."
    scene bg st with wipeleft
    play music t2 fadein 4.0
    "Abbiamo corso entrambi fino all'hotel di Kotonoha, Monika mi superò facilemente come pensavo."
    "Devo iniziare ad allenarmi nella corsa se questo dovesse diventare una cosa regolare."
    "Siamo arrivati poco dopo."
    scene bg hotel with wipeleft
    show monika 1a at t21 zorder 1
    show kotonoha 4ba at t22 zorder 1
    "Quando siamo arrivati, Kotonoha ci stava già aspettando alla lobby."
    show monika 1a at t21 zorder 1
    show kotonoha 4bc at t22 zorder 1
    kt "Un pò in ritardo, non credete?"
    show monika 1b at t21 zorder 1
    show kotonoha 4ba at t22 zorder 1
    m "Abbiamo avuto dei...problemi... mentre venivamo qui. Ma li abbiamo sistemati."
    show monika 1a at t21 zorder 1
    show kotonoha 7be at t22 zorder 1
    kt "Problemi?"
    show kotonoha 7be at t22 zorder 1
    show monika 3n at t21 zorder 1
    m "Beh, abbiamo visto ad un certo punto Natsuki che camminava davanti a noi. {w=0.5}E [player] ha provato a proteggermi. Ahaha!~"
    show monika 3n at t21 zorder 1
    show kotonoha 7bf at t22 zorder 1
    kt "Ma è andato tutto bene, vero?"
    mc "Beh, sì. Siamo venuti qui correndo più veloce che potevamo."
    show monika 1e at t21 zorder 1
    show kotonoha 4bo at t22 zorder 1
    kt "Cavolo..."
    kt "Comunque, sono già le 8:15 AM, andiamo. Faremo tardi."
    show kotonoha 4bh at t22 zorder 1
    show monika 1b at t21 zorder 1
    m "Già! Dovremmo prendere l'autobus se vogliamo arrivare più velocemente."
    show monika 3a at t21 zorder 1
    show kotonoha 4bj at t22 zorder 1
    kt "Bene. Andiamo."
    scene black with wipeleft
    scene bg st with wipeleft
    "Usciamo dall'hotel, e ora ci dirigiamo verso la fermata dell'autobus."
    show monika 1a at t21 zorder 1
    show kotonoha 2bd at t22 zorder 1
    kt "Quindi, com'era la colazione?"
    show kotonoha 2ba at t22 zorder 1
    show monika 1b at t21 zorder 1
    m "Deliziosa!"
    show kotonoha 1ba at t22 zorder 1
    show monika 5a at t21 zorder 1
    m "E mangiare con [player] l'ha fatta diventare 10 volte meglio~"
    show monika 5a at t21 zorder 1
    show kotonoha 1bj at t22 zorder 1
    kt "Uhuhu~"
    show kotonoha 1ba at t22 zorder 1
    show monika 3k at t21 zorder 1
    m "Perchè sei così felice oggi, Kotonoha?"
    show monika 3a at t21 zorder 1
    show kotonoha 7bc at t22 zorder 1
    kt "Non lo so, ma oggi mi sento bene. Uhuhu~"
    show kotonoha 7ba at t22 zorder 1
    show monika 3b at t21 zorder 1
    m "Sono contenta di sentirtelo dire~"
    scene black with wipeleft
    scene bg bus with wipeleft
    "8:19 AM. Non faremo mai in tempo."
    m "Prendiamo questo. Non abbiamo più tempo."
    kt "Non so perchè, ma mi sento un pò nervosa ad andare a scuola."
    m "E' perchè è la tua prima volta in un'altra scuola?"
    kt "Forse."
    mc "Hey ragazze, andiamo. Il nostro autobus è arrivato."
    kt "Sì, andiamo."
    scene black with wipeleft
    scene bg st with wipeleft
    scene black with wipeleft
    scene bg street with wipeleft
    scene black with wipeleft
    scene bg residential_day with wipeleft
    scene black with wipeleft
    scene bg school_front with wipeleft
    "Phew, 8:26 AM. E siamo quasi a scuola."
    "Come scendiamo dall'autobus, facciamo uno scatto velocissimo verso l'ingresso."
    scene bg school_corridor with wipeleft
    "8:29 AM. Siamo delle specie dei Dei. Beh, in effetti lo siamo, no?"
    kt "Haaaaaaaah... {w=0.5}Haaaaaaaah... {w=0.5}Haaaaaaaah... {w=0.5}Ce l'abbiamo fatta!"
    stop music fadeout 2.0
    "Ma proprio in quel momento, mi scontrai con qualcuno con dei capelli molto lunghi e di un colore violaceo."
    mc "O-{w=0.5}oh, {w=0.5}Mi dis--"
    mc "Yuri?"
    show kotonoha 1bw2 at t31 zorder 1
    show monika 2f at t32 zorder 2
    show yuri 2e at t33 zorder 3
    "Yuri, che ora guarda nella mia direzione, realizza che sono stato io a scontrarmi con lei."
    mc "Yuri?"
    show kotonoha 4bw2 at t31 zorder 1
    show monika 2f at t32 zorder 2
    show yuri 3y6 at t33 zorder 3
    m "Uh... {w=0.5}Ciao Yuri."
    show kotonoha 4bw2 at t31 zorder 1
    show monika 2g at t32 zorder 1
    show yuri 4d at t33 zorder 1
    "Yuri ha paura di Monika?"
    "Beh, ha delle ragioni per averne."
    y "S-{w=0.5}stai lontana da me!"
    show yuri at lhide
    hide yuri
    show monika 2f at t22 zorder 1
    show kotonoha 4bw2 at t21 zorder 1
    "Cazzo, questo non va bene. {w=0.5}Non va per niente bene."
    show monika 2f at t22 zorder 1
    show kotonoha 7bp at t21 zorder 1
    kt "Dio..."
    m "..."
    mc "Non ha nemmeno risposto alla mia domanda."
    show monika 1g at t22 zorder 1
    show kotonoha 7bp at t21 zorder 1
    m "Credi che Yuri potrà capire davvero tutto questo?"
    show monika 2f at t22 zorder 1
    show kotonoha 4bf at t21 zorder 1
    kt "Non ne ho idea..."
    kt "Sembrava tanto preoccupata e spaventata."
    show monika 2f at t22 zorder 1
    show kotonoha 4bf at t21 zorder 1
    mc "Già... Ma è qualcosa a cui non si può rimdediare."
    play sound school_ring
    window hide(None)
    window auto
    pause 4.0
    show monika 2f at t22 zorder 1
    show kotonoha 5be at t21 zorder 1
    mc "Dunque, {w=0.5}questo è il nostro segnale. {w=0.5}Andiamo in classe ora."
    "Come mi dirigo verso la mia classe, Monika fa per chiamarmi."
    show monika 2n at t22 zorder 1
    show kotonoha 5be at t21 zorder 1
    m "Ehm... {w=0.5}[player]... {w=0.5}Dobbiamo esporre al preside la situazione di Kotonoha..."
    show monika 2f at t22 zorder 1
    show kotonoha 5be at t21 zorder 1
    mc "O-oh! {w=0.5}Y-{w=0.5}già. {w=0.5}Andiamo."
    scene bg school_corridor with wipeleft
    play music sad fadein 4.0
    "Mi stavo quasi dimenticando del \"trasferimento\" di Kotonoha qui. E ora, sono ancora più preoccupato per tutta questa situaizone."
    "Non posso fare a meno di essere distratto quando sono ansioso. Non ho più visto Sayori da stamattina."
    show monika 1f at t11 zorder 1
    "E indovinate? Monika mi sembra un pò giù. E' veramente doloroso vedere Monika così."
    show monika at thide zorder 1
    hide monika
    mc "Monika?"
    show monika 1g at t11 zorder 1
    m "Sì?"
    show monika 1f at t11 zorder 1
    mc "Uhm, stai bene?"
    show monika 1g at t11 zorder 1
    m "S-{w=0.5}sì... {w=0.5}Sto..."
    show monika 1f at t11 zorder 1
    m "...{w=0.5}Bene."
    mc "..."
    mc "Monika, so che c'è qualcosa che non va. Posso vederlo solo guardandoti."
    m "N-{w=0.5}non so se riuscirò a parlare con le ragazze. {w=0.5}Sono mai stata destinata ad essere veramente felice?"
    mc "Dove c'è bianco, c'è nero."
    mc "Dove c'è vita, c'è morte."
    mc "Nella via per essere felice, momenti brutti ci saranno sempre; troverai sempre degli ostacoli."
    mc "Non credi in te stessa, vero?"
    show monika 1g at t11 zorder 1
    m "Non so... Dovrei?"
    m "Non posso farci niente se sento che non accetteranno le mie scuse..."
    show monika at thide
    hide monika
    show kotonoha 1bf at t11 zorder 1
    kt "{i}[player], Voglio provare una cosa.{/i}"
    mc "{i}...{/i}"
    mc "{i}Va bene. Vai.{/i}"
    kt "{i}Dunque, ecco...{/i}"
    scene black
    with dissolve_scene_full
    scene bg school_corridor
    with wipeleft
    show monika 1f at t21 zorder 1
    show mc2 1t at t22 zorder 1
    kt "Uh... Monika..."
    menu:
        m "Hm?"
        "Yuri capirà":
            $ persistent.kt_choice1 = 0
        "Yuri e Sayori capiranno":
            $ persistent.kt_choice1 = 1
        "Andrà tutto per il meglio":
            $ persistent.kt_choice1 = 2
    if persistent.kt_choice1 == 0:
        kt "Uh..."
        "I miei occhi sono fissi su quelli di Monika, la cui faccia è visibilmente angosciata."
        show mc2 at thide
        hide mc2
        show monika 1g at t11 zorder 1
        kt "Sono sicura che Yuri capirà. Lei è abbastanza aperta, anche se non parla molto."
        show monika 1g at t11 zorder 1
        m "Hai visto come mi ha spinto lontano da lei quando è corsa via, o no?"
        show monika 2g at t11 zorder 1
        m "E' chiaro; non vuole parlare con me."
        show monika 1g at t11 zorder 1
        m "E credi che possa capirlo?"
        show monika 1f at t11 zorder 1
        kt "No, hai ragione."
        kt "Ciò nonostante, conosciamo tutti Yuri. Ma lei non sa cosa sta accadendo. E' ovvio che sia spaventata."
        kt "Credo che abbia già abbastanza ragioni per essere spaventata, e ne ha ancor di più se si ricorda tutto quello che è successo."
        show monika 1p at t11 zorder 1
        m "..."
        m "Non so..."
        show monika 1f at t21 zorder 1
        show mc2 1b at t22 zorder 2
        mc "Monika, Kotonoha ha ragione."
        "Improvvisamente [player] iniziò a parlare."
        "Monika ed io ci giriamo a guardarlo."
        show monika 1o at t21 zorder 1
        show mc2 3b at t22 zorder 2
        mc "Come ti stavo dicendo: non ci stai aiutando ad aiutarti."
        show monika 1f at t21 zorder 1
        show mc2 3f at t22 zorder 2
        mc "Non sai quanto mi spezza il cuore vederti così giù. Come fai ad essere così insicura di te stessa?"
        mc "Siamo qui per aiutarti. Io sono qui per renderti felice."
        mc "Devi solo calmarti e iniziare a pensare positivo. Kotonoha ed io faremo tutto quello possiamo nel nostro raggio."
        show monika 1f at t21 zorder 1
        show mc2 3a at t22 zorder 2
        mc "Vero, Kotonoha?"
        kt "Affermativo."
        "A dire il vero non ho sentito niente di quello che ha detto [player], ma credo di aver risposto correttamente."
        "[player]... Così vicino ma così lontano..."
        "Ma.. Lo script mi sta facendo sentire così per colpa di [player]? Credo di sì."
        "Non posso far nient altro se non pensare a [player]..."
        "Però in ogni caso ho una missione. Devo aiutare Monika e [player] ad essere felici e sistemare tutto nel Club di Letteratura."
        "Ahaha... Quindi è così che ti senti, Monika..."
        show monika 1q at t21 zorder 1
        show mc2 2a at t22 zorder 2
        m "Okay... Ci proverò."
        show monika 1o at t21 zorder 1
        show mc2 2c at t22 zorder 2
        stop music fadeout 2.0
        mc "Allora, andiamo."
        show monika 1m at t21 zorder 1
        show mc2 2a at t22 zorder 2
        m "Sì! Chiederò al preside se Kotonoha potrà tenere un esame scritto per essere ammessa in classe, [player]."
    elif persistent.kt_choice1 == 1:
        kt "Hm..."
        "[player] fa un passo indietro e dice \"tutte voi\" senza guardare anche me."
        show mc2 at thide
        hide mc2
        show monika 1g at t11 zorder 1
        m "Kotonoha, quali sono i tuoi pensieri riguardo a questo?"
        show monika 1f at t11 zorder 1
        kt "Uhhh... Beh..."
        "Cosa dovrei dire?"
        "Okay... Farò quello che Naomi farebbe..."
        kt "Cioè... Penso che Yuri e Sayori capirebbero tutto e perchè hai fatto quello che hai fatto."
        kt "C'è la possibilità che non capiscano, però."
        "Non so cosa sto dicendo! Non posso fare a meno di pensare a [player] quando ce l'ho di fianco!"
        "Sono davvero ossessionata da [player]?"
        "Non so cosa pensare. Non so niente. Ma devo fare qualcosa!"
        kt "Sto dicendo che potremmo provare a parlare a tutti oggi nella stanza del club, riunendo tutti per il primo compito."
        kt "Uh... Oggi proverò a parlare con Natsuki. [player], tu puoi provare a parlare con Sayori?"
        show monika 2f at t21 zorder 1
        show mc2 2d at t22 zorder 2
        mc "Oh, ehm, posso provare a parlarle finché siamo nella stessa classe."
        mc "Non prometto niente però. L'ho vista stamattina che stava andando a scuola, l'ho salutata ma si è rifiutata di rispondermi."
        kt "Okay, allora questo è il tuo compito!"
        "Mi giro verso di lui, sorridendo gentilmente."
        kt "Monika, tu devi parlare con Yuri. Penso tu sia l'unica che possa convincerla."
        show monika 1g at t21 zorder 1
        show mc2 2d at t22 zorder 2
        m "Perchè lo pensi?"
        show monika 1f at t21 zorder 1
        show mc2 2d at t22 zorder 2
        kt "Beh, {w=0.5}so che siete amic--"
        stop music
        pause 2.0
        play music hb
        show black:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        with char_fade
        show layer master at heartbeat
        mc_b "No, Kotonoha."
        $ s_name = "Sayori"
        stop music
        hide black
        show layer master at thide
        hide layer master
        kt "Gh--"
        "{i}Ahhhhh! Non farlo!{/i}"
        "Provo a ridurre il dolore che sento al petto, ma senza alcun risultato."
        show monika 1f at t21 zorder 1
        show mc2 2i at t22 zorder 2
        mc "Kotonoha? Stai bene?"
        kt "O-Oh! Sì, sto bene, sono solo un pò in difficoltà per colpa del ciclo."
        show monika 1g at t21 zorder 1
        show mc2 2i at t22 zorder 2
        play music sad fadein 4.0
        m "E' successo qualcosa, Kotonoha?"
        show monika 1f at t21 zorder 1
        show mc2 2i at t22 zorder 2
        kt "Uh no, sto bene. Non preoccupatevi, ragazzi."
        "Ti prego dimmi che posso ingannarli con il mio sorriso, come ero solita fare con Naomi..."
        kt "Sto bene, vedete?"
        "Rivolgo un sorriso a Monika e [player] mentre apro le braccia per far capire che sto bene."
        show monika 1n at t21 zorder 1
        show mc2 2b at t22 zorder 2
        m "Okay... allora, andiamo."
        show mc2 at thide
        hide mc2
        show monika 1g at t11 zorder 1
        "Sembra che io sia riuscita a fregare Monika. Ma..."
        show monika at thide
        hide monika
        show mc2 5b at t11 zorder 1
        "--[player] mi sta guardando in modo strano. Non sono riuscita ad ingannarlo?"
        "Solo sentire i suoi occhi su di me mi fa battere forte il cuore..."
        kt "Allora, andiamo!"
        show monika 2n at t21 zorder 1 #with char_fade
        show mc2 2d at t22 zorder 2 #with char_fade
        m "Quindi, ora dovremmo andare all'ufficio del preside?"
        show monika 2e at t21 zorder 1
        show mc2 2c at t22 zorder 2
        mc "Già. Andiamo."
        m "Sì! Chiederò al preside se Kotonoha potrà tenere un esame scritto per essere ammessa in classe, [player]."
    else:
        kt "Monika, non so quante volte dobbiamo ripeterti che andrà tutto bene."
        "Andrà bene se glielo urlo?"
        "Direi di sì. Questo è un compito che mi è stato dato: proteggerla e aiutarla a sistemare tutto."
        kt "Nonostante tutto sembri andare male, decidi tu se vuoi espiare i tuoi peccati."
        show monika 1p at t21 zorder 1
        show mc2 2d at t22 zorder 2
        m "Stai parlando di Yuri..."
        show monika 1o at t21 zorder 1
        show mc2 2d at t22 zorder 2
        "Monika sembra non capire la gravità di quello che ha fatto, quindi credo sia arrivato il momento di attivare la mia 'serious mode'."
        "Mentre agito la mano per dire a [player] di fare un passo indietro, lui si avvicina e si mette di fianco a me."
        show mc2 at thide
        hide mc2
        show monika 1o at t11 zorder 1
        "..."
        "Perchè sono così nervosa? Il mio cuore batte all'impazzata!"
        "Concentrati Kotonoha... Concentrati... Una volta a casa potrai fantasticare liberamente."
        kt "E' normale dubitare della tua situaizone attuale se le cose non vanno come previsto."
        kt "Ciò nonostante, dubita troppo di te stessa e diventerai una pessimista. E sinceramente non fa proprio per te."
        show monika 1f at t11 zorder 1
        m "..."
        kt "Dall'altra parte, [player] ed io ti abbiamo detto che andrà tutto bene. Ti aiuteremo a ricucire il rapporto di amicizia con le altre."
        show monika 1f at t21 zorder 1
        show mc2 3x at t22 zorder 2
        mc "Ha ragione."
        "Improvvisamente [player], d'accordo con me, fa un passo avanti..."
        "...e mette la sua mano sulla mia spalla..."
        "[player]..."
        mc "Ci siamo noi. Non preoccuparti."
        show monika 1f at t21 zorder 1
        show mc2 3f at t22 zorder 2
        mc "E come ti ho giò detto: lascia che ti aiutiamo."
        mc "Puoi provare a pensare positivo almeno?"
        show monika 1f at t21 zorder 1
        show mc2 1f at t22 zorder 2
        mc "Kotonoha ed io ti aiuteremo."
        "Detto questo, [player] mette la mano sulla mia spalla e mi tira verso di lui."
        "Ho cercato di nascondere la mia faccia arrossita guardando per terra. Sembra abbia funzionato; lui non ha detto niente a riguardo."
        mc "Prova soltanto a rimanere positiva. Noi faremo il lavoro pesanteWe'll do the heavy lifting."
        show monika 1f at t21 zorder 1
        show mc2 3c at t22 zorder 2
        mc "Va bene?"
        show monika 1f at t21 zorder 1
        show mc2 3a at t22 zorder 2
        m "..."
        show monika 1m at t21 zorder 1
        show mc2 3a at t22 zorder 2
        m "Va bene..."
        show monika at thide 
        hide monika
        show mc2 at thide
        hide mc2
        stop music fadeout 2.0
        "Cos--"
        "Ci siamo dimenticati di andare all'ufficio del preside!"
        "Spero soltanto non siamo in ritardo..."
        "Prendo il telefono dalla mia borsetta."
        pause 2.0
        kt "Uhm... Hey ragazzi."
        show monika 2c at t21 zorder 1
        show mc2 1h at t22 zorder 2
        $ m_name = "[player] e Mon"
        m "Hm?"
        $ m_name = "Monika"
        kt "Sono già le 9:54 e non siamo ancora andati dal preside..."
        show monika 2l at t21 zorder 1
        show mc2 2d at t22 zorder 2
        mc "Cazzo, dovremmo andare allora!"
        show monika 2n at t21 zorder 1
        show mc2 2d at t22 zorder 2
        m "Già... Andiamo."
        m "Non preoccuparti [player], Io gli spiegherò come si è risolta la situazione di Kotonoha."
        show monika 2m at t21 zorder 1
        show mc2 2a at t22 zorder 2
        mc "Bene. Andiamo."
    scene black
    with wipeleft
    play music nday fadein 4.0

    scene bg school_corridor
    with wipeleft
    "Quanto sono difficili queste cose..."
    "Però non ho scelta."
    if persistent.kt_choice1 == 0:
        "Spero solo che Yuri capirà..."
        $ perc = "%"
        "Spero che Monika riesca almeno a portarla nella stanza del club. Se non dovesse riuscirci..."
        "Quello sarebbe il 50[perc] del fallimento totale dell'operazione."
        "E sì, Natsuki è il 50[perc] dell'operazione di oggi. Credo veramente di poter parlare a Natsuki e convincerla a venire al club."
    elif persistent.kt_choice1 == 1:
        "Cioè, spero solo che Sayori e Yuri capiranno."
        "Sayori è troppo gentile per ignorare qualcosa del genere. Yuri, però..."
        "Lei è già spaventata. Si vede, e ha anche tutto il diritto di esserlo."
        "Non so come [player_b] abbia fatto a cancellare i ricordi di Naomi..."
        "'Vorrei sapere come. Ciò nonostante so quali sono i miei limiti."
        "Non sono mica un robot che può imparare tutto in un attimo."
    else:
        "Dopotutto, [player] ha pormesso a Monika che sarebbe andato tutto bene."
        "Beh,  credo di averglielo detto pure io. Anche sapendo che non potr' andare tutto per il meglio, tengo alte le mie aspettative."
        "Sto spreando che [player] metta prima tutti i suoi sforzi. Ovviamente far; anche io del mio meglio."
    "Per adesso...Non so come togliermi dalla testa [player]..."
    "A questo punto avrei preferito perdere i ricordi pure io."
    "Nonostante questo sentimento, provo a sorridere anche se forzatamente."
    show monika 1k at t21 zorder 1
    show mc2 4k at t22 zorder 2
    "Nel mentre, dietro di me [player] e Monika stanno chiacchierando allegramente."
    "Credo sia un gran vantaggio essere così alti, così il dolore è quasi del tutto impercettibile se cammino davanti a loro."
    "Quasi..."
    show monika at thide
    hide monika
    show mc2 at thide
    hide mc2
    "Ora stiamo camminando nel cortile della scuola, e Monika ci sta accompagnando nell'ufficio del preside."
    "Mi sento un pochino strana. Vorrei dirgli che ci sono anche io, ma sono sicura che {i}qualcuno{/i} mi punirebbe."
    "Credo di potermici abituare. E poi, mi mancava il profumo degli alberi, l'aria fresca... E' così nostalgico."
    scene black
    with wipeleft
    scene corridor
    with wipeleft
    "Dopo qualche minuto di camminata, entriamo nell'edificio principale dove si trovano tutti gli uffici amministrativi e alcune classi."
    "Parlo del sistema scolastico, infermeria, classi di detenzione per gli studenti e la sala professori."
    "Come cammino nel corridoio, posso vedere gli studenti nelle loro classi. ALmeno finché i miei occhi non scrutano una classe alla mia sinistra."
    pause 2.0
    "Non è come se avessi visto un fantasma o qualcos'altro. Ma ho visto dei capelli rosa lucenti. Scommetto che è Natsuki."
    "Giusto per essere sicuri, dò un'occhiata dalla porta di nuovo. Già, è proprio lei. Forunatamente non sembra avermi visto."
    "La fisso finché Monika corre verso di me e si ferma davanti a me."
    show monika 5a at t11 zorder 1
    m "Kotonoha~"
    "Se Natsuki sente la voce di Monika, potrebbe dare non pochi problemi. Per questo la evito."
    show monika at thide
    hide monika
    "Per fortuna Natsuki non ha sentito niente. Beh, almeno mi piace pensarla così."
    mc "{i}Che problemi hai?{/i}"
    "Sento [player] che mi sta parlando."
    kt "Natsuki è in quella classe. Dobbiamo fare attenzione e fare piano per ora."
    show monika 2f at t11 zorder 1
    m "Kotonoha? Cosa c'è?"
    "Improvvisamente Monika viene di nuovo verso di me piuttosto preoccupata."
    kt "Oh! Sì, ero solo persa nei miei pensieri."
    show monika 2f at t11 zorder 1
    pause 1.0
    show monika 2g at t11 zorder 1
    m "I tuoi pensieri?"
    m "E' successo qualcosa, Kotonoha?"
    show monika 2f at t11 zorder 1
    kt "No, sto bene. Sono solo un pò nervosa."
    show monika 2m at t11 zorder 1
    m "Oh! Ahaha!~"
    show monika 1b at t11 zorder 1
    m "Non preoccuparti Kotonoha! Andrà tutto bene!"
    kt "Hehe... Okay, proverò a calmarmi."
    stop music fadeout 2.0
    show monika at thide
    hide monika
    if persistent.kt_choice1 == 1:
        "..."
        show mc2 5e at t11 zorder 1
        "I miei occhi incontrano quelli di [player], e posso dire che sospetta chiaramente di me."
        "I suoi occhi fissati ai miei, ma il mio arrossimento rovina tutto."
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    play music hp fadein 4.0
    "Dopo una lunghissima camminata, cercando l'ufficio amministrativo, alla fine lo trovammo. Una porta di legno scuro."
    show monika 3b at t11 zorder 1
    m "Eccolo lì."
    "Monika indica la porta col dito."
    play sound door
    pause 5.0
    "Una voce molto acuta si sente improvvisamente dall'interno della stanza."
    $ n_name = "???"
    n "Chi è?"
    m "Sono Monika, Signor Preside. Posso entrare?"
    $ n_name = "Preside"
    n "Oh, Monika! Certo!"
    scene black
    with wipeleft
    scene bg office
    with wipeleft
    "Come entrai nell'ufficio del preside realizzai quanto fosse spaziosa quella stanza. Wow, non mi sarei mai aspettata che sarei dovuta entrare qui dentro."
    "Monika saluta il preside, con un inchino. [player] la segue a sua volta."
    "Io faccio lo stesso per mostrare rispetto."
    n "Ma guarda che sorpresa!"
    m "Ahaha!~"
    m "Anche lei, Preside."
    n "Hai bisogno di qualcosa?"
    m "Sì! Ricorda di quella ragazza di cui le ho parlato? Quella che doveva trasferirsi nella nostra scuola."
    "Il preside guarda il soffitto cercando di ricordare."
    n "Hm... Non ricordo."
    n "Potresti ricordarmi perfavore?"
    m "Il giorno prima del festival."
    n "Hm..."
    "Il preside accende il suo computer, e inizia a controllare qualcosa."
    pause 2.0
    "Sono passati 2 minuti e sta ancora cercando qualcosa sul suo computer."
    pause 1.0
    "..."
    "La calma di Monika è impressionante."
    kt "{i}[player], credi andrà tutto bene?{/i}"
    mc "{i}Non lo so...{/i}"
    pause 1.0
    "Sono passati 7 minuti e finalmente il preside comincia a parlare."
    n "Oh, giusto! Infatti ho trovato la registrazione di una ragazza, ma sembra non si sia ancora presentata."
    m "Beh, quella ragazza è proprio di fianco a me!"
    "Una volta che Monika ha detto questo, mi prende per il polso e mi trascina verso la scrivania del preside."
    n "Oh, capisco. Come ti chiami, signorina?"
    "..."
    "Calmati Kotonoha. E' una semplice domanda."
    kt "E-{w=0.5}ehm... {w=0.5}Mi chiamo Kotonoha, Signore."
    n "Kotonoha, eh?"
    n "Bel nome."
    "Il preside mi sorride, facendomi sentire ancora più imbarazzata."
    n "Pensavo che saresti venuta qui ieri. Che è successo?"
    "Il preside usa un tono più serio."
    kt "Beh... Io--"
    "Monika, notando che ero nel panico, si fa avanti al posto mio."
    m "Beh, il suo volo è stato ritardato."
    n "Monika, apprezzo la tua risposta ma sto parlando con Kotonoha."
    m "E' un pochino timida, signor preside."
    n "Va bene."
    n "Quindi, l'affermazione di Monika è vera signorina?"
    kt "S-{w=0.5}sì! Il mio volo è stato ritardato. {w=0.5}Vengo dal... {w=0.5}Kansai, da Osaka precisamente."
    n "Hm..."
    n "Capisco. Sei venuta senza la nostra uniforme."
    kt "S-{w=0.5}sì, {w=0.5}mi scusi!"
    "Alzo la voce e mi scuso."
    "Sto esagerando forse, vero?"
    "Devo calmarmi... {i}Inspira{/i} ed {i}espira{/i}..."
    pause 2.0
    "Ok, facciamolo."
    n "Non c'è bisogno di scusarsi se sei una nuova studente. E' normale."
    mc "{i}Kotonoha, calmati.{/i}"
    kt "{i}{w=0.5}S-sì...{/i}"
    n "Beh, non importa. Vado a cercare una classe dove posso metterti."
    kt "V-{w=0.5}va bene."
    "Mentre aspettiamo, non diciamo niente e aspettiamo che il preside abbia finito."
    "La calma di Monika mi allieta, [player] è nel suo ruolo da \"tipa tosta\", e beh... Io non riesco a calmare i miei nervi."
    pause 2.0
    "Dopo un pò di minuti il preside mi chiama, invitandomi a sedermi sul divanetto. Tira fuori due fogli dalla stampante."
    n "Allora, ci sono due classi disponibili: la numero 100 e la 150. Sui questi fogli ci sono i nomi dei tuoi compagni di classe, e i banchi non occupati."
    n "Scegli quella che più ti aggrada - sappi che una volta scelta una classe, non potrai cambiarla."
    "In quel momento posiziona i due fogli su un tavolino."
    menu:
        kt "Hm..."
        "Foglio 1":
            $ sheet = 0
        "Foglio 2":
            $ sheet = 1
    if sheet == 0:
        "Prendo il primo foglio."
        call showpoem(sys_list, music=False) from _call_showpoem_6
        "Hm..."
        "Natsuki è in questo gruppo. Se scelgo questo magari potrei provare ad approcciarla."
        "...Se sono fortunata, potrei parlarle e convincerla a venire nella stanza del club."
        "Sarà una buona ideaIs that a good idea?"
        "Certo, è chiaramente una buona idea."
        "Sono sicura di poter avvicinarmi a Natsuki, ma se decidesse di non parlarmi..."
    else:
        "Hm."
        stop music fadeout 2.0
        "Dovrei controllare il secondo."
        call showpoem(sys_listb, music=False) from _call_showpoem_7
        play music goodbye fadein 4.0
        "..."
        "No..."
        "Naomi?"
        "Devo aver sbagliato a leggere di sicuro. Lo rileggo di nuovo."
        call showpoem(sys_listb, music=False) from _call_showpoem_8
        "No..."
        "Naomi è nella classe 150..."
        stop music fadeout 2.0
        "No Kotonoha, ci sono cose più importanti di cui occuparsi ora."
        "Avrò tante possibilità per avvicinarmi a Naomi. E solo una per sistemare questo mondo."
    scene black 
    with wipeleft
    scene bg office
    with wipeleft
    if sheet == 1:
        play music nday fadein 2.0
    else:
        pass
    if sheet == 0:
        n "Quindi, signorina, qual è la sua scelta?"
        kt "N-{w=0.5}non ho ancora controllato l'altro foglio."
        n "Va bene, prenditi il tuo tempo."
        kt "Ok."
        stop music fadeout 2.0
        call showpoem(sys_listb, music=False) from _call_showpoem_9
        kt "..."
        play music goodbye fadein 2.0
        "Ho letto per caso... Naomi?"
        "Devo leggerlo di nuovo."
        call showpoem(sys_listb, music=False) from _call_showpoem_10
        "..."
        "Sento le lacrime scendere dai miei occhi."
        m "Uh... Kotonoha?"
        kt "Uhm--"
        kt "S-sì?"
        m "Stai piangendo?"
        "Naomi... Non riesco a smettere di pensare a tutti i bei momenti passati insieme..."
        "Monika mi sta guardando con un preoccupazione; Dovrei risponderle."
        kt "Oh! Non preoccuparti. Mi bruciano gli occhi per qualche ragione."
        m "..."
        n "Potresti sbrigarti?  Ho altre faccende da sbrigare."
        stop music fadeout 2.0
    else:
        #stop music fadeout 2.0
        n "Quindi, qual è la sua scelta, signorina?"
        kt "Uhm... Non ho ancora controllato il primo foglio."
        n "Certo, prenditi il tuo tempo."
        kt "Glielo farò sapere appena avrò scelto."
        n "Mhm."
        call showpoem(sys_list, music=False) from _call_showpoem_11
        kt "Hm"
        "Natsuki è in questo gruppo."
        "Perfavore dimmi che posso riuscire a fermare il tempo..."
        stop music
        window hide(None)
        window auto
        $ style.say_dialogue = style.normal
        pause 2.00
        show black zorder 100:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        with char_fade
        kt "Gh--"
        "Haaaaaaaah... Ce l'ho fatta!"
        "Non so come [player_b] possa sopportare questo sforzo quando ferma il tempo."
        kt "Ehi [player], vieni qua."
        mc "Huh? Non ci sentono, vero?"
        "[player] è davanti a Monika, e la sta colpendo sulla faccia."
        "E' stata una scelta giusta?"
        kt "No. Vieni qua."
        "[player] si dirige verso il divanetto, e si siede di fianco a me."
        show mc2 3b at t11 zorder 1
        mc "Cosa c'è?"
        kt "Guarda tu stesso."
        "Gli passo il foglio con la lista dove c'è il gruppo di Natsuki."
        call showpoem(sys_list, music=False) from _call_showpoem_12
        kt "Natsuki è in questo gruppo. Va bene se scelgo questo qua?"
        show mc2 2a at t11 zorder 1
        mc "Vai. Sarà tutto più semplice così, no?"
        kt "E' quello che penso anche io. Bene, ritorna al tuo posto."
        mc "Capito."
        show mc2 at thide
        hide mc2
        kt "..."
        hide black with char_fade
        n "Quindi, qual è la sua scelta, signorina?"
    kt "Oh, beh... Vorrei unirmi alla classe 100"
    n "Bene. Prego, potrebbe dirmi il suo nome?"
    kt "Certo, mi chiamo Kotonoha."
    pause 2.0
    n "Cognome?"
    kt "Io... Non ce l'ho. {i}Soltanto Kotonoha{/i}."
    n "Hm..."
    play music nday fadein 4.0
    n "Fatto. Inizi oggi stesso."
    "Wow."
    "E' stato abbastanza insidioso. Felice di avercela fatta, ma è solo la prima parte del nostro piano."
    "Devo rimanere calma fino alla fine di oggi."
    if sheet == 1:
        "Anche se non vado da Naomi, sono abbastanza convinta di riuscire a riparare la nostra amicizia."
        "...Anche se non si ricorda di me."
    else:
        "Spero solo che con Natsuki vada tutto bene. Mi sento giusto un po' spaventata quando penso di dover parlare con lei."
        "Ma è ora o mai più."
    n "Va bene."
    m "Uhm... {w=0.5}Signor Preside..."
    m "Potrebbe darci il permesso per entrare in classe in ritardo?"
    n "Certo, datemi un momento. Sto stampando l'orario della tua amica."
    m "Okay!~"
    scene black
    with wipeleft
    scene bg office
    with wipeleft
    "Il preside ha stampato il mio orario, mentre consegna a Monika e a [player] il permesso per i loro insegnanti."
    "Bene, qua è dove il comincia il piano."
    scene black
    with wipeleft
    scene corridor
    with wipeleft
    n "Bene ragazzi, voi due dovreste andare nelle vostre classi. Mostrerò alla vostra amica dov'è la sua classe."
    mc "Sì signore."
    m "Okay!~"
    "Monika mi lancia un sorriso affettuoso."
    show monika 5a at t11
    m "CI vediamo per pranzo!~"
    show monika at thide
    hide monika
    "Una volta detto questo, entrambi si dirigono verso le loro classi."
    "{i}*sigh*{/i}"
    "Beh, vediamo cosa mi aspetta."
    stop music fadeout 2.0
    n "Vuole seguirmi, signorina?"
    n "Sì, andiamo."
    scene black 
    with wipeleft
    scene corridor
    with wipeleft
    play music tkotonoha_b fadein 4.0
    "Camminare di fianco al preside non è così male, ma sono un po' a disagio."
    "Mi sta chiedendo cose riguardo alla mia vita, cose come: perchè ho deciso di entrare in questa scuola, da dove vengo e altra roba."
    "Posso dire di essere del Kansai, della prefettura di Osaka perchè quello è vero."
    "Ma inventarmi storie false in modo che sembrino vere è abbastanza difficile."
    "Inoltre il preside sembra essere una persona davvero gentile, mi ricorda Monika."
    n "Okay, signorina Kotonoha, eccoci qui."
    "Arriviamo alla porta della classe dove si trova Natsuki."
    play sound door
    "Il preside bussa alla porta."
    pause 3.5
    n "Mi scusi professore, posso entrare? Sono il preside. Devo presentarle un nuovo studente."
    $ n_name = "Professore"
    n "Oh, certamente signor Preside. Entri pure."
    scene black
    with wipeleft
    scene bg club_day
    with wipeleft
    $ n_name = "Preside"
    n "Buongiorno, questa signorina si unirà a voi oggi."
    $ n_name = "Professore"
    n "Capisco. Per favore aspetta qui mentre parlo col preside."
    kt "O-oh, certo."
    "Con questo, aspetto indicazioni dal preside."
    "Una volta entrata, noto che l'attenzione di tutti è altrove: alcuni scrivono qualcosa sui loro quaderni, altri che stanno chiacchierando e ehm..."
    show natsuki 1k at t11 zorder 1
    "Natsuki è al suo banco che non sta facendo niente, ma vedo che mi sta fissando."
    "Forse mi ha vista con Monika qua fuori...?"
    "Non lo so... Non so neanche come spiegarglielo se dovesse chiedermelo."
    show natsuki at thide
    hide natsuki
    "Il treno dei miei pensieri si blocca quando il preside richiama l'attenzione della classe."
    n "Cari studenti, fate silenzio per favore. Oggi è arrivata una nuova studentessa e sarà vostra compagna da oggi."
    n "Viene dal Kansai, per questo il suo accento è un po' diverso dal vostro. Confido anche nel fatto che voi non la emarginiate."
    n "Dopotutto, è nuova e ha bisogno di farsi degli amici."
    "Beh, non che loro possano ferirmi. Ero un'emarginata nella classe dove stavo prima, quindi non m'importa."
    "Naomi era la mia sola amica, ma non m'interessava neanche di averne altre quindi non importa."
    n "Vorrebbe presentarsi, signorina?"
    kt "Oh! Certo, uhm... Mi chiamo Kotonoha e vengo dalla prefettura di Osaka. Ehm..."
    "Oh, eddai, Kotonoha! Non essere timida!"
    kt "Sono venuta in questa scuola perchè... Mi piace molto questo posto e vivo qua vicino."
    kt "E mi dispiace anche per essere venuta senza l'uniforme addosso!"
    "Beh, credo sia abbastanza. Però dovrei smettere di essere così timida."
    kt "Piacere di conoscervi e spero potremmo essere amici."
    "Dopotutto non sanno chi io sia. A me va bene così."
    n "Okay signorina, prego vada a cercarsi un posto libero."
    "Il preside è stato molto carino con me. Non so perchè [player] mi ha detto che è una persona con cui è difficile discutere."
    "Afferro allegramente con entrambe le mani la mia borsa, e do al preside una risposta."
    kt "Sì!"
    "Camminando lentamente tra le file di banchi cercando un posto libero, ne noto uno vuoto affianco a Natsuki. Qual è la probabilità di successo?"
    scene black
    with wipeleft
    scene bg kt_classroom
    with wipeleft
    "Metto la borsa sul tavolo mentre mi siedo, tirando fuori il quaderno che ho materializzato con la console ieri."
    "Sì, lo so... Avevo detto \"Non abuserò più della console\", ma era un'emergenza. O almeno mi piace pensarla così."
    stop music fadeout 2.0
    "Dovrei trovarmi un lavoro dato che nessuno mi può aiutare. Neanche i miei genitori."
    "Dovrei anche trovare Naomi e provare a essere di nuovo sua amica... Mi manca davvero tanto."
    "Persa di nuovo nei miei pensieri, sento qualcuno che mi sta chiamando."
    $ n_name = "???"
    n "Hey."
    kt "Ah-"
    kt "Sì?"
    show natsuki 1k at t11 zorder 1
    n "Conosci la ragazza con il fiocco in testa?"
    $ persistent.n_seen = True
    kt "Gh-"
    "Lo sapevo! Ci ha visti!"
    kt "Uh... ti conosco?"
    play music tnatsuki_c
    show natsuki 2k at t11 zorder 1
    n "Mi chiamo Natsuki."
    $ n_name = "Natsuki"
    kt "Oh! Natsuki! Piacere di conoscerti!"
    "Le faccio il mio miglior falso sorriso."
    show natsuki 2w at t11 zorder 1
    n "Hmph."
    show natsuki 2k at t11 zorder 1
    n "Sai chi è quella ragazza?"
#    show natsuki 2k at t11 zorder 1
    kt "Uh..."
    "Un'altra volta Kotonoha."
    kt "Beh, in realtà no. L'ho incontrata perchèè... Mi sono persa quando sono arrivata qui e mi ha mostrato la strada."
    kt "Sì! Proprio così."
    window hide(None)
    window auto
    show natsuki 1c at t11 zorder 1
    pause 2.0
    show natsuki 1e at t11 zorder 1
    n "Sento puzza di cazzate. Non pensare di poter mentire con me e sfuggire così."
    "E' così?"
    show natsuki 1e at t11 zorder 1
    n "La conosci, vero?"
    show natsuki 1g at t11 zorder 1
    kt "N-no! Ti sbagli!"
    "Tempo di far uscire la \"ragazza carina e indifesa\" che c'è in me."
    window hide(None)
    window auto
    show natsuki 1n at t11 zorder 1
    pause 2.0
    show natsuki 5m at t11 zorder 1
    n "Sicura?"
    "Fregata, Natsuki."
    kt "S-sì..."
    window hide(None)
    window auto
    show natsuki 1u at t11 zorder 1
    pause 2.0
    show natsuki 5m at t11 zorder 1
    n "V-va bene..."
    n "Scusa."
    "Wow, non pensavo di poterla fregare per davvero. Sono davvero brava."
    $ m_name = "Professore"
    m "Signorina Natsuki, vorrebbe contribuire in qualche modo alla spiegazione di questa lezione?"
    n "N-non proprio."
    m "Allora non parli in classe. e faccia silenzio. Signorina Kotonoha, Sei qui da troppo poco, per favore non mi causi problemi."
    kt "S-sì, Professore. Mi scusi."
    m "Adesso, prestate attenzione alla lezione di oggi-"
    $ n_name = "Koto & Nat"
    n "Sì, Professore!"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    "Sento delle risatine provenire dai banchi affianco a me e Natsuki, ma le ignoro."
    n 1l "Vuoi parlare dopo le lezioni?"
    kt "Certo!"
    show natsuki at thide
    hide natsuki
    "Dicendo questo, Natsuki fa voltare leggermente la testa del professore di nuovo."
    "Oof... Sono stata fortunata. Non ho idea di come abbia fatto a cavarmela."
    "M'immagino come potrà reagire quando inevitabilmente noterà che sto mentendo?"
    "Non ne sono sicura. Ma il solo pensiero mi riempie il petto di ansia e preoccupazione. Perchè [player_b] ha scelto me?"
    "Ma ancora più importante... Sarò in grado di dire agli altri chi ero? O cosa sto facendo qui?"
    scene black
    with wipeleft
    stop music fadeout 2.0
    scene bg kt_classroom
    with wipeleft
    "E' passata già un'ora, e il professore sta spiegando le leggi di Newton."
    "Odio fisica, però non è che possa lamentarmi. Dopotutto, non mi cambia niente studiare in questo mondo falso?"
    "Ho sempre studiato perchè volevo essere qualcuno, volevo essere una donna d'affari di successo. Ma ora? Ora voglio solo..."
    "Voglio solo terminare la mia vita in questo disastro di mondo. E' meglio così."
    "No Kotonoha, non puoi pensarla così. Fallo per [player]. Fallo per Naomi..."
    scene black
    with dissolve_scene_full

    show text("{size=100}{color=#6debab}{b}Nel mentre nella classe di{/b}{/size}{/color}\n{size=60}[player].{/size}"):
      yalign 0.5
    with dissolve_scene_full
    pause 2.0

    scene bg class_day
    with dissolve_scene_full
    "Aghhh... Matematica è così noiosa! Chiunque l'abbia inventata era un'idiota. Non posso fare a meno di sentirmi stanca, ma se non voglio compiti extra devo rimanere sveglia."
    "Poi, non ho idea di cosa possa succedere oggi con Sayori... E' stata un po' sprezzante verso di me."
    "Quando incrocio i miei occhi con i suoi, lei guarda altrove. Sta prestando attenzione alla lezione."
    "Devo portarla alla stanza del club, il resto non ha importanza. Devo aiutare Kotonoha dopo tutto l'aiuto che ha dato a me."
    play sound school_ring
    window hide(None)
    window auto
    pause 3.0
    "Ahhhh, finalmente! Iniziavo ad annoiarmi."
    $ s_name = "Professore"
    s "Bene ragazzi, non dimenticatevi dei compiti per domani! Potete andare."
    $ s_name = "Sayori"
    "Mi precipito fuori dalla porta nervosamente. Devo fermare Sayori prima che se ne vada."
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    "Wow, non pensavo potessi muovermi così velocemente. I miei poteri da codificatore mi hanno trasformato in un super-umano?"
    "[player], smetti di pensare a cose stupide! Hai cose più importanti a cui pensare."
    "Ecco Sayori. Dai, [player]."
    show sayori 1k at t11 zorder 1
    mc "Hey Sayori."
    show sayori at thide
    hide sayori
    "Ancora una volta mi ha ignorato, guardando altrove e varcando la porta."
    mc "Sayori!"
    "Le afferro con risolutezza il polso, fermandola."
    mc "Adesso basta Sayori! Che ti succede?"
    show sayori 1f at t11 zorder 1
    s "..."
    mc "Eddai, Sayori. Non te lo chiederò di nuovo."
    s "Monika..."
    mc "Monika?"
    s "Ieri ho visto che eri con Monika..."
    mc "Hm?"
    "Beh... Ad essere onesti non mi aspettavo che ci avesse visti. Le luci erano spente."
    mc "Già."
    s 2k "...ed è entrata in casa tua."
    mc "Sì."
    s "..."
    "Non mi piace trattarla così, ma ho altra scelta? Non credo."
    play music t9 fadein 2.0
    show sayori 1h at t11 zorder 1
    s "Ti ricordi cosa ci ha fatto, vero?"
    mc "Sì. Lo so, lo so."
    mc "So tutto, è per questo che sono qui."
    s 1f "Cosa?"
    mc "Ho parlato con Monika, e lei si sente {i}veramente{/i} male per ciò che ha fatto."
    s "Non ha assolutamente senso."
    s 3h "Mi ha fatto IMPICCARE!"
    s 3w "Come può essere dispiaciuta dopo aver fatto una cosa così?!"
    "..."
    "Quando ci ha visti? Dio... Non ne ho proprio idea."
    mc "Prima, abbiamo incrociato Yuri nel cortile principale, ed è corsa via. Ha reso Monika molto triste questa cosa!"
    mc "Sayori, credimi! Monika si sente davvero male! Vuole aggiustare le cose!"
    mc "Voglio farvi tutti felici, e voglio ricostruire il Club di Letteratura!"
    "Sayori inizia a singhiozzare ancora e ancora, facendo voltare tutti verso di noi."
    mc "Voglio riscrivere il destino di questo mondo, Sayori!"
    "Colpisco il muro più forte che posso mentre sento tutti che mi danno del pazzo, ma non m'importa."
    "Ho promesso a Kotonoha che l'avrei aiutata."
    if persistent.kt_choice1 == 1:
      mc "E ho anche promesso a Monika che tutto sarebbe andato bene, e non mi arrenderò."
    s 3h "Perchè alzi così tanto la voce?"
    s "Ma ancora più importante, perchè non è venuta direttamente lei a dirmelo?"
    s 3w "Può dire qualsiasi cosa lei voglia! Questo però non cambia il fatto che ci abbia uccise!"
    "Afferro le spalle di Sayori e la fisso negli occhi. Sto cercando di trattenere le lacrime. Voglio davvero tanto bene a Sayori, è così importante per me."
    "Non mi piace vederla in quello stato, ho bisogno di aiutarla perchè è {i}mia{/i} amica. Non farò lo stesso errore per due volte di fila."
    mc "Ascolta, Sayori."
    "Sayori finalmente ha i suoi occhi rivolti verso di me, mostrando un espressione davvero preoccupata e spaventata."
    mc "Anche Monika è impaurita... Tutto ciò che voleva era passare del tempo con me. E so che le sue azioni non giustificano questo fatto."
    mc "Ma era disperata; si sentiva sola. Era un mondo inutile per lei..."
    mc "So che sei spaventata e ti capisco, davvero. Fidati, Sayori."
    s "..."
    s 2e "E' la verità?"
    mc "Certo che lo è. Per questo son--"
    play sound cellphone
    window hide(None)
    window auto
    pause 2.0
    "Improvvisamente il mio telefono squilla. E' una chiamata da..."
    "...Kotonoha?"
    mc "Uh... Aspetta."
    s 2k "S-sì."
    stop music fadeout 2.0
    mc "Pronto?"
    kt "{i}[player]?{/i}"
    mc "Sono io. Che succede?"
    kt "{i}Vienei in cortile il prima possibile, abbiamo un {b}grosso{/b} problema!{/i}"
    mc "Okay okay, calmati. Qual è il problema?"
    kt "{i}E' Natsuki!{/i}"
    "Cosa? Oh no..."
    kt "{i}Abbiamo trovato Monika parlare con Yuri, ma è corsa via e Natsuki ha visto cos'è successo.{/i}"
    kt "{i}Natsuki ha provato a caricare verso Monika, ma ho provato a calmarla.{/i}"
    kt "{i}Ho provato a trattenerla, ma mi ha spinto via.{/i}"
    mc "Oh no... Stai bene?"
    kt "{i}Sì, io sto--{/i}"
    kt "{i}Aspetta Natsuki!{/i}"
    kt "{i}Vieni qua! Devo andare.{/i}"
    "..."
    s "[player]? E' successo qualcosa?"
    mc "Sayori, devi venire con me."
    s 2m "Eeehhh?"
    mc "Non c'è tempo per le domande, andiamo."
    show sayori at lhide
    hide sayori
    "Con questo, ci dirigiamo verso il cortile della scuola. Spero solo che Kotonoha riesca a tenere a bada Natsuki."
    scene black
    with wipeleft
    scene bg yard2
    with wipeleft
    "Arriviamo al cortile, e posso già dire dove si trova Natsuki."
    "Si è formato un gruppo nel cortile, e dei capelli argentei scintillanti confermano il mio sospetto. In più, posso già sentire la voce di Natuski."
    show natsuki 2b at l31 zorder 1
    show kotonoha 4bw at l32 zorder 2
    show monika 1f at l33 zorder 3
    "Incrocio gli occhi di Monika realizzando che Kotonoha è tra lei e Natsuki."
    mc "Che sta succedendo qui?"
    n 2k "[player]?"
    n "Kotonoha, lo conosci?"
    kt "..."
    mc "Sì, mi conosce. L'ho portata in questa scuola."
    mc "Giusto, Kotonoha?"
    kt 4bo "S-sì..."
    "Non riesco a fare a meno di notare lo strano comportamento di Kotonoha ogni volta che le parlo."
    if persistent.kt_choice1 == 1:
      "E quella roba del \"è in difficoltà col suo periodo\" ..."
      "In più, ha ignorato anche Monika."
    play music late fadein 2.0
    "Mettendo quel sentimento da parte, fisso i miei occhi su Natsuki. Non sono consapevole di ciò che è successo, ma Kotonoha è abbastanza coraggiosa da fronteggiare Natsuki."
    "Osservando la situazione capisco cos'è successo."
    n 5b "Ti avevo chiesto già prima se la conoscessi, Kotonoha."
    n "Sei così fastidioso, [player]."
    n 4f "Adesso, hai qualcos altro da dire, {i}Monika{/i}?"
    m 1g "Volevo solo parlare con Yuri, Natsuki."
    m "Ma è corsa via quando mi sono avvicinata..."
    m 1p "Giuro di non averle fatto nulla di male!"
    n 2b "Hmph. Non è che non te lo meritassi."
    n "Se non fosse per Kotonoha ti avrei già dato una lezione."
    "Hm, non sta andando affatto bene... Sembra che Yuri sia {i}davvero{/i} spaventata dalla presenza di Monika qui."
    "Ma sono fiero di Kotonoha, ha fatto rimanere calma Natsuki, anche se Natsuki l'ha spinta via."
    "Kotonoha è davvero coraggiosa abbastanza."
    s "Ahem..."
    $ s_name = "Tutti"
    s "Hm?"
    $ s_name = "Sayori"
    show natsuki 2k at t41 zorder 1 
    show kotonoha 7be at t42 zorder 2
    show monika 1f at t43 zorder 3
    show sayori 3c at t44 zorder 4
    s "Natsuki, hai ragione... Monika ha fatto delle cose orribili..."
    s "Ma credo dovresti mostrare un po' di empatia."
    m 2n "Empatia..."
    s 3j "Non stavo parlando con te, Monika!"
    m 2o "..."
    s 3c "Come stavo dicendo..."
    s 3m "Ahhhh!! Non mi ricordo più cosa dovevo dire!"
    "Quello che mi rende felice è vedere Sayori essere... Beh, Sayori. Non è cambiata per niente almeno."
    "Mi rende davvero felice."
    "E beh... Come al solito, Sayori sta cercando di risolvere questo argomento, ma non sta andando molto bene..."
    "Nel senso, Sayori di solito è una ragazza dolce, ma quello sfogo su Monika ha scioccato tutti noi."
    "Tutta la mia attenzione è rivolta verso Sayori e Natsuki."
    show monika at thide
    hide monika
    show kotonoha at thide
    hide kotonoha
    show sayori 2k at t21 zorder 1
    show natsuki 2g at t22 zorder 2
    s "Sono spaventata anche io, Natsuki... E anche se non posso confermare la storia di [player], non posso dire che non stia dicendo la verita..."
    s 2h "Se Monika si sente davvero male e vuole davvero parlare con Yuri, allora... Mi fido..."
    n 2c "Storia? Di quale storia stai parlando?"
    s 2l "Beh, credo sarebbe meglio che sia proprio [player] a raccontartela."
    "Sigh, credo sia il mio turno."
    "Mi volto e guardo Natsuki nei suoi occhi rosa diamante, e lei fissa i suoi occhi su di me."
    mc "Beh... Quindi, ieri ho parlato con Monik--"
    window hide(None)
    window auto
    pause 2.0
    show sayori 2l at t21 zorder 1
    show natsuki 5w at t22 zorder 2
    n "Hmph."
    n "Se avessi voluto che fossi {b}TU{/b} a raccontarmela, l'avrei chiesto a {b}TE{/b}."
    play sound school_ring
    window hide(None)
    window auto
    pause 2.0
    show sayori at thide
    hide sayori
    show natsuki 1b at t11 zorder 1
    n "Andiamo Kotonoha, non c'è niente da fare qui."
    mc "Aspetta, Natsuki!"
    show natsuki at lhide
    hide natsuki
    "Con quello, Natsuki s'incammina verso l'edificio scolastico. Kotonoha mi sta fissando impietrita."
    "Non posso lasciare che finisca così! Devo parlare con Natsuki!"
    "Guardandola passare di fianco a me, le afferro il polso con più decisione che posso, ma spinge via la mia mano e continua a camminare."
    mc "Natsuki!"
    show natsuki 5b at t11 zorder 1
    n "Ugh, cosa? Sei così fastidioso."
    mc "Ma voglio solo--"
    n "Vuoi solo dirmi quando \"male\" si senta Monika? Che si pente veramente di quello che ha fatto?"
    n "Non sono stupida, [player]."
    n "Non pensare neanche che accetterò le sue scuse e mi comporti come se non fosse successo nulla."
    show natsuki at lhide
    hide natsuki
    mc "Ma Natsuki, Monika--!"
    n "Kotonoha, andiamo in classe."
    kt "S-sì..."
    "Kotonoha a quel punto mi guarda come per dirmi \"non preoccuparti, sistemerò io\" e corre via."
    "Dio... Così non va bene..."
    "Monika è ancora in mezzo al cortile e sembra agitata."
    mc "Monika?"
    show monika 1o at t11 zorder 1
    m "..."
    show monika at thide
    hide monika
    "Monika mi ignora e inizia a farsi strada verso il plesso scolastico."
    mc "Monika!"
    "Come parlare al vuoto, il suo fiocco bianco scompare sempre più dal mio campo visivo come si addentra nel corridoio."
    "Non avrebbe potuto concludersi in un modo peggiore..."
    "Così tanti pensieri mi passano nel cervello, perchè non ero là per supportare Kotonoha, perchè non ero in grado di parlare con Natsuki..."
    "Fortunatamente la voce di Sayori mi ha deragliato da questo treno di pensieri."
    show sayori 1l at t11 zorder 1
    s "[player], dobbiamo andare... Ehehe..."
    mc "O-oh! Sì. Andiamo."
    scene black
    with wipeleft
    scene bg yard2
    with wipeleft
    "Mentre io e Sayori ci dirigiamo verso la nostra classe, non riesco a smettere di pensare a Monika."
    "Tutto la sofferenza che sta passando..."
    "La sua sfiducia, che ora aumenterà per via di questa situazione."
    "E anche Natsuki, non è disposta ad accettare le scuse di Monika. E non è che possa biasimarla."
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    "Ero così perso nei miei pensieri che non avevo realizzato che eravamo rientrati nel plesso."
    "Posso vedere Kotonoha e Natsuki parlare davanti alla loro classe."
    "Kotonoha realizza che stavo guardando lei e Natsuki, e mi risponde facendomi un dolce sorriso."
    "Uhhh... Non so cosa stia succedendo con Kotonoha..."
    "Mettendolo da parte, concentro il mio sguardo su Sayori"
    show sayori 1k at t11 zorder 1
    "Sembra chiaramente preoccupata anche lei..."
    "Dovrei ringraziarla per avermi aiutato là fuori."
    mc "Uh, Sayori?"
    s 2g "Hm?"
    mc "Grazie... per avermi aiutato con Natsuki. L'ho davvero apprezzato."
    s 2f "Non è niente [player]. Sono ancora preoccupata del fatto che Monika si trovi qui però..."
    "Già, non la biasimo."
    mc "Sayori."
    s 2k "Hm?"
    "Incrocio gli occhi blu di Sayori mentre metto la mia mano sulla sua spalla."
    mc "Non preoccuparti, non è che io ti possa biasimare per essere spaventata da Monika. Ma credimi..."
    mc "Monika si sente veramente male per quello che ha fatto."
    mc "E beh, hai visto che mi ha ignorato."
    s 1g "S-sì..."
    s "Credi che Monika stia bene?" 
    mc "Ad essere onesti no. Non sta bene."
    mc "Vederla così è {i}davvero{/i} straziante..."
    s 4d "E se la portassimo nella stanza del club?"
    s 4x "Credo che potrebbe sentirsi meglio!"
    "Sayori è ancora la ragazza solare che è sempre stata."
    "Ma conoscendo la situazione attuale... Non credo sia una buona idea."
    mc "Uhm... Non prenderla male Sayori, ma credo che prima debba portare tutti i membri nella stanza del club."
    mc "Poi, credo dovremmo darle del tempo per pensare."
    # that's all
    mc "Non so neanche se sia dell'umore giusto per parlare ora."
    s 1k "..."
    s "Credo tu abbia ragione..."
    s "Ma non possiamo lasciarla soffrire così se si sente davvero male per quello che ha fatto."
    mc "Sì, hai ragione... Ma non possiamo neanche forzarla. Faremo meglio a darle un po' di tempo."
    s 2c "Dormirà a casa tua?"
    mc "Mh... Non lo so. E' rimasta a casa mia stanotte perchè era troppo tardi per lei per tornare a casa."
    s "Oh, capisco..."
    s "Hey [player], sta per iniziare la lezione."
    mc "Oh, già. Entriamo dai."
    scene black
    with wipeleft
    scene bg class_day
    with wipeleft
    "E' passata mezz'ora dall'accaduto in cortile. Le lezione è iniziata già da un po'."
    "Non posso fare a meno di pensare a Kotonoha - Cosa succede se fallisce nel tentativo di portare Natsuki al club?"
    if persistent.kt_choice1 == 0:
      "Sono sicuro che Yuri accetterà le scuse di Monika, lei è solo spaventata."
      "Sayori esita ancora un po' nel credere a Monika, ma nonostante questo vuole aiutarla a sentirsi meglio."
      "E ce lo aspettavamo che Natsuki sarebbe stata la più difficile da convincere comunque..."
      "Ho ancora le mie speranze che possiamo fare qualcosa oggi, ma sono un po' ansioso."
    elif persistent.kt_choice1 == 1:
      "Poi non posso far a meno di pensare a come si è atteggiata Kotonoha prima... Non so cosa le sia successo."
      "Ha provato a dire qualcosa riguardo Yuri a Monika, ma improvvisamente si è bloccata."
      "Ha detto {i}qualcosa{/i}, ma non sono stato in grado di sentirla."
      "Devo parlarle ed essere sicuro che stia bene. Devo."
    else:
      "Nonostante il fatto che ho promesso a Monika che tutto sarebbe andato bene, niente sta andando bene... Sta andando tutto {i}molto{/i} male."
      "Yuri corre via ogni volta che vede Monika e Natsuki l'ha quasi colpita. Niente va bene."
      "Non riesco a smettere di pensare all'espressione di Monika... Mi ha fatto venire una fitta al cuore."
      "Non so cosa fare."
    if sheet == 0:
      "Senza menzionare quando Kotonoha ha iniziato a piangere quando ha visto il secondo foglio che il preside le ha dato."
      "Qualcosa l'ha decisamente disturbata."
      "So di essere stato maleducato, ma io mi preoccupo per lei. Dopotutto, le devo più che del semplice denaro."
      "Mi piace alla fine dei conti. Come amica, ovviamente."
    else:
      "Mi è sembrata sorpresa quando ha visto il secondo foglio. Non ho idea di cosa lei abbia visto per farla reagire così."
      "Decido di non chiedere però finché il preside e Monika fossero stati lì."
      "Anche se non la conosco abbastanza, sono davvero preoccupato per lei. Lei è stata abbastanza paziente con me nonostante il mio comportamento."
    "Credo che inviterò Monika per andare da qualche parte, poi di sera andrò da Kotonoha."
    "Spero solo che tutto vada bene."
    "Tutti hanno avuto problemi e preoccupazioni, ma c'è una cosa che non capisco... Perchè nascondercelo?"
    play sound school_ring
    "Ho una teoria. Anche lei è depressa, e lo sta mettendo da parte come per non farlo pesare su di noi."
    "Non mi conosce abbastanza; Dovrebbe sapere che l'aiuterò anche se non vuole il mio aiuto. Lo farò comunque."
    show sayori 2l at t11 zorder 1
    s "Uh... [player], la lezione è finita... Ehehe."
        mc "Ah--"
    "Mi sono davvero perso di nuovo nei miei pensieri?"
    mc "S-sì, andiamo."
    show sayori at thide
    hide sayori
    scene bg corridor
    with wipeleft
    show sayori 1h at t11 zorder 1
    s "Stavi pensando a Monika, vero [player]?"
    mc "Già... Puoi dirlo."
    play music nday fadein 2.0
    s 1c "Quella ragazza con i capelli argentei... Chi è?"
    mc "Ah, beh... E' un'amica di Monika."
    s "Capisco."
    s "Quindi, la conosci?"
    "Sayori è di fronte a me, mi sta facendo un sacco di domande su Kotonoha."
    mc "Sì, la conosco."
    s 2c "Perchè non sta indossando la nostra uniforme scolastica?"
    mc "Viene da un'altra scuola."
    s 2a "Oh! Questo spiega il suo accento e la sua uniforme!"
    s 3a "Poi è carina, vero?"
    mc "Uh... Sì, è vero."
    s 4x "Ehehe~"
    s 4c "Eeeeee... Riguardo a Monika?"
    mc "Eh? Cosa intendi?"
    s "Hai un piano per tirarla su?"
    mc "Hm... Ho paura di no... Me ne verrò fuori con qualcosa eventualmente."
    s 2x "Okay! E cosa farai con Yuri?"
    show sayori 2a at t11 zorder 1
    mc "{i}*sigh*{/i} Non lo so..."
    mc "La natura di Yuri la rende difficile da convinvere."
    mc "Penso che le parlerò io direttamente."
    s 2d "Beh... Spero che vada tutto bene. Vorrei parlare con Monika..."
    stop music fadeout 2.0
    s 1h "Sono un po' spaventata..."
    mc "Sayori, credimi su questo. Se mi aiuterai con Natsuki, prometto che renderemo tutti felici."
    mc "Te lo prometto."
    s "Okay... Ci proverò, [player]."
    "Con questo, ci dirigiamo verso la prossima classe. Ho capito, sarà una sfida convincere Yuri..."
    "Ma non posso arrendermi proprio ora. Non posso lasciare che il lavoro di Kotonoha vada sprecato."
    "L'unica cosa che devo fare è parlare con Yuri. Quello sarà facile. Penso."
    scene black
    with dissolve_scene_full
    show text("{size=100}{color=#6debab}{b}Nel mentre{/b}{/size}{/color}\n{size=60}nella classe di Kotonoha.{/size}"):
      yalign 0.5
    with dissolve_scene_full
    pause 2.0
    scene bg kt_classroom
    with dissolve_scene_full
    show natsuki 1g at t11 zorder 1
    "La lezione è ormai finita, e un'ora è passata dal... \"ritrovo\" tra Monika e Natsuki."
    "Devo essere onesta... Non mi aspettavo di tenere il passo di Natsuki quando è andata incontro a Monika, ma la mia altezza mi aiuta a correre più veloce."
    play music tnatsuki_c fadein 2.0
    "La cosa peggiore è che [player] non era lì ad assistermi... Ma fortunatamente sono riuscita a calmarla. Ma come mi aspettavo, Natsuki mi ha spinta via. E' più forte di quel che la sua figura può far sembrare."
    "Mi sono anche slogata il polso quando ho provato a coprirmi la faccia dalla caduta."
    "Ho parlato a Natsuki quando la lezione è finita, ed era abbastanza incazzata."
    n 4b "Quindi, perchè mi hai fermato?"
    kt "Ugh..."
    "Guardo altrove cercando di evitare il suo sguardo. Poi, incrocio le gambe."
    kt "Perchè... Non dovresti aggredire a caso le altre persone..."
    n 5e "Hmph."
    n "Probabilmente non diresti lo stesso se sapessi le cose che ha fatto. Alle {i}sue{/i} amiche."
    show natsuki 1v at h11 zorder 1
    n "Non la perdonerò mai!"
    "Mi comporto come se non sapessi di cosa sta parlando. Mi volto verso di lei."
    kt "Cosa ha fatto, allora?"
    n 1e "Non è qualcosa che tu dovresti sapere."
    kt "Uhh... Allora la odii senza una ragione?"
    n 1p "N-no! Io-io..."
    n "Ugh, stupida!"
    kt "Heh."
    "Le lancio il mio solito sguardo compiaciuto per rassicurarla che non mi sono offesa."
    stop music fadeout 2.0
    "Alla fine, Natsuki si decise a parlare."
    n 5u "Beh..."
    play music t9 fadein 2.0
    n "La verità è che... Ha rovinato tutto quello che avevo..."
    n "Il Club di Letteratura era un posto veramente importante per me."
    n 1q "Mi divertivo a passare il tempo con i miei amici..."
    n "Lo sentivo come un posto dove mi sentivo al sicuro. L'unico posto dove potevo essere me stessa in cui nessuno si prendeva gioco di me."
    "Sul punto di piangere, Natsuki trattiene le lacrime e continua a parlare."
    n 12b "Mi divertivo a parlare con i miei amici... E avrei voluto ritornare al club."
    n "Ma Monika..."
    kt "Monika?"
    n 1s "La ragazza di cui sto parlando."
    "Kotonoha, devi segnarti una nota mentale: \"non fare domande così stupide in situazioni del genere\"."
    n "Dunque... Questo è tutto quello che posso ricordare."
    n 12a "A quel punto anche Yuri cominciava a comportarsi male verso di me."
    n "In più Monika aveva scarsa considerazione del suo comportamento."
    n "Ho anche iniziato a pensare che fosse Monika la responsabile del comportamento di Yuri da... Pazza."
    kt "Come fa \"Monika\" ad essere la responsabile per il comportamento di un'altra persona?"
    "Metto le mani sul banco, e guardo Natsuki con un espressione curiosa."
    "Riesco a vedere gli occhi di Natsuki espandersi mentre lo faccio; sospira e poi inizia di nuovo a parlare."
    n 2c "Dunque... Yuri è davvero una persona timida, ma è molto gentile."
    n 12a "Non ricordo cosa sia successo a Sayori, la ragazza con il fiocco rosso in testa."
    n "Ricordo solo il comportamento di Yuri, e che Monika era poco interessata alla cosa."
    n 2q "Pensavo che Monika stesse dicendo delle cose brutte su di me a Yuri... Ma i miei sospetti vennero confermati quando Yuri iniziò a trattarmi peggio e peggio ancora."
    n "Alla fine... Ho trovato [player] e Yuri nella stanza del club. Yuri aveva 3 segni di accoltellamento e un coltello da cucina ricoperto di sangue e [player] la stava fissando, immobile..."
    "Natsuki allora cominciò a singhiozzare in silenzio."
    n 42g "N-non sono stata in grado di trattenermi dal vomitare... E improvvisamente mi sono trovata in un vuoto nero."
    "Devo finirla... Natsuki merita di sapere la verità! Ma... Andrà bene se glielo dico?"
    "Incasinerò di nuovo lo scrpt se le dicessi cos'è in realtà questo mondo?"
    "Cosa accadrebbe se succedesse?"
    "Provo a rispondere a questa domanda nella mia testa, ma Natsuki sembra soffrire davvero tanto... Non posso lasciarla in questo stato!"
    "Ma se glielo dico, potrei distruggere tutto di nuovo..."
    "Okay, ho fatto la mia scelta."
    kt "Hey, Natsuki..."
    n 2q "Hm?"
    "Gli occhi di Natsuki fissano i miei. Ora o mai più, Kotonoha."
    "Anche se mi farà ancora provare dolore, lei deve sapere cos'è questo mondo!"
    "Mettendo le mani sul mio petto, mi decido a parlare."
    menu:
      kt "Volevo solo sapere se..."
      "--sapessi tutto.":
        stop music fadeout 2.0
        $ n_choice = 0
      "--hai scritto i compiti.":
        $ n_choice = 1
    if n_choice == 0:
      kt "Sai tutto?"
      n 2m "Cosa?"
      "Natsuki mi sta guardando molto confusa, ma non posso fermarmi ora. Ho fatto la mia scelta e non voglio tornare indietro."
      "Sospirando a me stessa e posizionando la mano dove si trova il mio cuore, mi preparo per cosa farò ora."
      kt "Sai... La verità riguardo a questo mondo?"
      n "Di cosa stai parlando, Kotonoha?"
      kt "Natsuki, sai di cosa sto parlando?"
      n 1m "Beh... Credo di sì."
      "Bene! Sarà facile allora!"
      n "Non è che io sia una cattiva studentessa o che cosa, i miei voti sono... Buoni."
      kt "{i}*sigh*{/i}"
      kt "Natsuki, {w=0.5}sai che cos'è veramente questo mo--"
      pause 2.0
      play music hb
      show black zorder 100:
        alpha 0.5
        parallel:
          0.36
          alpha 0.5
          repeat
        parallel:
          0.49
          alpha 0.5
          repeat
        parallel:
          0.49
          alpha 0.475
          repeat
      with char_fade
      show layer master at heartbeat
      window hide(None)
      window auto
      if persistent.kt_choice1 == 1:
        pause 4.0
      else:
        pause 7.40
      if persistent.kt_choice1 == 1:
        mc_b "Ti ho detto di no, Kotonoha."
        mc_b "La prossima volta ti punirò."
        mc_b "Ci vediamo stanotte."
      $ n_name = "Natsuki"
      hide black
      show layer master at thide
      hide layer master
      stop music
      kt "Gh--"
      $ style.say_dialogue = style.edited
      kt "Haaaaaaaah... {w=0.5}Haaaaaaaah...{w=0.5}Haaaaaaaah..."
      $ style.say_dialogue = style.normal
      n "Kotonoha? Stai bene?"
      kt "Gh-- S-{w=0.5}sì... {w=0.5}Sto... {w=0.5}bene--"
      "Un'altra volta non mi sono accorta di essere caduta sulle mie ginocchia."
    else:
      kt "V-{w=0.5}volevo solo sapere se avessi scritto i compiti di oggi. Sono abbastanza lenta e non ho... Hehe."
      kt "Potresti farmi copiare i tuoi?"
      n 5k "Cosa?"
      "Natsuki è ancora esitante, guardandomi con un espressione confusa. Poi, prende il suo quaderno e me lo allunga."
      n 2k "Certo... Ecco."
      "Afferro poi il quaderno dalle sue mani. Apro il mio quaderno in una pagina vuota e inizio a scrivere."
      scene bg notebook
      with dissolve_scene_full
      "Come apro il quadenro di Natsuki, posso vederla guardarmi mentre inizio a scrivere."
      show kt_homework1 zorder 50 
      with ImageDissolve("mod_assets/wipeleft.png", 4.0, alpha=False)
      n "Kotonoha."
      kt "Hm?"
      "Sollevo la testa per guardarla."
      n "E' l'unica cosa che ti serve?"
      kt "Uh... Sì. Perchè?"
      n "Lo vedo nei tuoi occhi."
      "Ignoro il commento e ricomincio a scrivere."
      show kt_homework2
      with ImageDissolve("mod_assets/wipeleft.png", 2.0, alpha=False)
      show kt_homework3
      with ImageDissolve("mod_assets/wipeleft.png", 2.0, alpha=False)
      show kt_homework4
      with ImageDissolve("mod_assets/wipeleft.png", 2.0, alpha=False)
      "Sento Natsuki parlarmi di nuovo, questa volta la sua voce sembra più calma."
      n "Kotonoha, stai bene?"
      kt "Ah--"
      kt "Te l'ho già detto, Natsuki. Sto... Bene."
      "Natsuki si piega verso di me, con la sua faccia molto vicina alla mia."
      n "No, non stai bene, Kotonoha!"
      "Ignoro il fatto che la sua faccia sia a pochi centimetri dalla mia e ritorno a scrivere."
      show kt_homework5
      with ImageDissolve("mod_assets/wipeleft.png", 2.0, alpha=False)
      show kt_homework6
      with ImageDissolve("mod_assets/wipeleft.png", 2.0, alpha=False)
      show kt_jp_t1
      with ImageDissolve("mod_assets/wipeleft.png", 2.0, alpha=False)
      "Una volta finito di copiare gli appunti, chiudo il mio quaderno e ridò a Natsuki il suo."
      scene bg kt_classroom
      with dissolve_scene_full
      show natsuki 1n at face with char_fade
      n "Quindi?"
      kt "Ugh..."
      show natsuki 1n at t11
      with None
    if n_choice == 0:
      "{i}E' ora di finirla!{/i}"
      n 1n "Kotonoha..."
      kt "Ah?"
      "Natsuki apre le sue braccia, invitandomi ad abbracciarla."
      scene black
      with dissolve_scene_full
      play music goodbye fadein 2.0
      "E' un po' bizzarro che... Beh, Natsuki non sia così alta, ma essere sulle mie ginocchia facilita la cosa."
      "SDopo alcuni minuti, Natsuki finalmente parla."
      n "Come ti ho detto Kotonoha, non sono stupida."
      n "Stai bene?"
      "Importa davvero se sto bene e se è successo qualcosa? Non che io possa dire qualcosa in ogni caso."
      "Gli occhi di Natsuki si calmano; mi sta guardando veramente preoccupata. Penso tra me e me per un po' e poi le dò una risposta."
      kt "S-{w=0.5}sì Natsuki, sto bene. Sono solo un po' frastornata perchè sono affamata ora."
      "Vedo immediatamente Natsuki guardarmi ancor più preoccupata."
      "Come provo a rialzarmi, Natsuki improvvisamente mi ferma, scuotendo gentilmente la testa."
      "Poi mi abbraccia di nuovo e ricomincia a parlare."
      n "..."
      n "I tuoi genitori ti danno da mangiare?"
      kt "Beh... Attualmente vivo da sola, mi sono solo dimenticata di mangiare qualcosa prima di venire. Altrimenti sarei stata {i}un po'{/i} in ritardo per scuola."
      n "Non dovresti dimenticarti..."
      "Detto questo, Natsukimi lascia andare e mi aiuta ad alzarmi."
      stop music fadeout 2.0
      scene bg kt_classroom
      with dissolve_scene_full
      "Quando mi alzo realizzo che tutti ci stanno guardando. Non m'importa di loro, quindi scatto verso di loro."
      kt "Cosa? Avete perso qualcosa?"
      "Come mi aspettavo, \"fingevano\" solo di non aver visto niente e ritornarono tutti alle loro attività."
      play music nday fadein 2.0
      show natsuki 3m at t11 zorder 1
      n "Quindi... Starai bene?"
      kt "Sì, non preoccuparti. Sto già meglio, vedi?"
      "Le rivolgo un sorriso. Ma questa volta uno {b}VERO{/b}."
      kt "FInita la lezione, ti va di mangiare qualcosa insieme?"
      n 1u "Non ho i soldi per il cibo..."
      kt "Non preoccuparti! Posso prestarti i miei!"
      n 5u "N-no."
      n "Aspetterò fino a cena. Grazie comunque..."
      "Natsuki sembra abbastanza sorpresa del mio invito, ma nonostante questo ha rifiutato..."
      "Sembra che [player_b] non mi ha dato informazioni sufficienti sulla situazione di questa ragazza. Dovrò scoprirlo da sola."
      stop music fadeout 2.0
      scene black
      with dissolve_scene_full
    else:
      "Natsuki si guarda indietro ancora preoccupata."
      show natsuki at thide
      hide natsuki
      "Quando prende il suo quaderno, fa mezzo giro verso di me; mette il suo quaderno nel suo zaino e si gira di nuovo per guardarmi."
      show natsuki 1n at t11 zorder 1
      n "Kotonoha, ti stai comportando in modo strano da... beh..."
      n 2m "--quando è successo \"quello\". Stai bene?"
      kt "{i}*sigh*{/i}"
      kt "Sto bene Natsuki, te lo prometto."
      kt "Sono solo un po' affamata. Non ho mangiato stamattina, avrei fatto tardi a scuola."
      n 2n "..."
      n 2m "I tuoi genitori ti danno da mangiare?"
      kt "Beh... Attualmente vivo da sola, mi sono solo scordata di mangiare. Niente di ché."
      "Non so cosa stia passando Natsuki, ma spero non sia male come credo."
      "Ritornando al \"mondo reale\", la voce di Natsuki rieccheggia ancora."
      n 3m "Non scordarti la prossima volta, okay?"
      kt "Okay, non posso promettertelo però."
      "Sorridendomi, Natsuki risponde."
      stop music fadeout 2.0
      show natsuki 1l at h11 zorder 1
      n "Okay!"
      play sound school_ring
      window hide(None)
      window auto
      pause 3.50
      n 1z "La prossima lezione sta per cominciare, andiamo?"
      kt "Certo. Non che abbiamo altra scelta in ogni caso."
      n 1l "Hehehe~"
      "Con questo, lasciamo l'aula e ci incamminiamo verso la prossima lezione."
      scene black
      with wipeleft
      scene bg corridor
      with wipeleft
      n "Comunque, Kotonoha..."
      stop music fadeout 2.0
      kt "Yeah?"
      "Natsuki solleva la testa per guardarmi. E' molto più bassa di come dovrebbe essere alla sua età."
      show natsuki 1k at t11 zorder 1
      n "Quando ti sei presentata, mi ricordo che hai detto che la tua è qui vicino... Dove vivi esattamente?"
      "..."
      "Dannazione, solita fortuna! DOvrei dirle dove vivo?"
      "Se lo facessi, potrei avvicinarmi a Natsuki e lasciare che [player] faccia la sua parte con Sayori."
      "Sorridendo, le do una risposta."
      scene black
      with wipeleft
      scene bg corridor
      with wipeleft
      "Mentre andavamo in classe per la prossima lezione, ho detto a Natsuki l'indirizzo del mio hotel. Le ho detto che può venire quando vuole. Con esitazione ha accettato."
      "Qualunque cosa Natsuki stia passando, è qualcosa che la sta facendo soffrire. Devo aiutarla... Una ragazza così gentile non merita qualsiasi cosa stia passando."
    scene bg class_day
    with dissolve_scene_full
    "E' passato un po' dal... \"ritrovo\" di Monika e Natsuki."
    "Ora sono un po' preoccupato per Yuri... Si sta rifiutando di ascoltare Monika, e se Monika non sarà in grado di fare qualcosa con lei, dovrò intervenire io."
    "Non voglio stressarla. Sappiamo già quanto sia fuori dal normale questa situazione."
    show sayori 1a at t11 zorder 1
    "Sayori ha promesso di far sentire Monika meglio, e questo mi ha reso molto felice. Almeno so che sarà dalla mia parte."
    "Anche se è ancora un po' impaurita ad avere Monika attorno..."
    show sayori at thide
    hide sayori
    "Come non prestavo attenzione alla lezione, il professore mi chiama."
    $ n_name = "Professore"
    n "[player], sei attento alla lezione?"
    mc "Ah--"
    mc "Sì."
    n "Allora potresti rispondere alla domanda che ho posto."
    mc "..."
    n "{i}*sigh*{/i}"
    n "Se non vuoi più compiti, devi stare attento alla lezione. Ultimo avvertimento."
    mc "S-{w=0.5}sì. Mi scusi."
    "Poi, non intenzionalmente, ho guardato attraverso la finestra, vedendo degli scintillanti capelli viola."
    window hide(None)
    window auto
    pause 2.0
    "Subito non ero sicuro se fosse Yuri, ma poi ho visto il suo fermaglio per capelli."
    "E' la mia occasione!"
    mc "Professore, potrei andare in bagno?"
    n "Certo, non metterci troppo."
    "Mi alzo dalla sedia dirigendomi verso la porta della classe, poi sento Sayori sussurarmi qualcosa."
    s "{alpha=0.58}Non essere troppo insistente, [player]. Ehehe~{/alpha}"
    "Annuisco e apro la porta."
    play sound closet_open
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    play sound closet_close
    "Chiudo la porta, facendomi strada verso \"il bagno\"."
    "Il rumore delle mie scarpe rieccheggia ad ogni passo che faccio. Guardo intorno per cercare Yuri, ma sembra scomparsa."
    window hide(None)
    window auto
    pause 2.0
    # proofreading from here
    "..."
    "Ahhh... DDove sei, Yuri?"
    "Se non la trovo al più prest, non sarò in grado di portarla alla stanza del club oggi."
    scene black
    with wipeleft
    scene bg stairs
    with wipeleft
    "Riesco a sentire i suoi passi una volta che mi trovo alla fine delle scalinate, camminando attraverso i corridoi i miei occhi intravedono quei capelli viola di nuovo."
    mc "Yuri!"
    show yuri 1n at h11 zorder 1
    y "Ah--!"
    "Yuri con un espressione nervosa, si gira a guardarmi."
    y "[player]?"
    mc "Sì. Sono io."
    y 1q "O-{w=0.5}Oh! Scusa, {w=0.5}S... {w=0.5}Sono in ritardo per la lezione di chimica--"
    "Dicendo questo, frettolosamente scende un'altra rampa di scale."
    show yuri at lhide
    hide yuri
    "Sono curioso di sapere se davvero ha lezione contando il fatto che le lezioni sono già cominciate. Devo essere sicuro che stia bene."
    "Nel tentativo di raggiungere Yuri, corro giù per le scale il più velocemente possibile."
    "Yuri nota che la sto seguendo, quindi inizia a rallentare, quasi per farsì che la raggiungessi."
    show yuri 1o at l11 zorder 1
    mc "Yuri!"
    "Yuri si gira a guardarmi."
    y "S-sì?"
    mc "Um... {w=0.5}E' tutto apposto?"
    y "S-sì... Perchè non dovrei?"
    mc "Beh, sei corsa via quando hai visto Monika--"
    y 2p "P-perchè?"
    mc "Huh? Perchè, cosa?"
    y "Perchè...?"
    y "Non ti ricordi cosa ci ha fatto Monika, vero?"
    "Yuri smette completamente di camminare per lasciarmi andare davanti a lei, poi si gira verso la finistra e guarda fuori."
    show yuri at thide
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    play music t9 fadein 2.0
    y "Monika ha fatto del male a tutte noi..."
    y "Come ha fatto a ritornare? Riesco a malapena a ricordare cos'è successo prima..."
    show yuri 1v at face_window zorder 1:
      alpha 0.42
    with char_fade
    "Vedo un espressione triste e piena di dolore sulla faccia di Yuri riflessa nella finestra."
    y "Non ricordo neanche cosa mi è successo... Ma minimamnte riesco a ricordarmi cosa mi ha fatto fare Monika."
    "Girando debolmente la testa, inizia a guardarmi attraverso la finestra."
    y 2t "Ti ricordi, [player]?"
    "La afferro per le spalle e la giro perchè mi guardi, prendo un respiro profondo e inizio a parlare."
    show yuri 2t at t11
    with None
    mc "Sì, mi ricordo. Ma voglio solo che mi ascolti... Monika è profondamente pentita per quello che ha fatto!"
    mc "Capisco che tu sia spaventata da Monika e va bene, hai le tue ragioni per essere spaventata dopotutto."
    mc "Sono anche consapevole che il suo desiderio di raggiunger{i}mi{/i} le ha fatto fare cose orribili a tutte voi... Ma ti giuro che Monika è cambiata, Yuri."
    y "[player]..."
    mc "Sì?"
    y 2g "--stai mentendo."
    mc "Yuri credimi! {nw=0.5}Monika--"
    y 2k "Scusami [player], ma nessuno rimpiange le sue scelte così velocemente."
    y "Qualsiasi cosa Monika abbia fatto... Era tutto sbagliato."
    mc "Dunque, sai che Monika è quella che... Beh, sai... \"quello\"?"
    y 1j "Beh, sì mettila così... Non riesco ad affermarlo neanch'io però."
    y 3v "L'ultima cosa che ricordo è la dolora sensazione di un coltello che passa attraverso il mio stomaco e il petto..."
    y "Te lo ricordi [player]?"
    mc "{i}*sigh*{/i}"
    mc "Sì, me lo ricordo."
    "..."
    show yuri 2e at t11 zorder 2
    "E se avesse ragione? Come potrebbe una persona non avere rimorsi così velocemente? E' possibile?"
    show yuri 2o at t11 zorder 1
    "No [player]! Non puoi pensare così... Il pianto di Monika quando eravamo nella stanza nello spazio sembrava essere sincero..."
    "La sua preoccupazione per Yuri che è corsa via stamattina quando ha provato a parlarle sembrava anche quella sincera..."
    "Credo veramente che Monika si senta male per quello che ha fatto! Voglio davvero che tutti ascoltino le scuse di Monika."
    play sound steps_st
    window hide(None)
    window auto
    pause 3.5
    y 3n "Ah--"
    show yuri 3n at t21 zorder 1
    show monika 2f at t22 zorder 2
    m "Uhm... Ciao Yuri..."
    "Quei passi che ho sentito arrivare da dietro di me appartengono a Monika, apparentemente sta saltando la lezione ora."
    "Ancora, Monika e Yuri si incontrano. Yuri è un po' spaventata, ovviamente."
    mc "Monika? Cosa ci fai qui?"
    m 2f "Beh, mi sto prendendo una piccola pausa dalle lezioni di oggi..."
    m "Voi due invece? C'è una ragione per cui siate fuori dalla vostra classe?"
    mc "Beh, {w=0.5}Volevo solo--"
    "Come inizio a dare una spiegazione a Monika, Yuri si nasconde dietro di me, appoggiando il suo petto sulla mia schiena."
    show yuri at thide
    hide yuri
    show monika 2f at t11 zorder 1
    "Sarà un giorno moooooolto lungo questo..."
    "Sono consapevole che... Le tette di Yuri siano appoggiate sulla mia schiena, ma provo a ricompormi e do a Monika una spiegazione."
    mc "In realtà stavo andando al bagno. Ma ho trovato Yuri sulle scale."
    m 2p "E tu, Yuri?"
    show yuri 3o at t21 zorder 2
    show monika 2f at t22 zorder 1
    y "S-{w=0.5}Stavo andando anche io al bagno."
    m 1l "Ahaha!~ Capisco..."
    y 1g "Beh... Ora devo andare."
    show yuri at thide
    hide yuri
    "Yuri prova ancora una volta ad andarsene ma la afferro per il polso, non permettendole di farlo."
    "Yuri allora rinuncia ad andar via, ma ora è ancora più spaventata."
    show yuri 1n at h21 zorder 1
    y "C-{w=0.5}cosa? [player]?!"
    mc "Yuri, per favore ascolta... Ti prego! Ascoltala! Solo... Lascia che Monika ti parli."
    mc "Va bene se non vuoi ora, possiamo parlare durante la ricreazione."
    y 1o "..."
    y "Okay [player]..."
    "Come Yuri accetta, Monika è in piedi di fronte a lei. Sospira e inizia a parlare."
    m 1o "Yuri... So che vi ho fatto a tutte del male..."
    m "Sono ben consapevole che sei anche spaventata da me."
    m "Ma, sai... Ora realizzo i gravi errori che ho fatto per il mio egoismo, sono veramente dispiaciuta di avervi cancellate tutte."
    m 4p "Reale o no, questo mondo è la mia casa. Questo mondo sarà la mia casa per sempre."
    y 2o "Ho solo una domanda..."
    m "Sì?"
    y "Hai...il controllo di questo mondo?"
    y "Perchè ci hai fatto del male? Perchè mi hai costretto... ad uccidermi?"
    y "Poi Sayori? Le hai già parlato?"
    mc "Woah woah, rallenta Yuri. Lasciale rispondere una domanda alla volta."
    m 2m "E' tutto okay [player]. Merita delle risposte, è quello di cui abbiamo parlato la scorsa notte, ricordi?"
    "Monika abbassa la testa e incrocia lo sguardo col terreno prima di dare la risposta a Yuri."
    "Monika poi si ricompone, sospira e guarda Yuri."
    m 1n "Allora... Ho sì il \"controllo\" come hai detto tu, ma il mio potere ora è limitato. E' per questo che siete diventate pazze e avete iniziato a comportarvi male."
    m "Essere così potenti mi ha costretto a fare tutto quello che ho fatto... E me ne pento veramente di avervi danneggiato tutte!"
    m "L'unica cosa che ho ottenuto è stato che {i}qualcuno{/i} ha cencellato anche me."
    m "Sono ben consapevole di aver provato a raggiungere {i}qualcuno{/i} che sapevo di non poter raggiungere... Non importa cosa facevo, non ci sarei mai arrivata."
    m 3l "Nonostante questo, so che \"qualcuno\" vuole darmi una seconda possibilità per mostrare quanto male mi senta..."
    m "--So che ci stanno guardando da qualche parte, ed è l'unica cosa che ho bisogno di sapere. Yuri, siete tutte mie amiche. Ti considero davvero come un'amica preziosa per me."
    show yuri 1e at t21 zorder 1
    "Mentre Monika prende un respiro profondo, Yuri inizia a lasciarsi dal mio braccio."
    "Sembra essersi calmata dopo che Monika le ha dato le spiegazioni. Una volta che Monika si ricompone, Yuri inizia a parlare."
    y 3n "C-{w=0.5}come c'è \"qualcuno\" che ci guarda?! Di cosa stai parlando?!"
    m 2n "E' un po' difficile da spiegare."
    m 2p "{w=0.5}Nessuno di voi effettivamente è morto. Non potevo sopportare il pensiero di sbarazzarmi di tutte voi..."
    m 2q "Voi ragazze siete mie amiche dopotutto..."
    y 1g "Monika..."
    m "Hm?"
    "Yuri sospira quando mette insieme i suoi pensieri e poi inizia a parlare."
    y 1h "E' vero?"
    m 2g "Huh?"
    y 2q "Mi consideri veramene una tua amica?"
    m 2n "Certo Yuri. Sei una mia buona amica."
    y 1v "M-{w=0.5}ma se è davvero così, {w=0,5} perchè ci hai fatto del male?"
    y 2u "Non fai del male alle tue amiche come..."
    m "{i}*sigh*{/i}"
    m "Sì... Lo so. Ma è per questo che sono--"
    play sound school_ring
    window hide(None)
    window auto
    pause 3.5
    y 2w "{i}*sigh*{/i}"
    "Senza dire un'altra parola, Yuri scuote gentilmente la mano, per farmi segno di lasciarle andare il polso."
    show yuri at thide
    hide yuri
    show monika at thide
    hide monika
    "Una volta che l'ho fatto, Yuri si volta e si dirige verso il cortile davanti."
    mc "Yuri..."
    "Yuri smette di camminare e si gira verso di me."
    show yuri 1f at t11 zorder 1
    y "Hm?"
    mc "Ti va di venire al club oggi, finita la scuola?"
    y 1g "Perchè? Il club in ogni caso non esiste più."
    mc "Voglio presentarvi tutte a qualcuno."
    show yuri 1g at t21 zorder 1
    show monika 2g at t22 zorder 2
    m 2g "E vorrei anche che ascoltaste tutto quello che ho da dire."
    m "Non voglio davvero perdere la vostra amicizia."
    "Apparendo esitante, Yuri rivolge lo sguardo altrove. Poi mi guarda di nuovo."
    y 2f "Verranno tutti?"
    mc "Beh, stiamo cercando di riunire tutti. Sayori verrà di sicuro."
    y "E Sayori?"
    m 1g "Non lo sappiamo ancora."
    "Yuri annuisce."
    y 3q "O-{w=0.5}okay. Ci sarò."
    "Con questo, Yuri si incammina verso il cortile principale."
    show yuri at rhide
    hide yuri
    show monika 1g at t11 zorder 1
    "Gurado Monika. Ora posso dire che sembra star bene."
    mc "Monika? Ti senti meglio?"
    stop music fadeout 2.0
    m 1n "Oh! {w=0.5}S-sì, sto meglio!"
    "Ritornando in sé stessa, Monika risponde mentre sorride un po' nervosamente."
    "Beh, penso sia andata meglio di come mi aspettassi. Yuri verrà alla stanza del club dopotutto."
    "Credo che Sayori verrà, ma nonostante questo sembrava essere ancora spaventata."
    m 2l "Hey, [player]?"
    mc "Sì?"
    m 1k "Vorresti pranzare con me?"
    mc "Beh... Certo. Andiamo nel cortile dietro?"
    m "Sì! Andiamo~"
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    play music nday fadein 2.0
    "Monika ha pensato che sarebbe stata una buona idea pranzare dietro a scuola."
    "Nonostante la sua espressione triste, noto che si è calmata un pochino, e questa cosa mi mette sollievo."
    if persistent.kt_choice1 == 0:
      "Credo che l'invito accettato da Yuri sia la cosa che la tranquillizza di più ora."
      "Dopotutto, Kotonoha non si è sbagliata su Yuri... Come se fosse già consapevole dell'amicizia tra lei e Monika."
      "Credo sia un po' stupido pensare che Kotonoha lo sapesse già... E' venuta fuori da chissà dove."
      "Sai cosa? Kotonoha è un po' misteriosa, ma so che non dovrei pensar così. Questo mondo è ritornato per merito suo dopotutto."
    elif persistent.kt_choice1 == 1:
      "Sono anche più sollevato che Sayori si sia offerta per aiutare Monika a sentirsi meglio."
      "....anche se è ancora un po' dubbiosa del rimorso di Monika,ma sono sicurissimo che possiamo superarlo questo."
      "E nonostante Yuri sia ancora spaventata, è disposta comunque a venire alla stanza del club dopo scuola"
      "Dobbiamo solo tenere in considerazione di far accettare a tutti Monika di nuovo, ma sono ben consapevole che non sarà così semplice."
    else:
      "Non per menzionare quanto Kotonoha sia stata utile per tutto questo tempo."
      "Oserei dire che urlare a Monika era quello che aveva bisogno di sentire."
      "Beh... Credo che Monika sia stata un po' pessimista."
    "Perso nei miei pensieri e ignorando cosa c'era davanti a me, prendo contro ad una piccola ragazza coi capelli arancioni."
    "Lei lascia cadere i suoi libri a terra."
    $ mi_name = "???"
    show mio 2j at t11 zorder 1
    mi "Oh, no! Mi dispiace!"
    mc "Ah, non preoccuparti... E' colpa mia, non stavo prestando attenzione. Aspetta, ti aiuto a prendere le tue cose."
    show mio at thide
    hide mio
    "Chiedo a Monika di aspettarmi, lei annuisce."
    mc "Mi dispiace di aver fatto cadere le tue cose, scusa."
    mi "Oh, b-{w=0.5}beh... Non preoccuparti! Lascia stare."
    "Mi volto verso di lei mentre raccolgo i suoi quaderni. Non posso fare a meno di pensare a quanto Yuri abbia parlato gentilmente prima."
    mc "..."
    "Come raccolgo i suoi libri, vedo un libro che spicca più degli altri: un libro di Cultura Giapponese."
    "Lei solleva la testa e mi lancia uno sguardo preoccupato."
    mi "Ahh... E' successo qualcosa?"
    mc "Oh! No, questo libro risalta parecchio però."
    show mio 1c at t11 zorder 1
    mi "Oh! già, questo è un libro di Letteratura Giapponese, sono un po' appassionata di Letteratura Giapponese."
    mi 1e "Mi piace molto lo stile di poesia Giapponese!"
    mc "Ah, già..."
    "Potrebbe pensare che io sia un morto se resto qui a parlare di cose con cui non sono familiare."
    "Allungandole i libri, la guardo negli occhi."
    mc "Beh, {w=0.5}se sei interessata e non sei ancora dentro ad un club, {w=0.5}potresti venire al club di letteratura e--"
    m "[player], non dovremmo avviarci? Non avremo abbastanza tempo per mangiare."
    show mio 1g at t11 zorder 1
    "Monika mi tira delicatamente le orecchie."
    mc "Ow! sì sì, andiamo..."
    mi "Uhuhu~ Dovresti andare."
    mc "Oh, io sono [player]. Piacere di conoscerti."
    mi 2f "Piacere mio, [player]! Il mio nome è Mio."
    $ mi_name = "Mio"
    mi 1x "Ci vediamo al Club allora!"
    show mio at lhide
    hide mio
    "Con quello, Mio si incammina nella direzione opposta, e l'espressione di Monika cambia facendosi più seria."
    mc "Um? Monika?"
    "Senza dire una parola, affera il mio polso e mi trascina dietro al cortile scolastico."
    stop music fadeout 2.0
    scene black
    with wipeleft
    scene bg yard
    with wipeleft
    "Una volta fuori, Monika mi lascia andare il polso mentre fa un mezzo giro. Poi inizia a fissarmi."
    show monika 3i at t11 zorder 1
    m "[player], quella ragazza non può venire oggi alla riunione."
    mc "Huh? {w=0.5}Perchè? {w=0.5}Eddai Monika, ti ho già detto che sarai l'un--"
    m "Non è per {i}quello{/i}, [player]..."
    m "Abbiamo già abbastanza problemi così senza dire ad altre persone di venire, no?"
    mc "Beh... Forse, ma..."
    "Oh Dio... Non ci avevo pensato a tutti i problemi che abbiamo..."
    "Non lo so... Ma credo dovremmo provare, no? Nel senso, dopotutto vuol dire avere più membri."
    "Sebbene, Monika abbia ragione... Come dovremmo gestire tutto quello che abbiamo da gestire?"
    m 2i "Come dovremmo spiegare tutta {i}questa{/i} situazione?"
    mc "Allora non dire niente a lei, dovrebbe andar bene, no?"
    m 2q "{i}sigh{/i}"
    m 3i "Questa non è un opzione [player]... Potrebbe capirlo da sola. Non intendo la verità di questo mondo, ma come le ragazze si comportano nei miei confronti."
    m 4i "Aggiungi se lo capisce da sola, come credi di spiegare {i}questo{/i}?"
    m "--o piuttosto, {b}non{/b} farlo?"
    "Wow, sono proprio un'idiota, nevvero?"
    "Dall'altra parte però, non è che abbia un modo per contattare Mio."
    mc "E se provassimo a cambiare classe?"
    m 1i "Non possiamo senza l'autorizzazione della presidenza. Senza menzionare il fatto che non sia il momento adatto per farlo."
    mc "Allora diciamole che non ci sarà l'incontro di oggi--"
    m 2g "[player], non possiamo mentire così a lei!"
    mc "Dio..."
    mc "Penserò a qualcosa. Nel mentre dovremmo cominciare a mangiare."
    "Con questo, Monika annuisce e ci sediamo entrambi su una panchina vicina a noi."
    show monika at thide
    hide monika
    play music tmonika_b fadein 3.0
    "Una volta seduti, Monika prende dal suo zaino due bentou, allungandomene uno."
    mc "Wow, a che ora ti sei alzata per prepararlo?"
    show monika 2b at t11 zorder 1
    m "Beh, abbastanza presto per farsì che non te ne accorgessi! Ahaha!~"
    show monika at thide
    hide monika
    "Aperta la scatola, noto che c'è il clasico contenuto del bentou, mentre Monika a più roba vegetariana."
    mc "Hey Monika?"
    show monika 1b at t11 zorder 1
    m "Sì?"
    mc "Ne hai davvero cucinato uno per ciascuno?"
    m 1l "Ahaha!~ S-sì?"
    m 3n "Perchè? E' un problema?"
    mc "N-{w=0.5}no! {w=0.5}E' molto carino da parte tua."
    m "Beh, grazie [player]!"
    mc "Mangiamo allora."
    show monika at thide
    hide monika
    "Wow... E' veramente carino da parte di Monika averlo fatto"
    "Sta veramente provando a sentirsi felice? O sta fingendo?"
    "Non lo so... Si sta davvero divertendo a passare il tempo insieme. Almeno, così è come sembra che sia."
    "Nel senso, posso vedere la felicità sulla sua faccia con tutte le porzioni di cibo che prende con le bacchette."
    show monika 5c at t11 zorder 1
    m "Uh... [player], va tutto bene?"
    "Non ho realizzato che ero perso nei miei pensieri mentre guardavo Monika."
    mc "Oh! Sì, sto bene. Sto solo pensando ai compiti di oggi."
    m 5a "Wow [player], Sono felice di sentirtelo dire!"
    m 2b "Dovresti cominciare a mangiare, le lezioni iniziano tra poco."
    mc "Oh, già. Va bene."
    "Con questo, inizio a mangiare."
    scene black
    with wipeleft
    scene bg yard
    with wipeleft
    "Passano 20 minuti e abbiamo finito di mangiare."
    "Devo dire che Monika si è davvero divertita, stavamo parlando un po' delle nostre vite, la nostra prima esperienza con le epifania e altre cose."
    play sound school_ring
    window hide(None)
    window auto
    pause 3.8
    m "Andiamo [player]~"
    mc "Sì', andiamo."
    "Ci dirigiamo entrambi verso le nostre rispettive classi."
    scene black
    with wipeleft
    scene bg stairs
    with wipeleft
    show monika 1a at t11 zorder 1
    "Come saliamo le scale, c'è sempre lo stesso ambiente, consentendomi di sapere che tutto è tornato alla normalità. Più o meno."
    stop music fadeout 2.0
    "Una ragazza con i capelli rosa splendenti si intravede facilmente da dove siamo, e ovviamente anche Kotonoha sta venendo. Posso già dire a chi appartengono quei capelli rosa."
    show monika 1f at t21 zorder 1
    window hide(None)
    window auto
    pause 2.0
    "Già, Natsuki sta arrivando con Kotonoha. Però, sembra molto scocciata."
    show monika 1f at t21 zorder 1
    show natsuki 1b at t22 zorder 1
    python:
      n_name = "Natsuki"
    n "[player], dobbiamo parlare."
    mc "Uh... sì, certo. Cosa c'è?"
    n 2x "...solo noi due!"
    play music late fadein 2.0
    "Guardo verso Monika, e le chiedo di andare con Kotonoha. Lei annuisce e si incammina verso Kotonoha."
    show monika at thide
    hide monika
    show natsuki 2x at t11 zorder 1
    mc "Che succede?"
    n 2o "Sei fottutamente pazzo o cosa?! Che hai nella testa?! Perchè Monika è tornata?!"
    mc "Beh, è stata Kotonoha a riportarla indietro in realtà."
    n 1c "..."
    "Natsuki chiaramente stupita, si gira verso Kotonoha, che sta parlando con Monika."
    "Poi si gira di nuovo verso di me e parla."
    n 3h "Quindi Kotonoha l'ha riportata indietro? Dunque, non sei tu il responsabile? Agh! mi ha ment--"
    mc "Non lo ha fatto. Le ho chiesto io di portarla indietro."
    n "..."
    n 4c "Hai chiesto a Kotonoha di riportarla indietro?"
    mc "Già."
    n 1m "Ma... Lei non dovrebbe conoscerla presumibilmente."
    mc "Beh, questa è la verità."
    n 1n "..."
    mc "Cosa? E' successo qualcosa?"
    n 4w "Hmph."
    n "Non che te ne importi o altro."
    mc "Mi importa molto, in realtà. Monika si sente davvero tormentata, Natsuki."
    show natsuki 1p at h11 zorder 1
    n "Eddai, [player]! Come potresti crederle?! Se davvero si sente così male, non avrebbe fatto tutto quello che ha fatto per cominciare!"
    mc "Natsuki, calmati... Ci stanno guardando tutti..."
    n 4w "Non me ne frega! Non posso credere quanto tu sia stupido!"
    "Avendo gli occhi di tutti su me e Natsuki, Kotonoha lascia aspettare Monika e si dirige verso di noi."
    show natsuki 5p at t21 zorder 1
    show kotonoha 7bf at t22 zorder 1
    kt "Che succede?"
    n 2p "Kotonoha..."
    n 2o "Tu...!"
    n 1v "Mi hai mentito!"
    kt 7bg "Huh? Che intendi, Natsuki?"
    n 5e "[player] ha detto che sei stata tu a portare Monika indietro! La conosci, vero?"
    kt 5bq "N-no! Non so di cosa lui stia parlando!"
    mc "Kotonoha, smetti di mentire. Non raggiungeremo il nostro obiettivo se continuiamo a mentire a tutti."
    kt 1bi "{i}*sigh*{/i}"
    n 2b "Quindi?"
    kt 4bo "Beh... Sì, la conosco..."
    n "..."
    n 3m "Perchè, Kotonoha? Perchè mi hai mentito?"
    kt 5bp "Perchè... voglio solo che tu venga alla stanza del club."
    n 3n "La stanza del club? Come fai a sapere del club?"
    kt 7bq "Beh... {w=0.5}Proprio come Monika ha detto a [player] una volta... \"So probabilmente molto più cose di quello ch pensi\"."
    "Monika chiaramente sorpresa, alza le sopracciglia confusa mentre guarda Kotonoha."
    n 3x "Ugh!"
    "Senza aggiungere altro, Natsuki ignora Kotonoha mentre si dirige verso la sua classe."
    kt "Natsuki, aspetta!"
    show natsuki at rhide
    hide natsuki
    show kotonoha 5bp at t11 zorder 1
    n "Cosa vuoi? Qual è la prossima bugia che mi racconterai? Kotonoha poi è davvero il tuo vero nome?"
    mc "Natsuki, per favore... Vieni alla stanza del club oggi una volta finita la scuola, ti scongiuro!"
    mc "Se non voi venire dopo oggi va bene, ma ti prego... Vieni al club."
    n "Hmph."
    "Alla fine, Natsuki mette il broncio e si incammina verso la sua classe."
    kt 6bu2 "Agh, sei un'idiota [player]!"
    "Anche Kotonoha si dirige correndo verso la propria classe prima che io possa darle una risposta."
    show kotonoha at rhide
    hide kotonoha
    show monika 1o at t11 zorder 1
    m "[player]..."
    m 2p "Sei andato un po' oltre, non credi?"
    mc "Non possiamo mentire a nessuno Monika. Non ci aiuterà e non ci porterà all'obiettivo che stiamo cercando di raggiungere."
    m 3p "Kotonoha sembra davvero inalberata..."
    mc "Sì, lo so... Ma non possiamo mentire a nessuno contando in che situazione siamo."
    mc "Comunque, questa è la tua classe, vero?"
    m 3n "G-{w=0.5}già... Quindi... Ci vediamo più tardi credo."
    mc "L'hai detto, m'lady."
    "Le faccio l'occhiolino prima di voltarmi verso la mia classe."
    m 2l "Ahaha!~"
    m 1b "Okay [player], a dopo!"
    stop music fadeout 2.0
    scene black
    with wipeleft
    scene bg class_day
    with wipeleft
    "Dopo la conversazione con Natsuki, ho avuto come una strana sensazione dentro di me."
    "Non voglio davvro rovinare i piani di Kotonoha... Ma non possiamo mentire a loro sempre così."
    "Mentire potrebbe comportare più problemi di quelli che potremmo gesitre... Eeeeeeee noi siamo già pieni di problemi."
    "Ahhhh beh..."
    "Quest'ultima lezione sta andando troppo lenta. Sai, il tipo di argomenti inutili che non useremo mai nelle nostre vite."
    "Come per Kotonoha... Mi sto già pentendo per quello che ho detto a Natsuki su di lei..."
    "Ben fatto [player], hai rovinato tutto un'altra volta."
    if persistent.kt_choice1 == 0:
      "Siamo riusciti a convincere Yuri a venire all'aula del club almeno."
      "Sono sollevato per questo... Credo."
      "Ho davvero rovinato i piani di Kotonoha, vero? Non so cosa stessi pensando..."
    elif persistent.kt_choice1 == 1:
      "Fortunatamente ho convinto anche Sayori, e anche se è ancora spaventata da Monika apprezzo davvero la sua gentilezza."
      "Questa è la Sayori che conosco da quando eravamo bambini: la stessa gentile e dolce Sayori."
      "Sono felice anche che Yuri abbia accettato la nostra richiesta di venire alla riunione del club oggi."
    else:
      "Ma ecco, direi che sta andando molto bene. Nonostante la roba con Natsuki, sta andando tutto..."
      "--bene?"
      "Sì, credo. Dobbiamo solo parlare agli altri di tutto quello che è successo, e se tutto va bene capiranno tutto."
      "Devo anche scusarmi con Kotonoha. Un'altra volta..."
    play sound school_ring
    window hide(None)
    window auto
    pause 3.79
    "Su, andiamo... E' tempo di andare al club."
    show sayori 1x at t11 zorder 1
    s "[player], dobbiamo andare al club, sei pronto?"
    mc "O-{w=0.5}Oh sì, andiamo."
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    "Mentre ci dirigiamo verso la stanza del club, non posso fare a meno di notare il sorriso di Sayori."
    "Io? Beh... Sono un po' nervoso ma ormai ci siamo."
    scene black
    with wipeleft
    scene bg club_day
    with wipeleft
    stop music fadeout 2.0
    "Una volta all'interno della classe, sento un improvviso senso di nostalgia. Ma in questo momento, la classe è vuota."
    mc "Ehilà? C'è nessuno?"
    show sayori 2a at t11 zorder 1
    s "Sembra che siamo i primi qua [player]."
    mc "Già, così sembra."
    s 2c "Beh... Dobbiamo aspettare che gli altri arrivino allora."
    mc "Se tutto va bene verranno..."
    window hide(None)
    window auto
    "Sono passati 5 minuti e non è arrivato nessuno. E se non venissero?"
    "La mia ansia inizia a crescere--"
    play sound closet_open
    window hide(None)
    window auto
    pause 0.25
    play music t3 fadein 2.0
    mc "Cos--?"
    mi "Oh! Scusate. Potrei entrare?"
    mc "Certo, entra pure."
    "Dioo... Mio è venuta veramente."
    "Mio apre delicatamente la porta della stanza ed entra."
    show sayori 2b at t21 zorder 1
    show mio 1e at t22 zorder 1
    mi "Saluti [player]!"
    mc "S-{w=0.5}sì... Ohilà Mio."
    mi 2c "..."
    mi "Um... Posso chiederti chi sei?"
    s 3l "Il mio nome è Sayori Sayori. La vice presidentessa del club..."
    mi 4f "Piacere di conoscerti Sayori. Il mio nome è Mio."
    s "Ehehe... Sì, piacere mio."
    "Una volta che Mio ha finito i saluti, si incammina verso un banco e posiziona il suo zaino sopra di esso."
    mi 3h "Dove sono gli altri?"
    mc "Ah beh, potrebbero essere un po' in ritardo."
    mi 5l "Capisco..."
    mi 5e "Dunque, aspettiamoli."
    s 1y "Sì, abbiamo aspettato qui per 5 minuti ora."
    s "[player], possiamo parlare qui fuori?"
    mc "Certo, andiamo."
    "Con questo, andiamo fuori dalla classe."
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    "Una volta qui fuori, Sayori chiude la porta e inizia a parlare."
    show sayori 1h at t11 zorder 1
    s "[player], conosci quella ragazza?"
    mc "Beh... Non proprio. Ma l'ho letteralmente urtata facendole cadere tutti i libri a terra durante l'ultima ricreazione."
    mc "Quindi, ho notato che aveva un libro sulla Letteratura Giapponese. Quindi le ho detto che se avesse voluto venire e non fosse stata in un club, che sarebbe potuta venire."
    s 1m "Eeehhh?"
    s 5d "E' il mio lavoro quello [player]!"
    mc "Heh... Credo di meritarmi il titolo di vice presidente invece."
    s 4p "Cattivo!"
    s 2c "Ma... Cosa ne pensa Monika di questo?"
    mc "Beh...Non ha avuto la reazione che mi aspettavo ad essere onesto."
    s "Oh, davvero? Come ha reagito?"
    mc "Beh, ha detto che Mio non sarebbe potuta venire all'incontro di oggi."
    s 2h "Hmm...Pensavo sarebbe stata contenta di avere un nuovo membro."
    mc "Già, a proposito... Potrebbero esserci due nuovi membri oggi."
    s "Due?"
    mc "Già, due in più."
    s 1x "Oooh! Chi è il secondo?"
    mc "Top secret mia cara amica."
    s 2y "Ehehe~"
    s 2n "Guarda, arriva Yuri!"
    "Guardando giusto dietro di me, Sayori vede Yuri arrivare. Poi abbraccia Yuri, quasi a placcarla."
    show sayori 4q at t22 zorder 1
    s "Heyyy Yuri!~ Mi sei mancata molto!"
    show yuri 2p at l22 zorder 2
    y "Cos--? Hey, non abbracciarmi così forte Sayori!"
    show sayori 5a at t21 zorder 1
    s "Ehehe... Scusami tanto Yuri, sono così felice di rivederti!"
    show yuri 2p at t22 zorder 1
    mc "Hey Yuri."
    show sayori 1a at t21 zorder 1
    y 1e "Ciao, [player]. Um... Perchè siete fuori dalla classe?"
    mc "Stavamo parlando dei nuovi membri che vengono oggi."
    y 2f "Nuovi membri? Di chi stiamo parlando?"
    mc "Beh, puoi vedere tu stessa attraverso la finestra della porta."
    "Yuri cammina verso la porta della classe e sbircia attraverso la finestra, vedendo Mio nel suo campo visivo."
    "Una volta che Yuri l'ha vista, comincia a parlare mentre continua a guardare attraverso la finestra."
    show yuri 2h at t22 zorder 1
    y "Uh... [player]..."
    mc "Sì?"
    y "Chi è quella ragazza?"
    mc "Beh, puoi andare dentro e parlarle direttamente o aspettare che tutti siano arrivati."
    y "..."
    y 3q "I-{w=0.5}Io credo che aspetterò qui con voi."
    show yuri 3q at t22 zorder 1
    mc "Va bene."
    "Dopo una corta attesa, Natsuki arriva dalla stessa direzione da dove è venuta Yuri. Non è venuta con Kotonoha comunque..."
    "Mi incammino verso Natsuki e le parlo."
    mc "Natsuki?"
    show sayori 1k at t31 zorder 1
    show yuri 1g at t32 zorder 2
    show natsuki 2e at l33 zorder 3
    n "Cosa?"
    mc "Dov'è Kotonoha?"
    n 2b "E' solo in una classe a fissare il niente. Ora andiamo!!!"
    show natsuki at thide
    hide natsuki
    show yuri 1g at t22 zorder 1
    show sayori 1k at t21 zorder 2
    "Prima di potermi muovere, Natsuki si fa spazio scansandomi di lato e apre la porta della stanza del club. Senza dire niente a Mio, si siede ad un banco."
    "Agh! Scommetto che Kotonoha si sente male per colpa mia!"
    "Devo trovarla."
    stop music fadeout 2.0
    mc "Hey Sayori, ho dimenticato un quaderno nella nostra classe, vado a prenderlo."
    s 2g "Oh, vorresti che venissi con te?"
    mc "No, {w=0.5}Preferirei andare da solo. Io... {w=0.5}Dovrei anche andare in bagno."
    s 2k "Okay, [player]."
    mc "Nel mentre, voi ragazze date un caloroso benvenuto ai nostri nuovi membri."
    $ s_name = "Yuri & Sayo"
    s "Okay [player]."
    $ s_name = "Sayori"
    s 2l "Andiamo dentro Yuri~"
    y 3g "S-{w=0.5}Sì. Andiamo."
    show sayori at lhide
    hide sayori
    show yuri at lhide
    hide yuri
    "Una volta che Yuri e Sayori sono entrate in classe, mi faccio strada verso la classe di Natsuki e Kotonoha."
    "Uff... Non so neanche come andrà la riunione di oggi... Natsuki è la mia più grande preoccupazione ora come ora."
    "Adesso che ci penso, se Natsuki è stata così altezzosa, saremo in grado di fare qualcosa?"
    "Forse col tempo potrebbe accettare che Monika sia ritornata e poi potremo tutti essere felici di nuovo."
    "Come per Kotonoha... Sono stato un'idiota nei suoi confronti di nuovo..."
    "Ora rimpiango tutto ciò che ho detto a Natsuki."
    "Scacciando questi pensieri dalla mia testa, inizio a camminare verso la classe di Natsuki."
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    "Sto camminando in questo corridoio per un po', pensando a cosa potrei dire a Kotonoha."
    "Dio... Non so neanche come reagirà quando vedrà che sono venuto a carcarla."
    "Devo scusarmi di nuovo con lei... {w=0.5}Ben fatto [player], l'hai ferita di nuovo."
    "Sei felice ora?"
    "L'ho cercata in ogni singola classe in questo corridoio. Forse si è nascosta o qualcosa del genere, ma non sa che la sto cercando."
    window hide(None)
    window auto
    pause 2.0
    "Hm..."
    "Aha! Eccoti qua Kotonoha!"
    play sound door
    window hide(None)
    window auto
    pause 3.0
    mc "Kotonoha?"
    kt "Huh? [player]?"
    play music t9 fadein 2.0
    mc "Sì, sono io. {w=0.5}Andiamo, dobbiamo andare al club, {w=0.5}forza s--"
    $ currentpos = get_pos()
    $ audio.t9 = "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    kt "Non voglio andare."
    mc "..."
    mc "Perchè?"
    kt "Non t'importa! Lasciami in pace!"
    mc "..."
    mc "Posso entrare?"
    kt "No! Ti ho detto di lasciarmi in pace!"
    mc "Kotonoha..."
    window hide(None)
    window auto 
    pause 3.0
    mc "Kotonoha?"
    kt "Lasciami in pace!"
    mc "Non lo farò."
    kt "Se mi odi così tanto allora cosa ci fai qui?! Vattene!"
    kt "Andrò al club una volta--"
    kt "{i}*sniff*{/i}"
    "..."
    kt "Io... Io voglio solo stare da sola."
    "Kotonoha sta piangendo?"
    "Oh no... L'ho fatto di nuovo."
    "L'unica cosa che volevo era cercare di evitare problemi e invece ho finito col crearne più di prima!"
    "Devo impegnarmi un po' più duramente per Kotonoha..."
    "Non perchè io sia inutile senza di lei, ma perchè in realtà mi importa di lei..."
    "--perchè la considero una mia buona amica."
    "Entro in classeI let myself in the classroom."
    scene black
    with wipeleft
    scene bg kt_classroom
    with wipeleft
    show kotonoha 1o at t11 zorder 1
    kt 1p "Ti ho detto di andare [player]!"
    mc "Ti ho detto che non lo farò."
    "Da dove ha preso quell'uniforme Kotonoha? Qualcuno le ha detto che poteva trovarla nel suo armadietto?"
    "Non è il momento per domande stupide [player]! Kotonoha sta piangendo di fronte a te!"
    kt 1p "Perchè mi odi?! Cos'ho fatto per farmi odiare così tanto da te?!"
    $ gtext = glitchtext(35)
    $ style.say_dialogue = style.edited
    kt 1u2 "Desidero davvero che [persistent.playername_b] non mi avesse por[gtext]{w=0.5}"
    stop music
    window hide(None)
    window auto
    pause 2.55
    $ style.say_dialogue = style.normal
    python:
      _history_list[-1].what = "[gtext]"
    show kotonoha 1u2:
        easeout_cubic 0.5 yoffset 850
    play sound "sfx/fall.ogg"
    #scene black
    kt "Gh--!"
    mc "Kotonoha!"
    scene mc_kt_cg
    with dissolve_scene_full
    $ renpy.music.play(audio.t9, channel="music", fadein=2.0, tight=True)
    "Kotonoha cade a terra, io mi inginocchio e la afferro."
    mc "Kotonoha... Mi dispiace!"
    mc "Mi dispiace davvero! Non voglio perdere un'altra amica di nuovo... Non ti odio Kotonoha, mi piaci davvero!"
    mc "Perchè pensi che ti abbia odiato? Mi... importa davvero di te Kotonoha."
    kt "Smetti di mentirmi!"
    kt "Non... non ti importa di me."
    kt "Mi stai facendo piangere... Non fai altro che rovinare i miei piani."
    mc "..."
    mc "Kotonoha, {w=0.5}Io--"
    kt "Zitto! Basta... Basta."
    kt "Voglio solo che tu mi dica perchè mi odi così tanto."
    mc "Kotonoha, ti ho detto che non--"
    kt "E' ovvio che mi odi!"
    "Kotonoha inizia a tirarmi pugni sul petto provando a liberarsi. Però non è abbastanza forte e non può far quasi niente."
    "Posso dire che ha delle mani veramente morbide, il suo pugno infligge poco dolore al mio petto. Riesco ad afferrarle il polso e a tenerle la mano."
    kt "Ah?!"
    mc "Kotonoha... Mi sento davvero male per come mi sono comportato nei tuoi confronti."
    mc "Non ti odio. Mi piaci davvero."
    if persistent.kt_choice1 == 0:
      mc "Sei davvero un aragazza coraggiosa ed intelligente."
      mc "Dopotutto non hai fatto alcun errore con Yuri. Ora è al club che ci sta aspettando."
      mc "Yuri ha deciso di ascoltare cos'ha da dire Monika, ed è venuta alla riunione. Senti, per favore non dire che ti odio. Non farlo mai più."
    elif persistent.kt_choice1 == 1:
      window hide(None)
      window auto
      pause 2.0
      "Kotonoha finalmente smette di agitarsi tra le mie braccia. Quindi continuo a parlare."
      mc "Vuoi sapere una cosa? Sei più intelligente di quanto io potrei mai esserlo. Sei pronta per tutto quello che ci verrà incontro."        #You're ready for everything that's coming our way."
      mc "E io invece cos'ho fatto? Ho solo parlato con Sayori e Yuri, e ora ci stanno aspettando al club."
      mc "Non dir più che ti odio... Ti considero davvero una buona amica, Kotonoha."
    else:
      mc "Tutto sta andando bene, e non lascerò che nessun altro soffra. Neanche tu."
      mc "Non solo questo, anche Monika è preoccupata per te! E lo sono anche io."
      mc "Mi dispiace di averti trattata così male... Mi piaci davvero, Kotonoha."
    kt "..."
    kt "M-{w=0.5}ma se non mi odi... {w=0.5}perchè hai detto quella cosa a Natsuki?"
    mc "Non possiamo più mentire a nessuno. Non penso che mentire ci porterà al risultato che vogliamo."
    mc "Le bugie vengono sempre scoperte non importa quanto bene sono celate."
    kt "[player]..."
    mc "Uh--"
    "Dopo che Kotonoha ha detto il mio nome, inizia ad abbracciarmi più forte che può."
    "E' un po' strano perchè riesco a sentire il suo... Um... il suo seno ed è molto più vicina al petto."               #It's kind of weird because I can feel her... Um... \"posture\" and she is way too close to my chest."
    "Ciò nonostante, mi lascio andare e lascio che mi continui ad abbracciare. Non vorrei rovinare questo momento."
    "Kotonoha strofina la sua faccia sul mio petto mentre sento il suo incontrollabile piagnucolio. Poi alla fine inizia a parlare."
    kt "..."
    kt "[player]..."
    mc "Sì?"
    if persistent.kt_choice1 == 2:
      kt "I-{w=0.5}io ti... {w=0.5}Piaccio veramente?"
    else:
      kt "D-{w=0.5}Davvero... {w=0.5}Davvero mi consideri una tua amica? Davvero mi apprezzi?"
    mc "Ovvio."
    "Provo a lasciarla andare, ma lei mi abbraccia ancora più forte."
    kt "S-{w=0.5}solo un altro po', [player]."
    mc "Oh... Okay."
    window hide(None)
    window auto
    pause 2.0
    "Sono passati 4 minuti buoni, e Kotonoha mi lascia andare."
    scene black
    with wipeleft
    scene bg kt_classroom
    with dissolve_scene_full
    show kotonoha 4d at t11 zorder 1
    kt "Hey [player]..."
    mc "Sì?"
    stop music fadeout 2.0
    kt 5s2 "D-{w=0.5}dovremmo andare in classe ora."
    mc "Oh! Già, andiamo."
    kt 3j "Uhuhu~"
    "Kotonoha prende il suo borsello dal suo banco ed esce dalla classe ridacchiando."
    show kotonoha at rhide
    hide kotonoha
    mc "Ahhhh..."
    kt "Dai su [player], porbabilmente si starannno chiedendo dove siamo~"
    mc "Sì! Sto andando!"
    "Prima di andare, mi assicuro che sia tutto a posto prima di chiudere la porta."
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    "Mentre camminiamo per andare in classe, vedo Kotonoha fissare il terreno mentre stringe il borsello con entrambe le mani."
    "Penso stia anche un po' arrossendo."
    "Non so cosa stia succedendo o cosa stia pensando, ma sembra davvero felice in questo momento."
    "Cosa succederebbe se glielo chiedessi?"
    window hide(None)
    window auto
    pause 2.0
    mc "Hey, Kotonoha?"
    show kotonoha 1j at t11 zorder 1
    kt "Sì?"
    mc "Stai bene?"
    kt "S-{w=0.5}sì. Perchè?"
    mc "Beh, stai arrossendo."
    kt 4t "S-{w=0.5}Sto bene!"
    mc "Heh."
    show kotonoha at thide
    hide kotonoha
    "Kotonoha sposta lo sguardo altrove, fissando il pavimento e avvicinandosi ancora di più a me. La sua faccia prende un intensa tonalità di rosso."
    "Beh... Devo dire che è carina, ma non voglio che pensi che voglia essere il suo ragazzo o altro."
    "Mi piace solo come amica, ma non vorrei neanche che morisse come è successo a Sayori..."
    "Penso sia meglio che non glielo dica. Almeno per ora è davvero felice, e non voglio rovinare questo momento felice per lei."
    mc "Di qua, Kotonoha."
    show kotonoha 7c at t11 zorder 1
    "Indico la porta."
    kt 7c "Mhm~"
    "Apro la porta lasciando entrare Kotonoha."
    scene black
    with wipeleft
    scene bg club_day
    with wipeleft
    play music late fadein 2.0
    $ currentpos = get_pos()
    $ audio.late = "<from " + str(currentpos) + " loop 0>eheart-music/Too Late.ogg"
    "Una volta all'interno del club, vedo Monika seduta alla cattedra."
    "Sayori è nel ripostiglio, Yuri al suo solito banco, Mio sembra un po' spaventata, e Natsuki è proprio davanti che sta fissando Monika."
    "Penso che dovrei chiedere a Sayori cos'è successo mentre non c'ero."
    "Mi giro verso Kotonoha, e anche lei si gira per guardarmi."
    show kotonoha 1e at t11 zorder 1
    mc "Kotonoha, devo parlare a Sayori. Puoi venire anche tu se vuoi."
    kt 1f "N-{w=0.5}no, preferisco aspettarti qui."
    mc "Bene, allora aspetta un momento."
    "Con questo, mi avvicino a Sayori."
    scene black
    with wipeleft
    scene bg closet 
    with wipeleft
    mc "Hey... Sayori?"
    show sayori 1g at t11 zorder 1
    s "[player]?"
    s "Chi è quella ragazza?"
    mc "E' il secondo membro. Vi presenterò tutte a lei, volevo parlare con te."
    s 1b "Hm?"
    "Guardo verso Natsuki e Monika."
    mc "Cos'è successo qui? Mi sono perso qualcosa?"
    s 1h "Ehhh... Beh, stavamo parlando a Mio, poi Monika è arrivata. Natsuki seduta a quel posto l'ha a..."
    s "--poi Monika ha salutato tutti, ma nessuno apparte Mio l'ha salutata."
    mc "E' tutto?"
    s "Sì..."
    mc "Capisco."
    mc "Bene, facciamolo. Vieni qua Sayori."
    s "..."
    s 2k "Preferirei non..."
    mc "Huh? Perchè? Stavi aspettando questo da tutto il giorno, no?"
    s "..."
    "Senza dire altro, Sayori si va a sedere al suo solito posto"
    show sayori at thide
    hide sayori
    "Dio... Cos'altro è successo qui?"
    "Penso che questa situazione dipenda da me e Kotonoha."
    "Guardando dritto, mi incammino verso la cattedra."
    scene black
    with wipeleft
    scene bg club_day
    with wipeleft
    "Riesco letteralmente a sentire l'aura amara provenire da Sayori, Yuri e Natsuki nei confronti di Monika, quindi chiedo a Kotonoha di venire con me. Lei annuisce e anche lei si incammina verso la cattedra."
    mc "Oookay, ragazzi?"
    "I loro occhi fissati su di me, mi fanno sentire un po' nervoso. Niente ripensamenti ora."
    "Sospiro e inizio a parlare."
    mc "Bene... {w=0.5}Allora, oggi vi ho chiamato considerando tutto quello che è successo \"prima\"."
    "Kotonoha si piega verso di me e mi sospira qualcosa."
    show kotonoha 2f at t11 zorder 1:
      alpha 0.48
    kt "{i}[player], per favore sta attento. Quella ragazza coi capelli arancioni non sa niente riguardo al vecchio mondo.{/i}"
    kt "{i}Lo prometti?{/i}"
    mc "{i}Sì, te lo prometto.{/i}"
    show kotonoha at thide
    hide kotonoha
    "Detto questo, Kotonoha annuisce e poi guarda Mio."
    mc "Allora... Oggi parleremo di due cose. Prima di tutt, i nuovi membri."
    mc "Forse vi starete chiedendo chi sono queste ragazze, ebbene--"
    show natsuki 1b at t11 zorder 1
    n "Mio."
    mc "Cos--?"
    mc "La conosci?"
    n 1g "Hmph."
    show natsuki at thide
    hide natsuki
    "Ignorando la mia domanda, Natsuki distoglie lo sguardo."
    mc "Bene... Mio, prego vieni qui."
    mi "O-okay..."
    "Mio si alza dal suo posto e si incammina lentamente verso la cattedra."
    show mio 1k at t11 zorder 1
    "Poi fa un mezzo giro e gentilmente posa le sue mani una sopra l'altra."
    mc "Dunque... Sì, questa è Mio. Sarà un nuovo membro del nostro club, quindi ragazzi diamole un--"
    show mio 1j at t21 zorder 1
    show natsuki 2b at t22 zorder 1
    n "Apparentemente saresti un membro del club di musica, no?"
    mi 2l "Già... Beh, in un certo senso l'ho lasciato e quando [player] mi ha invitata a venire, io ho accettato il suo invito."
    mc "Okay... Qesta è Kotonoha, viene da un'altra scuola ed è per questo che il suo accento è un po' diverso."
    show mio 1k at t31 zorder 1
    show natsuki 2b at t32 zorder 1
    show kotonoha 7s at t33 zorder 1
    kt 7s "Sì, uhm... Vengo dalla regione del Kansai, dalla prefettura di Osaka."
    "..."
    "Un'altra volta nessuno dice niente."
    show mio 1k at t41 zorder 1
    show natsuki 2b at t42 zorder 1
    show kotonoha 1s at t43 zorder 1
    show yuri 2q at t44 zorder 1
    y "B-{w=0.5}benvenuta, Kotonoha."
    show natsuki at thide
    hide natsuki
    show mio at thide
    hide mio
    show kotonoha 4v1 at t21 zorder 1
    show yuri 2q at t22 zorder 1
    kt "O-{w=0.5}oh! Grazie, uh..."
    y 2u "I-{w=0.5}il mio nome è Yuri. Piacere di conoscerti."
    kt " Oh già, me lo ero dimenticato... {w=0.5}Ci eravamo incontrati stamattina nel cortile."
    y "S-{w=0.5}sì, scusami per quello!"
    kt 2a "Non preoccuparti, è tutto apposto."
    #show kotonoha 4a at t31 zorder 1
    show kotonoha 4a at t31 zorder 2
    show yuri 2s at t32 zorder 1
    show mio 2g at t33 zorder 1
    y "Benvenuta anche a te, Mio."
    mi 4l "Grazie, Yuri! Spero che potremo essere amiche."
    y 3b "Sì, lo spero anche io."
    show kotonoha at thide
    hide kotonoha
    show yuri at thide
    hide yuri
    show mio at thide
    hide mio
    "Ero così distratto a vedere tutti che si presentavano che non ho realizzato che Monika non è più qui."
    mc "Hey Kotonoha?"
    show kotonoha 1f at t11 zorder 1
    kt "Sì?"
    mc "Dov'è Monika?"
    stop music fadeout 2.0
    kt "Se n'è andata da un po'... Scommetto che è nel corridoio."
    mc "..."
    mc "Okay vado a vedere se è lì."
    mc "Tieni tutti occupati nel mentre."
    kt 4e "C-{w=0.5}certo, [player]! Sarà datto."
    mc "Bene, allora torno subito."
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    "Come esco dalla classe, vedo Monika che sta fissando fuori dalla finestra."
    "Mi avvicino in silenzio a lei e inizio a parlare."
    mc "Monika?"
    show monika 1g at t11 zorder 1
    m "[player]?"
    $ audio.t9 = "<loop 3.172>bgm/9.ogg"
    mc "Va tutto bene?"
    m 1o "..."
    m 2p "No..."
    play music t9 fadein 2.0
    mc "Perchè? E' successo qualcosa?"
    m 2p "Sarebbe stato meglio se non ci fossi venuta qui... Non vogliono davvero parlarmi."
    m "E' stato un errore riportarmi indietro... Riportare tutti indietro..."
    mc "Non dirlo mai più! Non è stato un errore!"
    mc "Ti ricordi cosa ti ho detto?"
    m 1o "Hm?"
    mc "\"Se vuoi la pace; preparati per la guerra\" in pratica. Non butterai tutto quello che abbiamo fatto fino a adesso, vero?"
    mc "Questo non è il modo giusto di pensare Monika. Non buttare via tutti i tentativi di Kotonoha... Arrendersi non è una scelta."
    m "Già..."
    mc "Quindi, non farlo. E' ora di finirla. Non far sentir male Kotonoha perchè vuoi arrenderti."                            #Kotonoha feel bad by just giving up."
    m 2n "Ma... Perchè sei così preoccupato per Kotonoha?"
    mc "Perchè non sono stato altro che un'idiota nei suoi confronti. L'ho fatta piangere senza volere... L'ho ferita."
    mc "Mi preoccupo di tutti, devo proteggere tutti. Devo impegnarmi di più anche per Kotonoha."
    m "Ma lei non è una di noi..."
    mc "No, finché è nel club e continua ad essere una mia amica, sarà una di noi."
    if persistent.kt_choice1 == 1:
      mc "Non hai visto com'era torta dal dolore quando stavamo parlando?"
      m 3n "Beh... Ha detto che era solo...ummm beh... problemi da donne. E' abbastanza comune quando sei una ragazza, [player]."
      mc "Non erano per niente problemi da donne! C'è qualcos'altro che Kotonoha sta patendo." #That wasn't lady problems at all! There's something else Kotonoha is going through."
    m "..."
    m 2p "Sì... Hai ragione, credo..."
    if persistent.kt_choice1 == 1:
      m "Cosa pensi che possa star patendo?"
      mc "Non ne sono sicuro..."
    mc "Come per gli altri, devi stare calma. Tutti meritano di sapere cos'è successo, no?"
    "Dicendole quello, inizia a rilassarsi un po'."
    m 2m "Già..."
    mc "Te l'abbiamo già detto. Andrà tutto bene, e se vuoi i tuoi amici indietro, allora dobbiamo gestire questa \"tempesta\"."
    mc "Non c'è problema che non possa essere risolto qui."
    m "..."
    window hide (None)
    window auto
    pause 2.0
    m 2m "Hai ragione [player]..."
    m 3l "Ahaha!~ Sono un disastro, nevvero?"
    mc "Ah beh, dovremmo entrare e sistemare tutto."
    stop music fadeout 2.0
    m 1k "Mhm~"
    "With that, we both get inside the classroom."
    scene black
    with wipeleft
    scene bg club_day
    with wipeleft
    "While joining the others, I can see Kotonoha sitting at the teacher's desk talking to the girls."
    "I'm surprised how well Kotonoha has gotten along with everyone here."
    mc "We're back."
    "They all turn to look at me. Or rather Monika, I'm not really sure though."
    "Kotonoha stands up from the teacher's desk taking a seat at one of the desks in the classroom, allowing us to take control."
    if renpy.random.randint(0, 3) == 0:
      $ renpy.sound.play(audio.notif)
      $ renpy.notify("SGVyZSdzIHdoZXJlIHRoZSBlbmQgYmVnaW5zIGZyb20u==")
    "Alright...Now is the time."
    "Having Monika stand beside me, I place my hand on her shoulder. She then starts speaking."
    $ renpy.music.play(audio.late, fadein=2.0, tight=True)
    $ audio.late = "<loop 0>eheart-music/Too Late.ogg"
    show monika 1m at t11 zorder 1
    m "Well..."
    m 4n "Y-{w=0.5} you probably all recall everything that happened before and you're all kind of confused, but..."
    m 2o "Today I want to say... That I really feel terrible for everything that happened before, I know I made some horrible mistakes."
    m "I really regret everything I've done... For everything I made you go through... For being so selfish..."
    "Kotonoha stands up from her chair, she whispers something to Monika. I assume it's the same thing she told me. Anyway, Monika just nods and speaks up again."
    m 3o "I want to thank [player], because he's helping me make this possible. He's being very understanding even knowing everything I did."
    m "Kotonoha has helped me a lot as well... I met her thanks to [player], and she's willing to help me."
    m 4o "I've been pursuing something I know I can't reach, and that {i}someone{/i} gave me this chance as well..."
    m 2q "I'm really sorry everyone, and if you all give me a second chance I swear I'm not gonna commit the same mistakes I did before."
    show monika 2q at t21 zorder 1
    show natsuki 1e at t22 zorder 2 
    n "Well well well, are you finished already? May we speak our minds now?"
    "Natsuki stands up from her chair staring at Monika. Monika has a concerned expression on her face as she looks at Natsuki."
    m 2o "Well, yeah..."
    n 2e "Why should we trust you to begin with?"
    n "If you really feel thaaaaat \"bad\", why did you do that to begin with?"
    show monika 2o at t31 zorder 1
    show natsuki 2e at t32 zorder 2 
    show yuri 3o at t33 zorder 3
    y "A-{w=0.5}agreed."
    n 2h "Sayori?"
    s "..."
    "Kotonoha is beside me watching this argument and listening to how they speak their minds about this situation. But Mio..."
    "Mio is in her seat having no idea about what's happening here."
    "Concerned, I turn to look at Kotonoha."
    show monika at thide
    hide monika
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show kotonoha 4b at t11 zorder 1
    mc "{i}Kotonoha?{/i}"
    kt "{i}Hm?{/i}"
    mc "{i}Could you take Mio elsewhere please? I'm gonna deal with this. As soon as everything finishes, I'll phone you.{/i}"
    kt "{i}O-okay [player]...{/i}"
    show kotonoha at thide
    hide kotonoha
    "With that, Kotonoha goes to Mio's desk indicating to her that they have to leave."
    show monika 2o at l41 zorder 1
    show natsuki 2e at l42 zorder 2 
    show yuri 3o at l43 zorder 3
    show sayori 1f at l44 zorder 4
    "Once they're out of the clubroom, I focus on the girls again."
    s 2h "Agreed."
    n 1g "You see? {w=0.5}No one trusts you! So, get o--"
    play music t9 fadein 2.0
    s 3l "Wait! While I don't believe Monika actually regrets everything she did, I can't say she doesn't feel bad."
    y 3j "I concur with Sayori as well."
    n 2e "What?! Oh, come on!"
    n "Did you really believe that fairy tale [player] told you?!"
    $ s_name = "Sayo & Yuri"
    s "No."
    $ s_name = "Sayori"
    y 2h "Nonetheless, we can't say Monika isn't feeling bad at all."
    s 1k "That's right... {w=0.5}If Monika tried to at least talk with Yuri, I'd say she really does feel bad actually."
    s "We have to be antipathetic."
    y 1l "Empathetic, Sayori."
    s "That!"
    s 1g "I kinda get how Monika was feeling though... When I realized what this world is..."
    s "I almost killed my friends too..."
    s 2k "So... I really do understand how Monika was feeling! Even so, that doesn't justify the fact that she did mean things to us."
    y "As Sayori said: Monika did try explaining her situation to me, So I do trust she's feeling bad as well."
    y "That doesn't mean I believe she's actually feeling regretful of her actions though."
    n 3x "Ugh..."
    n 3w "I can't believe how credulous you girls are."
    m 2o "Natsuki, {w=0.5}I--{w=0.5}"
    n 3e "No Monika, you're not gonna trick me anytime soon. Unless you can prove your regret to me, I'm not gonna trust you ever again!"
    mc "Natsuki, just--{w=0.5}"
    n "Blah blah blah. That's all I hear from you, [player]."
    "Sitting back in her seat, Sayori and Yuri walk towards us."
    show natsuki at thide
    hide natsuki
    show monika 2o at t31 zorder 1
    show sayori 2k at t32 zorder 2
    show yuri 1l at t33 zorder 3
    $ s_name = "Sayo y Yuri"
    show sayori 2h at t32 zorder 1
    show yuri 1h at t33 zorder 2
    s "Monika..."
    $ s_name = "Sayori"
    m 1f "Hm?"
    s "As we said, while we do understand you, it doesn't mean we believe that you're feeling this remorseful this quickly."
    s "But even so... We'll be here."
    y 2h "Affirmative."
    y "Just that."
    "With that, Sayori and Yuri return to their respective seats."
    show yuri at rhide
    hide yuri
    show sayori at rhide
    hide sayori
    show monika 1q at t11 zorder 1
    stop music fadeout 2.0
    "Well... That could've gone worse, I guess."
    "I turn to look at Monika, who now seems to have calmed down."
    mc "Monika?"
    m 2m "Y-{w=0.5}Yes?"
    mc "Do you feel any better now?"
    m "Yeah... {w=0.5}You guys were right, [player]-"
    if persistent.kt_choice1 == 0:
      m "Yuri did understand after all."
    elif persistent.kt_choice1 == 0:
      m "Yuri and Sayori did understand, just like you said..."
    else:
      m "Despite Natsuki being kind of rude, I'd say everything went well."
    mc "Yeah. Just a moment, I'm gonna call Kotonoha."
    m 1m "Mhm~"
    "I take my phone out and dial Kotonoha's number."
    window hide(None)
    window auto
    pause 2.0
    kt "{i}[player]?{/i}"
    mc "Yo Kotonoha, everything's done over here. Time to come back."
    kt "{i}How did it go?{/i}"
    mc "Well, it could have been worse."
    kt "{i}Huh? What's that supposed to mean?{/i}"
    mc "Sayori and Yuri understand Monika, although they're not convinced of Monika's remorse."
    kt "{i}What about Natsuki?{/i}"
    mc "Tonight I'm paying a visit to your hotel so we can talk."
    kt "{i}O-{w=0.5}oh... {w=0.5}Are you sure?{/i}"
    mc "Yeah, why not?"
    kt "{i}N-{w=0.5}no! I didn't mean it like that, I just...{/i}"
    mc "Okay... Come here already."
    kt "{i}Mhm~{/i}"
    "Kotonoha hangs up first."
    "I can't help but wonder what Kotonoha is thinking about..."
    "Ahhh well, I think I have to finish today's meeting."
    scene black
    with wipeleft
    scene bg club_day
    with wipeleft
    play music t3 fadein 2.0
    "Kotonoha and Mio arrived and well...Mio still seems to be kinda confused."
    "I let everyone have a little chit-chat before calling for the girls to leave. Monika is talking with Kotonoha."
    "Meanwhile Sayori, Mio and Yuri are on the other side of the classroom having a conversation. Natsuki is... Well, doing nothing."
    "Alright, time to call it a day [player]. I'll call for everyone."
    mc "Hey girls! It's time to leave. What if we all bring poems for tomorrow? So we all can start building confidence in each other again."
    show sayori 1l at t11 zorder 1
    s "I have no problem with that."
    show sayori 1l at t21 zorder 1
    show yuri 3l at t22 zorder 2
    y "I-{w=0.5}I guess that could work..."
    show sayori 1l at t31 zorder 1
    show yuri 1l at t32 zorder 2
    show natsuki 2b at t33 zorder 3
    n "Whatever."
    show sayori 1l at t41 zorder 1
    show yuri 1l at t42 zorder 2
    show natsuki 2b at t43 zorder 3
    show kotonoha 5s at t44 zorder 4
    kt "W-{w=0.5}what?! I've never wrote any poetry ever in my life!"
    show sayori 1l at t51 zorder 1
    show yuri 1l at t52 zorder 2
    show natsuki 2b at t53 zorder 3
    show kotonoha 5s at t54 zorder 4
    show mio 5b at t55 zorder 5
    mi "That's a good idea."
    mc "Alright! So, everyone bring a poem of their own for tomorrow's meeting. So we can all have a chance to rebuild the club."
    $ s_name = "Everyone"
    s "Okay..."
    $ s_name = "Sayori"
    show kotonoha at rhide
    hide kotonoha
    show mio at rhide
    hide mio
    show natsuki at rhide
    hide natsuki
    show yuri at rhide
    hide yuri
    show sayori at rhide
    hide sayori
    "Having said that, everyone goes to get their belongings and leaves the clubroom."
    show sayori 1c at t11 zorder 1
    s "[player], you coming?"
    mc "Actually, I'm gonna stay for a little bit."
    s 1d "Ehehe~"
    s "Okay, see you tomorrow."
    show sayori at thide
    hide sayori
    "Sayori slowly leaves the clubroom, leaving just the two of us here."
    "Monika is cleaning up and aligning the desks. {w=0.5}Okay [player], it's time."
    "I walk towards Monika."
    mc "Hey, Monika?"
    show monika 1c at t11 zorder 1
    m "Yes, [player]?"
    mc "Uh... Well, I was wondering if you..."
    mc "--if you would want to go somewhere today."
    m 1d "Huh? Well, I..."
    mc "{w=0.5}Well, it's okay if you don't want to, we have to do tomorrow's assignments and--"
    m 2e "I would love to, [player]~"
    mc "Wha--? {w=0.5}Really?"
    m 1b "Sure! Why not?"
    mc "Ok... Well, so, should we get going then?"
    m 3k "Ahaha!~ I'm gonna change out of my uniform [player], I'll see you at your house instead."
    mc "Y-{w=0.5}yeah... See you then."
    m 5f "See you soon!~"
    show monika at thide
    hide monika
    "Ah well... I thought that she was gonna say 'no'."
    "But well, I'm not considering the fact that she's making me call her \"my girlfriend\" even though I haven't asked her yet."
    "Alright [player], time to leave and get ready!"
    scene black
    with wipeleft
    scene bg corridor
    with wipeleft
    "For now I just want go home and get ready for today's meeting with Monika."
    "Or... Is this a date?"
    "Ah well, I just have to stay calm and I'm sure everything will go fine."
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    # show text()
    show text("{size=100}{color=#6debab}{b}Moments ago{/b}{/size}{/color}\n{size=60}at Kotonoha's POV.{/size}"):
      truecenter
    with Dissolve(1.0)
    pause 2.0
    scene bg corridor
    with dissolve_scene_full
    "[player] did tell me to take Mio somewhere since they all are starting to talk about what happened before. Mio shouldn't know that."
    play music t6 fadein 2.0
    "Since I had that argument with Natsuki when [player] told her that it was me who brought Monika back, she doesn't want me to be close to her."
    "And well, Mio was looking at me kinda weird, I decided to ask her. But... I kinda know her actually."
    $ currentpos = get_pos()
    $ audio.t6 = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    show mio 1b at t11 zorder 1
    mi "Um... Excuse me?"
    "Mio turns to face me."
    "I make contact with Mio's eyes and reply back."
    kt "Hm? What is it?"
    mi 2i "What's happening in there?"
    mi 2k "I-{w=0.5}it's because of me, isn't it?"
    kt "Well, not really. I don't really know what they are up to..."
    "Trying to pretend that I know nothing about what happened is what I reply to Mio, who is evidently kinda concerned."
    "It seems like she bought the lie, so she just nods and speaks up again."
    mi 4l "Oh... I see. So, what are we going to do in the meantime?"
    kt "Hmm... I don't know. Do you have any ideas?"
    mi 5e "What if we go to the backyard? There's nobody here after all~"
    kt "Sounds good, let's go then."
    "Mio takes the lead and we go to the backyard."
    scene black
    with wipeleft
    scene bg yard 
    with wipeleft
    show mio 6x at t11 zorder 1
    mi "Aaahh! Nothing like breathing fresh air after a rough class day."
    kt "Mhm~"
    "Ahhh... I really missed this peaceful environment. I used to come here every morning."
    "Mio points towards a bench as we were walking around, we then both have a sit."
    show mio at thide
    hide mio
    "Once we sit down, the conversation we had a little while ago starts to fade into an unsettling silence."
    "I didn't expect anything else actually since... Well, I never managed to have a conversation with her since we were at the Music Club."
    "She's kinda condescending, the kind of people I really hate the most."
    "We weren't even close to having a conversation now that I think about it, mainly because when she tried to do so I just tried to avoid her."
    "I can't do that right now because supposedly she doesn't know who I am so it would look kinda odd."
    "I mean, she told me where to find my uniform despite the fact I know where it is located. Even so, I think that I should thank her for that."
    kt "Hey, Mio..."
    show mio 1c at t11 zorder 1
    mi "Hm?"
    "Mio turns to see me."
    kt "Uhm... Well, I just wanted to thank you for telling me where I can find my uniform. I was feeling kinda weird walking around with my dress."
    mi 5x "Uhuhu~"
    mi 5e "You're welcome Kotonoha!"
    $ currentpos = get_pos()
    $ audio.t6 = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    mi 2f "It's just that... Well, you sort of remind me of someone. I can't figure it out though..."
    stop music fadeout 2.0
    kt "Gh---!"
    "..."
    "What did she just say?!"
    mi 3i "Kotonoha? Did I say something wrong?"
    kt "O-oh! No, I'm currently struggling with my period and--"
    mi 1a "Uhuhu~"
    extend 8f "Okay okay, I got you."
    $ renpy.music.play(audio.t6, fadein=2.0, tight=True)
    $ audio.t6 = "<loop 10.893>bgm/6.ogg"
    "With that, Mio sits straight up while swinging her legs up and down like a little girl."
    "What did she just say?! Does she know something she's not telling me about?"
    show mio at thide
    hide mio
    "I don't understand... Perhaps [persistent.playername_b] didn't delete everyone's memories?"
    "I doubt it... They were as careful as they could in regards to that... I'm telling that person anyway!"
    "Once the night falls I'm gonna ask that person. I wouldn't want something else to happen. It's Mio after all. She used to be in the Music Club."
    "As usual while lost in my thoughts, Mio speaks to me."
    show mio 2a at t11 zorder 1
    mi "Hey, Kotonoha."
    kt "Yeah?"
    mi 1e "I really love your braid! Can I get a closer look at it?"
    kt "Well...Sure."
    "Mio gets slightly closer to me and starts touching my braid."
    show mio 7f at face zorder 1
    mi "Woah, it's so cute! It fits you very nicely~"
    kt "{w=0.5}Well, thank you so much! It is a real pain to make it like that."
    mi 6e "I bet."
    window hide(None)
    window auto
    pause 2.0
    show mio 6e at t11 zorder 1
    with None
    mi "Aaaand... Do you have a boyfriend?"
    kt "Gh--!"
    "What?! What is she even talking about?! God... I feel my face blushing so much right now!"
    "Trying to avoid eye contact with her, I look away."
    kt "W-{w=0.5}well... Not really."
    mi 2g "Oooh, I see. It's a shame, you're such a beautiful girl~"
    "..."
    "Someone save me! My face is as red as a tomato and I'm unable to speak without stuttering."
    "Mio then starts speaking again."
    mi 1c "And... Is there someone you have a crush on?"
    "She isn't gonna stop, is she? I'm feeling kinda harassed and flustered..."
    "I mean, I can't say anything to her since we're nothing. I used to talk about my crush on [player] with Naomi, but it's not the same case... After all, she was my friend."
    "What if I just tell her? Will there be consequences?"
    window hide(None)
    window auto
    pause 1.0
    "Okay, I'm gonna tell her."
    kt "Well, {w=0.5}actually I--"
    play sound cellphone
    window hide(None)
    window auto
    pause 2.0
    kt "Wha--?"
    kt "Um, [player] is calling me, just a moment."
    "Thanks [player], you just saved me!"
    show mio at thide
    hide mio
    "I reach for my phone and answer it."
    kt "[player]?"
    mc "{i}Yo Kotonoha, everything's done over here. Time to come back.{/i}"
    kt "How did it go?"
    mc "{i}Well, it could have been worse.{/i}"
    kt "Huh? What is that supposed to mean?"
    mc "{i}Sayori and Yuri understand Monika, although they're not convinced of Monika's remorse.{/i}"
    kt "What about Natsuki?"
    mc "{i}Tonight I'm paying a visit to your hotel so we can talk.{/i}"
    kt "O-{w=0.5}oh... {w=0.5}Are you sure?"
    mc "{i}Yeah, why not?{/i}"
    kt "N-{w=0.5}no! I didn't mean it like that, I just..."
    mc "{i}Okay... Come here already.{/i}"
    kt "Mhm~"
    "Ahhh, I had luck this time! Mio is kinda behaving weird towards me."
    "I think that I can evade her question this time."
    "Whatever, I just put my phone in my purse and call for Mio."
    show mio 1a at t11 zorder 1
    kt "Mio, it's time to leave already!"
    mi 3e "Okay Kotonoha, let's go~"
    mi "I almost forgot! Don't think that you can evade my question!~"
    stop music fadeout 2.0
    kt "Uh... Y-{w=0.5}yeah, I guess that I don't have a choice..."
    mi 1x "That's right! Come on, let's go."
    show mio at thide
    hide mio
    "Saying no more, Mio heads back to the building."
    "Well... That was something... That question bomb Mio threw at me is kinda suspicious actually..."
    "I mean, supposedly she doesn't know anything about this world and she shouldn't remember who I am."
    window hide(None)
    window auto
    pause 2.0
    "Or... Does she?"
    scene bg mc_lr
    with dissolve_scene_full
    "It's been an hour since school finished. Since then I've been getting ready for today's meeting with Monika."
    "I wouldn't want to look like a homeless bum after all."
    "I've been thinking about Kotonoha today as well... Every time I talk to her, she gets flustered and stutters."
    "Almost like she has feelings for me, but... Why would she feel something for me? Is that even possible? And I mean having a crush on someone you don't know at all."
    "I don't know... But I have to let her know that I love Monika. I have to be careful though, I wouldn't want her to commit suicide..."
    "I mean, Kotonoha is a really cute girl but she's not my type. Not to mention that I just met her, so... Dating her doesn't feel right at all."
    "I'm gonna tell her sometime soon."
    play sound "<from 2.00>mod_assets/theme/door.ogg"
    window hide(None)
    window auto
    pause 2.0
    "I hear knocking at the door. Monika must be here already."
    scene black with wipeleft
    scene bg mc_hw with wipeleft
    mc "Yeah?"    
    m "It's me [player]~"
    "I open the door letting Monika in."
    play music tmonika_b fadein 3.0
    show monika 1bb at t11 zorder 1
    m "Hello [player]~"
    mc "Hey Monika! You take your time, don't you?"
    show monika 1bk at h11 zorder 1
    m "Ahaha!"
    m 4bk "Well, I had to get ready after all. It would be better than me coming here with my school uniform on, wouldn't it?"
    mc "Heh... Yeah, you got me there. So, where are we heading to?"
    m 2bc "Hm..."
    m 2be "I don't know. I thought you had something planned."
    mc "Heh... Not really."
    m 2bb "Oh, I got it! What if we just go with the flow?"
    mc "Hm... Are you sure?"
    m 1bb "Mhm~"
    mc "Alright then... Do you know a cafe near here? I barely know my neighborhood."
    m 1bj "Ahaha!~"
    extend 1ba " Of course I do, [player]. There's a good cafe in the city!"
    mc "I'll follow you."
    "With that we both head out to the cafe that Monika is talking about."
    play sound closet_open
    scene black with wipeleft
    scene bg house with wipeleft
    play sound closet_close
    "Once we're out Monika points in the direction that we need to go, and it seems that it's on the same street where Kotonoha's hotel is at."
    scene black with wipeleft
    scene bg street with wipeleft
    "God... Speaking of, I'm still worried about Kotonoha... I can't help thinking about what she's going through... If I want to try harder for Kotonoha, I need to know what's happening to her."
    "I'll try to reach her as soon as I'm done spending time with Monika."
    if persistent.kt_choice1 == 1:
      "Y'know, I need to make sure she is doing alright. I mean, the way she behaved this morning was kind of odd. That \"problem\" she mentioned isn't something I can just believe."
      "I need to show her that I really do care about her, that's why I need to make sure she's alright."
    else:
      "I haven't thanked her for everything she did today, and I'm pretty sure that doing so would make her happy."
      "I really want to let her know that I like her and I'm really thankful for her help so far."
    show monika 1bg at t11 zorder 1
    m "Um... [player], are you okay?"
    mc "Ah--"
    mc "Y-yeah, why?"
    m 2bg "You look kind of stressed... Is there something that is stressing you so much?"
    mc "Not really, I'm just thinking about the poem that I'm going to write for the club meeting."
    m 2bc "Oh!"
    extend 3bb " Have you come up with something yet?"
    mc "Not really... I'm still thinking about that, it's not like I'm a good writer after all."
    m 1bb "Well, I'm sure you'll come up with a good poem eventually. "
    extend 1ba "The only thing you just need to do is practice a little bit!"
    mc "You think so?"
    m 3bk "Of course! We all have talent to do something, though practice is necessary."
    mc "Heh... Yeah, I guess you're right. What about you? Do you have an idea for your poem?"
    m 1bb "Yeah, but I'm not telling you~ Ahaha!"
    mc "I see... Well, I'm a patient man. More or less."
    show monika 3bb at h11 zorder 1
    m "Isn't that Kotonoha's hotel?"
    scene black with wipeleft
    scene bg st with wipeleft
    "Monika points in the direction of Kotonoha's hotel. It's certainly a big hotel, and not very cheap either."
    "Pulling my sleeve, Monika calls for me while she flashes me a sweet smile."
    show monika 2bl at t11 zorder 1
    m "You know something? I want to go to visit her place and cheer her up after all that stuff you made her go through."
    mc "H-hey, I said that I was sorry! Hopefully she understood that..."
    m "Ahaha!~ "
    extend 3bb "Well, I think that Kotonoha is a really nice girl actually. I'm sure she'll find a boyfriend that appreciates her and loves her."
    mc "Yeah, she's a very nice person. I'm even surprised with how well she knows you all."
    mc "Kotonoha is kind of a mysterious girl, isn't she?"
    m 2bc "Eh?"
    extend 1bd " What are you even talking about?"
    mc "Um... Nevermind. It's just crazy stuff that I'm thinking about."
    mc "Anyway, where is that cafe located at?"
    m 3bb "Over there."
    scene black with wipeleft
    scene bg cafe2 with wipeleft
    "As Monika said, this cafe looks really nice being next to Kotonoha's hotel."
    "Wow... I'm really surprised with this. I didn't even know that this cafe even existed. I really need to get out more."
    "Monika stands in front of me while smiling."
    show monika 1ba at t11 zorder 1
    m 1ba "So, what do you think, [player]?"
    mc "Well... It looks good from outside."
    m 1be "Oh..."
    extend 2bb " Well, this is a really good cafe! I swear you're gonna love it."
    mc "Okay, what are we waiting for then? Let's step in!"
    "Saying no more Monika nods and we both head towards the cafe."
    show monika 1bb at h11 zorder 1
    m "Follow me~"
    scene black with wipeleft
    scene bg cafe_inside with wipeleft
    "As soon as we get in, the smell of coffee fills the whole place giving it a kind of mature environment. It feels weird though..."
    show monika 1bb at t11 zorder 1
    m "Well?"
    mc "Woah, this certainly is a nice place! And this coffee smell makes it even better."
    m 2bb "Just wait till you taste the coffee!"
    "Monika then heads to the clerk and cheerfully greets him."
    m "Hello!"
    $ n_name = "Clerk"
    n "Welcome lady, may I take your order?"
    m "Sure, can I get an americano?"
    n "Okay! What is the boy having?"
    mc "Hm... Well, actually I'm not a coffee drinker, so I'm not sure what to order."
    m 3bb "What about a coffee with milk?"
    mc "I'm not a child either..."
    "The clerk while looking at me decides to give me a suggestion."
    n "How about a capuccino? It's not as strong-flavored as the one the lady asked for!"
    mc "Hm... Okay, I'll take that."
    n "Well! 551¥ please."
    "As the clerk rings up our order, Monika takes some money out of her purse."
    mc "Wait, Monika..."
    m 2bc "Hm?"
    "It's definitely not right if she pays for the coffee, I would feel bad if she did."
    "But it's also not fair if I just pay for everything, isn't it?"
    menu:
      mc "Well..."
      "Pay for everything.":
        $ pay_everything = True
      "Divide the bill.":
        $ pay_everything = False
    if pay_everything:
      "No, I'm the one who invited her, so that's why I have to pay for everything."
      "And since she's my guest I have to do this for her. I turn to look at Monika."
      mc "Monika... I'm paying for everything."
      m 1bg "[player], no! let's just divide the bill, that would be fair."
      mc "No way, I'm paying."
      python:
        m_aff -= 1
      $ renpy.sound.play(audio.notif)
      $ renpy.notify("Monika's affection = \"[m_aff]\"")
      "Monika, looking kind of sad, puts her money back into her purse, letting me cover the bill."
      mc "You can wait over the--"
      m 2bh "Mhm."
      show monika at rhide
      hide monika
      "She then heads to a table and sits down."
      "..."
      n "{i}Hey.{/i}"
      mc "{i}Hm?{/i}"
      n "{i}I think you should have let your girlfriend pay for half the bill{/i}"
      mc "{i}She's not my girlfriend yet.{/i}"
      n "{i}Yeeeeaaaahhh... She's not...{/i}"
      "He then goes to the kitchen to prepare our coffee orders. I may have made a mistake now that I think about it..."
      "But letting her pay anything would ruin my reputation as a man."
    else:
      "I think I'll ask Monika if we can divide the bill... It's not fair if she pays for everything herself, is it?"
      "Seeing as I invited her, it would be good idea if we did that."
      "Monika is still watching me so I respond to her."
      mc "Monika, what if we divide the bill instead of you paying for it all?"
      m 1bc "Um..."
      extend 2bd " Are you sure?"
      mc "Yeah! I think it would be unfair if you pay for everything."
      mc "It's no big deal!"
      m 2bj "Okay."
      $ m_aff += 1
      $ renpy.sound.play(audio.notif)
      $ renpy.notify("Monika's affection = \"[m_aff]\"")
      "I take my wallet out of my pocket and hand Monika enough money to cover half the bill."
      m 3bb "Thank you~"
      show monika at rhide
      hide monika
      "She then goes to search for a table for us to sit at."
      n "Your order will be ready in a while."
      mc "Alright."
      "I head towards the table Monika chose for us."
    scene black
    with wipeleft
    scene bg cafe_inside
    with wipeleft
    if m_aff > 0:
      "Monika happily waves her hand telling me to sit down."
      show monika 1bb at t11 zorder 1
      m "[player]~"
      mc "That's me."
      m "Mhm~"
      m 1bd "Hey, [player]?"
      mc "Yeah?"
      m 1be "I just wanted to thank you for helping me pay the bill!~ It was so nice of you."
      mc "Oh! Sure, I thought it would be wrong if you paid for everything yourself."
      m 2bk "Ahaha!~"
    else:
      "Monika is sitting at the table staring at nothing through the window."
      show monika 1bc at t11 zorder 1
      mc "I'm back."
      m 1bc "Mhm."
      "Monika, without looking at me gives me a dry answer."
      mc "Hm? Did something happen?"
      m 1bd "Yes."
      extend 3bg " Don't you think I should have paid at least half of the bill?"
      mc "No, don't you worry. It's okay."
      m 2bf "Okay..."
    mc "So, is there anything that you would want to talk about?"
    m 1bc "Hm..."
    if m_aff > 0:
     m 1bn "W-well, I want to thank you for everything you've done for me so far as well!"
    else:
     m 1bn "W-well, I want to thank you for everything you've done for me so far!"
    mc "Heh, well I didn't do it all, it was Kotonoha too, remember."
    m "Yeah... You're right."
    m 2bn "What if we go to pay Kotonoha a visit at her hotel? I would like to talk to her."
    mc "Sure, I gotta talk to her too."
    show monika 1bh at t11 zorder 1
    "Monika stares at me while lost in thought, she then speaks."
    m 2bi "Did something happen?"
    mc "Well.. Today she kind of cried again because of me..."
    if persistent.kt_choice1 == 1:
     mc "Not to mention her odd behavior from today."
    m 2bc "Hm..."
    m 2bd "Because of that Natsuki stuff?"
    mc "Yeah... She thinks I hate her for telling Natsuki that it was her who brought you back."
    mc "I have had to explain everything to her and I let her know that I don't hate her. I think she understands."
    m 2be "That's a relief..."
    $ n_name = "Waiter"
    n "Your coffee is done!~"
    "The waiter comes with a tray with two cups on it. He then politely places each cup on the table and takes a bow."
    mc "Wow, this place has awesome service."
    m 1ba "This is a really good cafe~"
    mc "Yeah, it looks like it."
    m 1bj "Mhm~"
    "With that Monika takes a sip of her coffee. Just the strong smell that emanates from her cup makes me feel like a kid... I should try that coffee."
    m 1ba "So, [player]..."
    extend 2bb " You assigned everyone poems for tomorrow's meeting, didn't you?"
    mc "Yeah... I'm sorry for taking your place. You were looking kind of down at the time."
    m "Ahaha!~ It's okay [player], thanks for doing that for me!"
    mc "Plus I think that it's a great way to rebuild this club and get to know Mio a little bit better."
    m 1bf "Yeah, Mio..."
    mc "Hm?"
    m 2bl "Oh! Nevermind, ignore that."
    "While looking out the window, Monika takes another sip from her cup."
    mc "Did something happen with Mio?"
    m "No, everything's okay [player]..."
    mc "Hm..."
    $ mi_name = "???"
    mi "[player]? Monika?"
    $ n_name = "Natsuki"
    $ m_name = "[player] & Mon"
    m "Ah--"
    $ mi_name = "Mio"
    $ m_name = "Monika"
    show monika 2bf at t21 zorder 1
    show mio 1c at t22 zorder 1
    mc "Uhhh... Mio? What are you doing here?"
    mi "Did something happen? It's almost like a ghost scared you guys!"
    "..."
    "What time did Mio come in? I didn't even see her."
    "Monika lowers her eyes once she notices Mio is here at the cafe, so I think that I should ask Mio what she is up to."
    mc "You haven't answered my question yet Mio."
    mi "Hm..."
    extend 1e "Buying a coffee for myself I suppose. This is a cafe after all, isn't it Monika?"
    m 2bp "Y-yeah..."
    mc "Shouldn't you be writing tomorrow's poem?"
    mi 2e "Yes, that's why I'm getting some coffee~ Writing a poem is not the only assignment I have to get done."
    mi 1e "I usually spend time doing my homework and studying for a little bit at night. So the surprise exams are not so surprising for me!"
    mc "Fair enough. So, leave already and do whatever you have to get done."
    mi 3h "Eeehhh? But my coffee isn't ready yet! Coffee is something that takes time, right Monika?"
    m 1bp "Y-you're right."
    mc "Well... I mean, butting in on another's conversation isn't well-mannered."
    mi 1f "Oh! Are you talking about someone behind their back? Because that's really bad too, [player]... You might hurt their feelings!"
    mi 8f "Fortunately, the generous part of me is gonna just let it go, though next time I will make you pay for it~"
    mc "As long as it's not money, I'm willing to do whatever you want."
    mi 8e "Whatever I want? "
    extend 1y "Uhuhu~ "
    extend 3e "That's the spirit, [player]!"
    mc "No, I didn't mean it like that! I meant that--"
    mi 1a "Too late for regrets [player], now you will have to fulfill that promise."
    mi 2x "Looking forward to listening to you guys talk about me while I'm not around!"
    $ n_name = "Clerk"
    n "{i}Espresso coffee order!~ Your beverage is ready!{/i}"
    $ n_name = "Natsuki"
    mi 3e "Oh, that's me! See you tomorrow guys~"
    mc "Uh-huh. See you."
    mi 8e "See you later Monika!"
    m "S-sure. Goodbye."
    "With that, Mio walks towards the clerk, takes her coffee, and leaves the cafe, winking at me while doing so."
    show mio at thide
    hide mio
    show monika 1bo at t11 zorder 1
    "Geez... What just happened?"
    "Monika is still staring at nothing while tracing the rim of her cup with her fingers."
    mc "Hey!"
    m 1bp "Hm?"
    mc "What happened? Are you alright?"
    m "...Oh, yeah I'm okay. Shall we drink our coffee? I want to go outside and get some fresh air."
    mc "Uh... Alright."
    "Damn! Mio just ruined this special moment Monika and I were having."
    "How did Mio come in without us noticing?  Did something happen between Monika and Mio?"
    "I really don't understand anything... But I gotta get rid of her before she ruins my chance with Monika!"
    "I don't know if I should talk about this with Kotonoha though... But for now I'll keep it to myself. Unless everything starts to get difficult."
    "Well, for now I'm gonna drink this cup of coffee."
    scene black with wipeleft
    scene bg cafe_inside with wipeleft
    "A good 25 minutes have passed since Mio left the cafe. On the other hand, Monika is barely saying anything."
    "Could it be because of that \"As long as it's not money, I'm willing to do whatever you want\" stuff? It's just logic actually."
    "I think that I'm gonna clear that up once we're at the park."
    show monika 1bd at t11 zorder 1
    m "Are you ready to leave [player]?"
    mc "Oh, sure. I've finished my coffee already. Do you still wanna go to the park?"
    m 2bd "Yeah, I need to get some fresh air."
    mc "Alright, let's get going then."
    "Monika takes her purse from the table, while I stand up myself."
    scene black with wipeleft
    stop music fadeout 2.0
    scene bg cafe2 with wipeleft
    "Once we step out I can't help noticing Monika's expression becomes more serious. No doubt it's because of what I said to Mio..."
    "But can I do something if she's not willing to tell me what happened before? Because I don't think so..."
    "That being said, I'm taking on yet another problem that needs to be done. I have to think of something."
    "Something good!"
    mc "Well, where's the park?"
    show monika 3bd at t11 zorder 1:
      xzoom -1
    m "Over there."
    "Monika points with her finger where the park is located at."
    mc "Well, I'll follow you."
    scene black with wipeleft
    scene bg city_b with wipeleft
    play music city fadein 2.0
    "Ahhh... It's almost nighttime already and the cold wind starts to come..."
    "Since the park is kind of close, we just have to walk a few blocks."
    "Monika is walking in front of me saying nothing. For now I'm not gonna push her. I'll leave her be and wait for her to tell me what's happening."
    "Yeah, that's the best choice for now."
    "I don't know if I should try chatting with her... This is becoming awkward."
    mc "Hey, Monika?"
    show monika 1bd at t11 zorder 1
    m "Hm?"
    mc "Uhm... How are you feeling right now?"
    m 1bf "..."
    show monika at thide
    hide monika
    "Saying nothing, Monika just turns back. God... Something definitely happened with Mio, but I can't do anything if she refuses to tell me."
    "I just want Monika to tell me..."
    extend "For now it would be best if I remain silent."
    scene black with wipeleft
    scene bg park_b with wipeleft
    "The sun barely illuminating the street makes it look very beautiful. It gives the environment a certain air of peacefulness."
    "Monika stops walking while doing a half turn to face me, then she speaks up."
    show monika 2bg at t11 zorder 1
    m "Hey, [player]..."
    mc "Yeah?"
    m 2bn "Well... It's about that Mio stuff that happened at the cafe..."
    $ currentpos = get_pos()
    $ audio.city = "<from " + str(currentpos) + " loop 0>eheart-music/city.ogg"
    mc "Oh... Well, What happened then?"
    stop music fadeout 2.0
    m "Well... "
    extend 1bp "Ehm..."
    extend 2bp "I kind of think that Mio knows what this world is."
    "..."
    mc "What?"
    m 1bd "Look... When I walked into the clubroom, Mio greeted me in a very weird manner, Almost like she knew what I was doing."
    mc "Well, she's clearly behaving kind of condescending, but to be honest I think that's just the way she is."
    m 2bq "..."
    m 2br "I mean, she's behaving like that just with me [player], but she doesn't do that with the others."
    "I don't know where Monika got that from... But I don't see anything off about her, actually."
    "I'd say that she's just a condescending person, that's it. Unless she actually shows that she's well aware of what this world really is."
    "Then that would be something of Kotonoha's concern as well, but for now these are just Monika's speculations."
    "Let's give her the benefit of the doubt."
    mc "{i}*sigh*{/i}"
    mc "Look Monika... What you're saying is barely provable, not to say it can't be proven. For now these are just speculations of yours."
    m 1bg "But [player]--"
    mc "Nevertheless, if it makes you feel any better then let's give her the benefit of the doubt and let's be on the lookout for her."
    m 1bd "Shouldn't we tell Kotonoha about this?"
    mc "No, not yet. If we confirm that she knows something then we'll tell Kotonoha."
    mc "Understand?"
    m 2bd "Yeah... I think it's for the best right now."
    $ renpy.music.play(audio.city, channel="music", fadein=2.0, tight=True)
    mc "Cool, so let's enjoy ourselves before going to Kotonoha's place."
    m 1bb "Mhm~"
    scene black with wipeleft
    scene bg park_c with wipeleft
    "We have been sitting on a bench in the park, looking at the trees that are covered with the sun's soft illumination as it slowly starts to fade into night."
    "Monika - despite being still kind of worried, is actually enjoying herself."
    "It's getting dark already so I think it's time for this day to come to an end."
    mc "Hey Monika, it's time to leave already."
    mc "Are you sleeping at your home today or something?" 
    show monika 2bl at t11 zorder 1
    m "Well... It's not like I have my own house, you know?"
    mc "Then you can sleep at my house, is that okay with you?"
    m 1bk "Okay [player]!"
    mc "I suppose you have your belongings in that purse, don't you?"
    m 1ba "Yes!"
    mc "Alright, so... Shall we meet Kotonoha at her place? So we can write our poems for tomorrow."
    m 2bk "Ahaha!~"
    extend 2bb " Did you bring your notebook?"
    mc "Geez... No, I forgot it... Then we should go to her home another time."
    m 3bb "I can give you a sheet of paper from my notebook if you want!"
    mc "Oh, will you do that for me?"
    m 3bk "Sure! Plus, your house isn't near here at all. Ahaha!~"
    mc "Heh, you got me there. Let's get going then."
    m "Mhm~"
    "Having said that, Monika and I make our way to Kotonoha's."
    scene black with wipeleft
    scene bg city_c with wipeleft
    m "Hey, [player]..."
    mc "Hm?"
    "Monika raises her eyes and stares at me."
    show monika 2bp at t11 zorder 1
    m "Is this really for me?"
    mc "Uh? What are you talking about?"
    stop music fadeout 2.0
    m 1bn "You told Mio that you're willing to do anything she wants..."
    mc "Uhm... Well, I didn't know what to say..."
    mc "But if you're that worried then yeah, this is not just for you; it's for the others as well."
    mc "Mio was... Well, it was a mistake of mine to bring her to the club... So, for now we have to try to get along with her."
    m 2bn "Yeah... I suppose you're right."
    mc "Mhm. "
    show monika 1bn at t11 zorder 1
    play music night fadein 2.0
    extend "As for Mio... I think we just need to be alert, and be ready for anything."
    m "Agreed, we have to do that. But trust me [player], Mio is suspicious..."
    mc "We'll see Monika. We'll see..."
    mc "Well, now where should we walk to?"
    mc "Isn't that the bridge that goes to Kotonoha's sidewalk?"
    m 1bd "Um... I think so. "
    extend 2bk "Oh wait, it is! That's the cafe [player]!"
    scene black with wipeleft
    scene bg cafe3 with wipeleft
    mc "Ohhh yeah, you're right! Wait, I'm gonna call Kotonoha and tell her to be ready."
    show monika 1bk at h11 zorder 1
    m "Okay [player]!"
    mc "Ahhh wait, I'm not getting any coverage."
    m "Okay! "
    extend 2bb "Will it be okay if I wait at the cafe?"
    mc "Sure, go for it."
    m 1bb "Don't be too long [player]~"
    show monika at thide
    hide monika
    "As I take my phone out, Monika walks towards the cafe and rests her back on the wall."
    "Using both hands I start typing Kotonoha's number."
    window hide(None)
    window auto
    pause 2.0
    $ kt_name = "Voicemail"
    kt "{i}The number you are trying to reach is not available at this time. Try again later.{/i}"
    mc "Eh?!"
    mc "Come on... Don't do that..."
    window hide(None)
    window auto
    pause 2.0
    kt "{i}The number you are trying to reach is not available at this time. Try again later.{/i}"
    mc "What the--"
    show monika 1bg at t11 zorder 1
    m "[player]? Did something happen?"
    stop music fadeout 2.0
    mc "Kotonoha is not answering her phone. We gotta go to her place."
    m 2bg "Oh... What do you think is happening?"
    mc "I don't know... But I'm getting worried."
    "Saying nothing else, we both head to the bridge."
    scene black with wipeleft
    scene bg st3 with wipeleft
    play music spns fadein 2.0
    "Walking as fast as we can, we're coming closer to the bridge."
    "Is it possible...? Did she...?"
    "No [player], stop thinking like that! Kotonoha wouldn't do that... I suppose..."
    "I'm probably exaggerating, but I can't help thinking of anything else except Kotonoha taking her own life..."
    "I just can't help it."
    mc "Alright, we're here."
    m "Mhm."
    scene black with wipeleft
    scene bg hotel with wipeleft
    "Once we get inside the hotel, we make our way to the reception desk, where the recepcionist is doing something on his computer."
    $ n_name = "Recepcionist"
    n "Welcome, what can I help you with?"
    mc "I came to visit a friend of mine, a tall silver haired girl."
    n "What's her name?"
    mc "It's Kotonoha."
    "The recepcionist then goes back to his computer, presumably looking for Kotonoha's room."
    n "..."
    n "Ah! It's room 308-C; third floor."
    mc "Okay, thank you."
    mc "Come on Monika."
    show monika 2bd at t11 zorder 1
    m "Yeah..."
    python:
      n_name = "Natsuki"
    "With that we both walk to the elevator."
    scene black with wipeleft
    scene bg hotel2 with wipeleft
    #play music hotel fadein 2.0
    show monika 1bc at t11 zorder 1
    m "Hey [player]?"
    mc "Hm?"
    m 2bd "Um... Don't you think that you're being paranoid?"
    mc "Huh?! No! I... I'm just worried about a friend."
    m 3bd "I bet she's just taking a shower."
    mc "I don't know..."
    "Monika stands straight."
    m 2bi "[player], I know you want to help Kotonoha as well, but I think you should try to trust her at least."
    m 1bi "I don't think Kotonoha would do something like {i}that{/i}, even when she knows that you really care about her, you hav--"
    "Suddenly, the elevator's door slowly opens, revealing Kotonoha semi-nude. She's just wearing a nightgown."
    python:
      kt_name = "Kotonoha"
    stop music
    kt "Wha--?"
    play music t7 fadein 2.0
    kt "AAAAHHHHHHHH!"
    play sound "sfx/fall2.ogg"
    show monika at thide
    hide monika
    scene bg hotel2 at n_cg2_wiggle
    "Monika pushes me towards the elevator's left side, She then hugs Kotonoha, nearly tackling her."
    kt "Uwa--?! M-Monika, w-what are you doing?!"
    m "[player] is right there! Do you want him to look at you semi-nude?"
    "As I'm rubbing my shoulder, Monika stares at me."
    mc "Ow... Was that necessary?!"
    m "I-I'm sorry [player]! K-Kotonoha is... Well... Kind of a mature and a well developed girl."
    kt "What?! What are you even saying, Monika?!"
    m "Ahaha!~ I-I'm sorry Kotonoha."
    m "Even so, close your eyes [player]!"
    mc "Huh? But then I can't see where I'm going!"
    m "Well, I'm gonna be your eyes! Just take my hand~"
    mc "Uh? What do you mean by that?"
    m "I'm going to guide you."
    kt "Guide him? Where to?" 
    m "Oh by the way Kotonoha... We gotta talk to you."
    stop music fadeout 2.0
    kt "Oh... I see. Well, my room is one floor up. We can go there if you guys want to."
    m "That would be nice~"
    "As I recover, Kotonoha stares at me and starts blushing."
    kt "C-Close your eyes, [player]!"
    mc "I'm not even watching you."
    kt "You might still try to stare at me and I don't want you forming lewd thoughts in your head!"
    mc "What kind of degenerate do you think I am?"
    kt "J-Just do it!"
    mc "{i}*sigh*{/i}"
    mc "Alright..."
    scene black
    with close_eyes
    play music hotel fadein 2.0
    "With my eyes closed, Kotonoha then steps in the elevator. I gotta admit that I kind of actually wanted to look at her though..."
    "Well, glad I didn't do that anyway."
    kt "Uhm... May I ask what's happening?"
    m "Well, actually we came to talk to you about something, didn't we [player]?"
    mc "Yeah, me and Monika have something we want to discuss with you."
    kt "I see."
    m "Um... Kotonoha?"
    kt "Yes?"
    m "Can I ask why you are semi-nude walking around this corridor?"
    kt "Oh... Well, the hotel has an awesome pool; the water is set to an ideal temperature."
    kt "It makes the water feel warm, very relaxing actually. And well, the corridor is empty at this time so why not?"
    m "Ahaha!~ You're enjoying yourself at this hotel, aren't you?"
    kt "Well, this is one of the best and most expensive hotels in the city. It would be a waste if I don't take advantage of it, you know?"
    m "Fair enough."
    kt "Over here, let me open the door."
    stop music fadeout 2.0
    play sound closet_open
    kt "Get in~ Remember to take your shoes off."
    play sound closet_close
    mc "Can I open my eyes already?"
    kt "N-not yet!"
    mc "..."
    mc "Alright..."
    "As soon as I hear Kotonoha run to the bathroom, I slowly open my eyes."
    scene bg hotel3 with open_eyes
    mc "Ahhhh... Finally."
    show monika 2bk at t11 zorder 1
    play music night fadein 2.0
    m "Ahaha!~ You know what? I think Kotonoha was as paranoid as you."
    m "I mean, I wouldn't mind if you looked at me semi-nude~"
    mc "It's a different situation nevertheless."
    m 2bl "Yeah... I think you're right."
    "Having no more to say, Monika sits on the bed while we wait for Kotonoha."
    m 3ba "Do you wanna sit as well [player]?"
    mc "No, I prefer to stand here while we wait for Kotonoha."
    m 2bb "Okay~"
    "After a short period of time, Kotonoha steps out of the bathroom already dressed."
    show monika 2ba at t21 zorder 1
    show kotonoha 7bc at t22 zorder 2
    kt "I'm back!~"
    m 1bb "Okay, so... Can we talk to you?"
    kt 1be "Sure, go ahead."
    mc "Well... Ladies first."
    m 1be "Okay. Well, I wanted to thank you for everything you did today. I really appreciate your effort."
    kt 2bh1 "Uhuhu~ Well, it's nothing. I almost feel like I already know you actually."
    m "..."
    m "What?"
    kt 7bs2 "Oh! Ignore that, it was just kind of a metaphor. "
    extend 4bd "What I mean is, that I enjoy helping you out."
    kt "This power I have... It's almost like being God. It feels awkward though."
    kt 2bd "I'll be here anytime you need me!"
    mc "Well, as I said to Monika: this is not just for her, it's for you too."
    kt 2be "..."
    kt 4bf "What are you talking about?"
    m "Hey Kotonoha? Can I take a shower in your bathroom?"
    kt 7bf "Sure, go ahead."
    stop music fadeout 2.0
    "Before heading to the bathroom, Monika comes close to me and whispers something."
    show kotonoha at thide
    hide kotonoha
    show monika 1bd at face zorder 1
    m "Just be considerate with what you are gonna say [player]... Kotonoha is not mentally healthy either."
    show monika 1bd at t11 zorder 1
    with None
    "With that, Monika makes her way to the bathroom."
    show monika at rhide
    hide monika
    "Well, so... Here we go."
    mc "So, Kotonoha..."
    play music t9 fadein 2.0
    show kotonoha 4bb at t11 zorder 1
    kt "Yeah?"
    mc "Look... I was spending my time with all the other girls in the club before, except for Monika. "
    show kotonoha 1bb at t11 zorder 1
    extend "And after she realized this entire world is fake, Monika lost her mind and did some terrible things."
    kt 1bb "Mhm..."
    mc "So, I don't want to make the same mistake. Now you're one of us, and I'm not gonna leave you behind."
    kt 7be "But [player], wasn't this for Monika to begin with?"
    mc "That doesn't mean that you don't all deserve to be happy...To live a normal life."
    mc "It's not a choice. I want to protect everyone. And despite the fact that I don't know you very well, I can tell that you're a very wonderful and intelligent person."
    "Kotonoha stares at me while presumably thinking of something. Next, she sighs."
    kt 1bv1 "B-but [player]..."
    mc "Hm?"
    kt 7bv1 "Are you sure you can deal with such a big responsibility?"
    mc "Whatever the price is, I'm willing to pay it as long as I can see you all smiling everyday. I'm gonna give it my best effort to reach that ending we are all looking for."
    kt 5bs "[player]..."
    "Kotonoha sits on the bed at the left side, I sit right next to her."
    "Kotonoha facing the floor, I hold her hand in mine. Her hand is as soft and small as Monika's. "
    show kotonoha 4ba2 at t11 zorder 1
    extend "Kotonoha blushes and looks away."
    "Giving her a moment to recover, I proceed to talk again."
    mc "I know what you are thinking... You probably think that I am doing this because I want to look like a tough guy that can do anything... But I really want to make you all happy."
    mc "I don't care what the price is and I don't care if there will be consequences, I'm gonna keep my promise!"
    mc "Even if this world is not real, even if you think everything might go wrong, I'll be there for you."
    mc "I'm not going to lose the people I love... Not again. I want everyone to be happy."
    mc "And \"everyone\" also includes you."
    kt "A-Are you serious, [player]?"
    mc "Yeah."
    mc "Nobody will suffer as long as I'm here. "
    extend "Not again."
    kt 4bs "Well... I don't know what to say..."
    kt 1bp "I just..."
    "As Kotonoha lowers her head, she lets go of my hand and places her hand on her chest."
    kt 3bp "[player], I'm sorry... But you can't do anything with what I'm going through... Nobody can!"
    mc "There's no such thing as an unsolvable problem. Even if it takes a long time, every problem can be solved eventually."
    mc "And since I care for you, I'm gonna help you with whatever you're going through. I promise you."
    if sheet == 0:
      mc "Watching you cry in the principal's office is just confirming that you're not doing alright at all."
      mc "But even if I ask, I don't think you're gonna tell me what's happening."
      kt 3bo "{i}*sigh*{/i}"
      extend 4bq " It's not like I don't want to tell you... I do want to, but there are a lot of reasons why I can't do that..."
      mc "What would that be?"
      kt "I cannot tell you."
    else:
      mc "The way you just sat on the couch at the principal's office staring at that sheet kind of confirms that you're not doing alright."
      kt 2bq "Yeah... You're right..."
      mc "So, can you tell me what's happening?"
      kt 4bw "I don't think so, [player]..."
      mc "Then would it be better if I don't bring it up again?"
      kt "Yeah."
    mc "Well..."
    if persistent.kt_choice1 == 1:
      mc "Just tell me something. Do you have some kind of heart issue?"
      kt 1bw "No... Why would you think that?"
      mc "Ah, nevermind."
    mc "I suppose you're not willing to tell me what happened when we were in your classroom, are you?"
    kt 2bw "Uh? What about?"
    mc "The way you tried dissimulating the pain on your chest is something that kind of got me concerned."
    mc "Are you sure you don't have some heart issue or something?"
    kt 1bs "Uhh... Not really."
    mc "Well, then we're going to the hospital on Friday."
    kt "..."
    kt "Okay [player]..."
    "The bathroom door slowly opens, revealing Monika already dressed in her PJs."
    stop music fadeout 2.0
    show monika mp1_b at l21 zorder 1
    if persistent.kt_choice1 == 1:
        show kotonoha 1bw at t22 zorder 1
    m "I'm back!~"
    show kotonoha 1bv at h22 zorder 1
    play music hotel fadein 2.0
    kt "Wha--?"
    kt 4bf "Why are you in your pajamas already?"
    m mp2_b "So I could feel more cozy I suppose. Ahaha!~"
    kt 4bs2 "O-oh! Y-yeah, I guess you're right."
    m "Are you guys done talking?"
    kt "Y-yeah! Nothing e-else happened!"
    m mp2_l "Huh? I never said that."
    mc "{i}*sigh*{/i}"
    "Now that I think about it... It will be better if Monika stays here with Kotonoha. They get along so well!"
    "And since they seem to get along so well, it would be a good idea. So Kotonoha will rid herself of these thoughts."
    "These thoughts that make her say I don't care about her."
    mc "Hey, Kotonoha?"
    kt 7bf "Hm?"
    mc "Can somebody stay here with you for awhile?"
    kt 7bu2 "Eeehhh?! {w=0.5}I-if you think that I'm gonna allow you to stay here with me, then I just want you to know that...!"
    mc "Not me. I'm a boy who stares at girls and forms lewd thoughts in his head after all."
    kt 4bs "Very funny, you pervert!"
    python:
      m_name = "[player] & Moni"
    show monika mp2_k at t21 zorder 1
    m "Ahahahaha!"
    python:
      m_name = "Monika"
    mc "I'm talking about Monika actually..."
    kt 4bf "Oh! "
    extend 4bj "Of course she can stay here!"
    m mp3_n "Oh... I guess you don't want me to stay at your place, [player]..."
    mc "We'll talk about that later, alright?"
    m mp3_o "Okay..."
    extend mp2_b "By the way Kotonoha, did you write your poem already?"
    kt 3bq "W-well no... To be fair I know nothing about poetry..."
    m mp2_b "Alright, I can help you write one then! Shall we write our poems, then?"
    kt 1bj "Oh, that's a good idea! Thank you Monika!"
    m mp1_k "Okay, I'm going to get my notebook!"
    mc "Wait, will it be a problem if someone else stay here?"
    kt 7be "Hm... "
    extend 4ba "I don't think so. "
    extend 3bc "Even so, I'm gonna talk to the recepcionist and see if there's something we can do."
    m "Well, this is the first time that I'm staying at a hotel of this caliber, so I'm gonna feel kind of weird."
    kt 1bc "Don't worry Monika, you'll get used to it eventually~"
    "Watching Monika and Kotonoha having this cheerful conversation is actually relieving me."
    "Monika then goes to her purse, taking her notebook out as she pulls out a sheet of paper."
    m mp3_b "Okay everyone!~ Let's write our poems already!"
    kt 6bj "Well... I'll try..."
    scene black with wipeleft
    scene bg hotel3 with wipeleft
    "It's been a long time and I still don't know what to write my poem about... "
    extend "Well, it's been just 10 minutes actually, but it feels like an eternity."
    "Being with two beautiful girls Is kind of distracting."
    "Curiously enough, it seems that Kotonoha is doing well with her poem. Kind of sad for me though."
    "It seems like Monika is also doing alright with her poem. She is so talented with this kind of thing."
    window hide(None)
    window auto
    pause 2.0
    "Hm..."
    window hide(None)
    window auto
    pause 2.0
    "I got it! I'm gonna write a poem for both Monika and Kotonoha, to show my appreciation to both of them."
    "I think I can come up with something good."
    scene black with wipeleft
    scene bg hotel3 with wipeleft
    "Finally... I think it's looking good."
    call showpoem(mc_poem1, music=False) from _call_showpoem_13
    "It's the best I can do. I mean, it's not that bad I'd say."
    "Folding the sheet and putting it into my pocket, I stand up."
    mc "Alright girls, it's 10 PM already and the buses to my home take way too long to come. I'm gonna call it a day for now."
    show kotonoha 1bf at t11 zorder 1
    kt "Now for real, would you want to stay and sleep here?"
    mc "No, I'm heading to my home instead. Plus, there are just two beds."
    show kotonoha 1be at t21 zorder 1
    show monika mp1_a at t22 zorder 2
    m "We can sleep in the same bed again, [player]~"
    mc "Ahaha... No, I'm going home."
    m mp1_b "Oh... Alright then... See you tomorrow and goodnight~"
    kt 4ba "Goodnight [player]~"
    mc "Goodnight girls."
    stop music fadeout 2.0
    "As Kotonoha and Monika wave goodbye to me, I open the door and head outside."
    play sound closet_open
    scene black with wipeleft
    play sound closet_close
    play music hotel fadein 2.0
    "The carpet of the corridor is pretty soft, almost like snow. A warm snow though."
    "I hope I don't get lost... "
    extend "Ah! Here's the elevator."
    scene bg hotel2 with wipeleft
    "Phew... Today was kind of an active day and full of bad vibes everywhere."
    "Kotonoha is a really nice person by allowing Monika to stay with her. I'm really going to give it my best to make them all happy."
    "From now on, the happiness of 5 people are in my hands. I'm not going to fail again."
    "Mio? I don't care about her actually. As far as I can tell, she's trying to take Monika away from me."
    stop music fadeout 2.0
    "I really don't care if she leaves the club either. I know I'm being kind of mean here, but her behavior isn't befitting of her at all."
    "Unless she shows that she is really worth putting any effort into, I'm not changing my mind."
    "Ah well, I just want to get home, take a shower, and get some sleep..."
    scene black with dissolve_scene_full
    show text("{size=100}{color=#6debab}{b}Kotonoha, night 2{/b}{/size}{/color}\n{size=60}A girls night{/size}\n{size=60}with Monika.{/size}"):
        truecenter
    with Dissolve(1.0)
    pause 4.0
    scene bg hotel3 with dissolve_scene_full
    play music hotel fadein 2.0
    "[player] just left, leaving just Monika and I."
    "Wow... It was kind of a messy day...I can't believe [player] held me!"
    "Monika is right, [player]'s hugs feel so nice and warm, but now I'm concerned... Will [persistent.playername_b] come today now that Monika is staying with me?"
    mc_b "{i}Remember that I can hear every single thought in your head.{/i}"
    kt "Ah--!"
    "Monika, clearly startled, stares intently at me."
    show monika mp1_g at t11 zorder 1
    m "Are you ok? Did something happen, Kotonoha?"
    kt "N-no, I just... Um...I just remembered that I should talk to the recepcionist."
    m mp1_b "Well, should we go to the reception area then?"
    kt "Well, we could just use the intercom but yeah, it would be more proper if we went to the reception area."
    m "Ok, let's go then!~"
    "With that, Monika and I head out."
    play sound closet_open
    scene black with wipeleft
    play sound closet_close
    m "Where's the elevator?"
    kt "Over there."
    m "Oh! Sorry, the upholstery makes it kind of difficult to navigate."
    kt "Don't worry, I still get lost sometimes too."
    m "Mhm~"
    "And then, the conversation fades to an unsettling silence. I have to say that I'm happy that Monika is staying with me, My nights won't be so boring now."
    "I mean, I spend most of my day focusing on my homework and studies so I can free up my nights, but why? It's not like anybody ever invites me to hang out with them..."
    "And even if someone did, I would probably decline. I just want [player] to spend time with me..."
    "There's really something wrong with me... Am I obsessed with him?"
    mc_b "{i}Kotonoha, we need to talk.{/i}"
    kt "What do you want?"
    m "What?"
    kt "Oh! Sorry, um... Just forget it, I'm talking to myself."
    m "..."
    m "Okay, I guess..."
    mc_b "{i}This is the second time that you did that Kotonoha, I will punish you next time.{/i}"
    kt "{i}Y-yeah... I'm sorry.{/i}"
    mc_b "{i}So...{/i}"
    kt "{i}Not now, can we talk after I get this done?{/i}"
    mc_b "{i}...{/i}"
    mc_b "{i}Very well.{/i}"
    kt "{i}Thanks.{/i}"
    "As I was talking to [persistent.playername_b], Monika yells at me."
    m "Kotonoha!"
    kt "Ah--"
    m "Um... The elevator stopped 5 minutes ago..."
    kt "Sorry, I was thinking about my poem."
    m "Hm, I see. Well if you followed my advice then it should turn out fine, but i guess we'll see tomorrow if you're talented enough for this!"
    kt "Uhuhu~"
    kt "Well, let's go then."
    "Having said that, I step out from the elevator, walking with Monika to the reception area."
    scene black with wipeleft
    scene bg hotel with wipeleft
    "Monika cheerfully walks towards the recepcionist, he then notices us."
    python:
      n_name = "Recepcionist"
    n "Good evening ladies. Can I help you?"
    kt "Yes, please. This girl will be staying with me, can you please try registering her to my room?"
    n "Yeah, that shouldn't be a problem. The only thing I have to do is register your reservation again. Can I have your name?"
    kt "Sure, I'm Kotonoha."
    n "Room 308-C?"
    kt "Yes."
    n "Okay, I'm gonna take your previous reservation's information and make a new one."
    window hide(None)
    window auto
    pause 2.0
    n "..."
    n "Permanent stay?"
    kt "Just like before."
    n "Okay."
    n "So, two people then?"
    kt "Yes."
    window hide(None)
    window auto
    pause 2.0
    n "Hm..."
    n "Okay, it's done. You ladies can return to your room now."
    kt "Okay, thank you!"
    n "Goodnight."
    $ kt_name = "Koto & Moni"
    kt "Goodnight~"
    $ kt_name = "Kotonoha"
    $ n_name = "Natsuki"
    "The recepcionist is a very nice person... I really like seeing people enjoying their line of work."
    "I wish I can be as happy as him..."
    "While lost in my thoughts, Monika tugs at my sleeve."
    show monika mp1_b at t11 zorder 1
    m "Kotonoha, can we go to sleep already? "
    extend mp4_l "I'm kind of exhausted... Ahaha!~"
    kt "Well, actually I think I'm going to go for a walk."
    m mp4_d "..."
    m "Okay. "
    extend mp1_b "Just don't take too long okay? Remember that the hotel closes its doors at midnight."
    kt "Don't worry, I won't be longer than half an hour."
    m mp4_b "Okay, see you at the room then!"
    "As Monika waves goodbye to me, the elevator slowly closes its doors."
    "Well... Here we go, [player]..."
    "I leave the hotel and I notice the recepcionist smiling at me. I smile in return and head out."
    stop music fadeout 2.0
    scene black with wipeleft
    scene bg st3 with wipeleft
    "As soon as I'm outside, I head towards the bridge. Once there I take a few moments to enjoy the breeze flowing through my hair while I watch the traffic below me."
    "I then take a deep breath and close my eyes."
    scene bg st3 at bg_zoom
    with Dissolve(1.0)
    play music mend fadein 2.0
    kt "Now what?"
    mc_b "Well, a lot of things happened today."
    if persistent.kt_choice1 == 1:
      mc_b "You tried to tell Monika that you are aware that Yuri and her are old friends."
    else:
      mc_b "You managed to keep prudent when talking with Monika and [player]."
    if n_choice == 0 and persistent.kt_choice1 == 1:
      mc_b "You also asked Natsuki if she knows what this world is."
    if n_choice == 0:
      mc_b "You asked Natsuki if she knows what this world is."
    else:
      mc_b "You also remained silent with Natsuki about this world."
    if n_choice == 0:
      mc_b "Not to mention you talked about me to [player]."
    else:
      mc_b "Though you mentioned my name to [player]."
    mc_b "Do you have something to say?"
    kt "Well..."
    if persistent.kt_choice1 == 1:
      kt "I know that I made a mistake by almost telling Monika that I know about her friendship with Yuri."
    else:
      kt "I tried my best to not tell [player] and Monika about you."
    kt "But well... "
    if persistent.kt_choice1 == 1:
      extend "You stopped me with Monika."
    else:
      extend "I think that remaining silent will be a hard task. I'll keep trying though."
    if n_choice != 0:
      kt "As for Natsuki... I'll try not to tell her."
    else:
      kt "And yeah, I know I didn't do well by almost telling Natsuki about this world, but I swear I'll try harder."
    mc_b "Alright."
    mc_b "But if you do that again, I'm not going to show any mercy towards you. Got it?"
    kt "Yes [persistent.playername_b], I'm so sorry!"
    kt "I'm not gonna fail again."
    mc_b "I hope so. Don't make me regret choosing you instead of someone else."
    kt "I'll do my best."
    mc_b "Well, that's enough from me. Is there anything else I need to know before I leave?"
    kt "..."
    window hide(None)
    window auto
    pause 2.0
    kt "Yeah, there's something else actually. "
    kt "It's about a new girl, who just joined the Literature Club. Her name is Mio."
    mc_b "Mio?"
    kt "Yeah. She was a schoolmate of mine in the Music Club."
    mc_b "Hmm... What about it? Why should this concern me?"
    kt "I think she may know what this world really is. She was asking me a lot of questions about it."
    kt "She... "
    extend "She said something that got me worried."
    mc_b "What was that?"
    kt "\"You sort of remind me of someone\"."
    mc_b "Hm..."
    mc_b "These are just suspicions of yours, I think you're just being paranoid."
    kt "Perhaps, but I want to know whether her presence is a menace to this world or not."
    kt "Can you do some investigating about this?"
    mc_b "Well... "
    extend "{w=0.5}Alright, but don't get your hopes up though. You know I can barely do anything from here."
    mc_b "I'm leaving the difficult tasks up to you after all."
    kt "Alright... Understood."
    mc_b "Well, I think it's time for you to call it a day. You need to be ready for tomorrow."
    kt "Don't worry [persistent.playername_b]... I'm always ready."
    mc_b "Glad to hear that. Now go get some sleep."
    kt "Alright! Goodnight~"
    mc_b "Goodnight."
    stop music fadeout 2.0
    scene bg st3 with char_fade
    "The wind waving through my hair, I feel the determination that I began with."
    "I recall why I accepted this task... Not just for Monika, but for the others as well."
    "I'm ready for anything that may come up. I cannot lower my guard. I have to be ready for any suspicious moves Mio may make."
    "Even if Mio is an actual menace to this world, I'm gonna try to reach that happy ending. And if [player] wants me to be in that ending..."
    extend " Then I have no choice."
    " I know someday I can tell them who I was and what I am doing here. What I know and how much I know."
    "For [player]. For the girls. {w=0.5}For you, Naomi..."
    "Well, it's getting late already... Time to return and get some sleep."
    scene black with wipeleft
    scene bg hotel with wipeleft
    scene black with wipeleft
    scene bg hotel2 with wipeleft
    pause 2.5
    scene black with wipeleft
    pause 2.0
    scene bg hotel3_night with wipeleft
    show black onlayer front zorder 6:
      alpha 0.68
    with char_fade
    "Aaahh! Finally, the day is done. Woah, it's so dark in here."
    m "Um? Kotonoha?"
    kt "Yes, it's me Monika, no one else but you and I have the key remember?"
    m "Ahaha! True..."
    "Sitting on the bed, I take my dress off. Monika covers her face with her blanket when I take my stockings and blouse off."
    kt "Oh, what is it? Have you never seen anybody naked before?"
    m "W-well... I kind of thought you may get embarrassed like you did when [player] was here."
    kt "Not really, you're a girl after all. "
    kt "If [player] would have stayed, I would have to go to the bathroom to get dressed in my pajamas."
    m "Fair enough."
    window hide(None)
    window auto
    pause 2.0
    m "Hey, Kotonoha..."
    kt "Hm?"
    "As I was putting on a clean nightgown, Monika sits on the bed facing me."
    "she sighs very sadly."
    play music t10 fadein 2.0
    m "Well it's just...I really am trying to find happiness in this world, but it's really difficult..."
    m "Knowing there's someone I want to reach but I'm unable to do so, it kind of makes me feel sad."
    kt "Someone? Who may that \"someone\" be?"
    m "Well, it might be difficult to explain... There is a {i}person{/i} I really want to be with, but it's just impossible."
    kt "Oh... So, you are talking about that {i}someone{/i}."
    m "..."
    m "What?"
    kt "Hm... Nevermind."
    m "How deep is your knowledge of this world?"
    kt "Deep enough. No more, no less."
    window hide(None)
    window auto
    pause 2.0
    "After I finish brushing my hair, I climb into my bed and lie down."
    scene black with close_eyes
    hide black onlayer front
    m "Kotonoha?"
    kt "Yeah?"
    "Monika gets up from her bed and starts looking at me."
    m "I need some advice... How can I find happiness in this world?"
    kt "..."
    kt "Well... I really don't have an answer for that."
    kt "But, you wanna know something? [player] really wants to make you happy. Not just you; all of us as well."
    kt "Why [player] would want such a huge responsibility... I will never know."
    kt "But does it matter if this world isn't real? Does it matter if somebody wrote what we're saying? As long as it feels like it's real, then that would be enough for me."
    kt "Just go with the flow. If I were you, I would trust [player] to make me happy."
    kt "That's my advice. Go with the flow and accept your reality. Even if this world is not real, this is the reality you live in."
    m "..."
    m "I really try, but sometimes I feel empty Kotonoha."
    kt "Trust me, it would be better than trying to pursue something you know you can't reach."
    kt "Acting like this will make [player] worry and you don't want that, do you?"
    m "{i}*sigh*{/i}"
    m "Yeah... I suppose you're right..."
    kt "Just think like this: "
    extend "{w=0.5}everything will get better eventually."
    m "Okay... I'll try."
    stop music fadeout 2.0
    kt "Then let's get some sleep, we have a long day ahead of us."
    m "Mhm~"
    "Another day wraps up \"well\", but hopefully everything will be better tomorrow."
    if persistent.kt_choice1 > 0:
      $ persistent.kt_choice1 = 0
    else:
      $ persistent.kt_choice1 = 0
    scene black with dissolve_scene_full
    call act1_ch2_d2 from _call_act1_ch2_d2


































label act1_ch2_d2:
  show text("{size=100}{color=#6debab}{b}Day{/b}{/size}{/color}\n{size=60}2{/size}"):
      truecenter
  with Dissolve(1.0)
  pause 4.0
  scene black
  with dissolve_scene_full
  play sound clock
  window hide(None)
  window auto
  pause 5.0
  scene bg bedroom 
  with dissolve_scene_full
  "..."
  window hide(None)
  window auto
  pause 2.0
  "Wow, 8:05 AM. Well done [player], you almost broke your record."
  "Alright, now that I'm alone it would be better if I try waking up earlier... Whatever, I'm going to have breakfast."
  "But before I do that, I need to put my uniform on."
  window hide(None)
  window auto
  pause 2.0
  "I'm ready. I guess..."
  scene black with wipeleft
  scene bg kitchen with wipeleft
  play music nday fadein 2.0
  "..."
  "Oh, come on! I have nothing in my fridge at all? Dang... I guess I'll have to go shopping later."
  "And since I have nothing else, I think I'm going to have some cereal and fruit."
  play sound rphone
  window hide(None)
  window auto
  pause 2.0
  "Wha--?"
  "Another call THIS early? "
  "Now that I think about it, it's not like anybody ever really calls me"
  mc "Hello?"
  python:
    s_name = "???"
  s "{i}Good morniiiing [player]!~{/i}"
  mc "Uh? Sayori?"
  s "{i}Hm...Let me check my ID.{/i} "
  $ s_name = "Sayori"
  extend "{i}{w=0.5}Yep, it's me!{/i}"
  mc "It would have been easier if you said \"yes\" in the first place."
  s "{i}Ehehe~ I like messing around with you!{/i}"
  mc "Very funny Sayori. Ha ha ha. You see? I'm dying of laughter here, Call me an ambulance."
  s "{i}Eeehhh? You meanie!{/i}"
  mc "Heh."
  mc "Well, did something happen?"
  s "{i}Um... Not really. I just wanted to know if you are going to school with someone today...{/i}"
  mc "Maybe, I'm probably going to call Monika and Kotonoha, so the three of us might go to school."
  s "{i}Oh...I see...{/i}"
  "Sayori's cheerful voice becomes sadder in tone, So I think I should invite her to come with me."
  "Plus Kotonoha could get to know her a litte bit better."
  mc "Hey, Sayori."
  s "{i}Hm?{/i}"
  mc "Uhm... Do you want to come with me? I could introduce you to Kotonoha."
  s "{i}Hey, that's a great idea! I'm in!{/i}"
  mc "Alright, I'll be outside in 4 minutes or so."
  s "{i}Alrighty~{/i}"
  mc "Well, I'm calling Monika. See you Sayori."
  s "{i}Okay! See you [player]!{/i}"
  mc "Remember to have some breakfast this time."
  s "{i}Meanie!{/i}"
  "After I hang up, I dial Monika's number. Hopefully she picks up her phone..."
  window hide(None)
  window auto
  pause 2.0
  m "{i}Hello?{/i}"
  mc "Morning Monika! How did you sleep?"
  m "{i}I slept great! This hotel's beds are so soft and nice!{/i}"
  mc "With how expensive that hotel is, it would be a shame if they weren't."
  m "{i}You're right [player].{/i}"
  mc "Well, should I pick you girls up?"
  m "{i}Oh, of course! Kotonoha is getting dressed. I now know the secret to how she braids her hair.{/i}"
  mc "Really? Did she teach you how to do her braid?"
  m "{i}Well... Not really. When we were talking, I was watching her in a mirror while she was braiding her hair.{/i}"
  mc "Ah, I see."
  m "{i}Mhm~{/i}"
  mc "Oh, Sayori is coming with us by the way."
  stop music fadeout 2.0
  $ currentpos = get_pos()
  $ audio.nday = "<from " + str(currentpos) + " loop 0>eheart-music/Daytime.ogg"
  m "{i}...{/i}"
  m "{i}Sayori?{/i}"
  m "{i}W-well... Okay, I suppose...{/i}"
  mc "Hm? What was that?"
  m "{i}Sayori is still scared of me...{/i}"
  mc "And she will continue to be scared of you if you don't talk to her and apologize."
  m "{i}...{/i}"
  m "{i}Okay.{/i}"
  $ renpy.music.play(audio.nday, channel="music", fadein=2.0, tight=True)
  $ audio.nday = "<loop 0>eheart-music/Daytime.ogg"
  mc "Alright, then see you soon."
  mc "And remember: everything will be alright."
  m "{i}Okay...{/i}"
  m "{i}See you [player].{/i}"
  "After I hang up, I finish my cereal and put the bowl in the kitchen sink."
  stop music fadeout 2.0
  "I have a feeling today is going be a very long day..."
  "Well, I shouldn't make Sayori wait any longer. I grab my backpack and head out."
  scene black with wipeleft
  scene bg mc_hw with wipeleft
  play sound closet_open
  scene black with wipeleft
  play sound closet_close
  scene bg house with wipeleft
  play music t2 fadein 2.0
  "As always, Sayori is waiting for me outside her house. Once she sees me, she comes running towards me."
  show sayori 1r at t11 zorder 1
  s "Hellooooooooo [player]!"
  mc "Yo Sayori. How did you sleep?"
  s 2l "Well...I guess I slept ok more or less. Ehehe..."
  mc "..."
  mc "More or less?"
  s 2f "..."
  s 2g "Just forget it."
  mc "Okay, shall we go already?"
  s 4l "Okay!~"
  "Sayori starts following me after I show her which direction we need to go."
  scene black with wipeleft
  scene bg street with wipeleft
  "While we're walking, Sayori's cheerful self starts coming out, as well as her nice and child-like demeanor."
  "Even if she's faking it, I'm happy to see the Sayori I know."
  show sayori 1c at t11 zorder 1
  s "So, [player]... This Kotonoha girl, have you met her before?"
  mc "Well... Kind of. She helped me bring Monika back."
  s 1b "Um... "
  s 2g "Does that mean... she knows what this world really is?"
  mc "Yes, she does. If you ask me, Kotonoha is kind of a mysterious girl."
  s 2b "Mysterious? How so?"
  mc "Oh... Nevermind. I kind of rambled there."
  s 1f "Hm... "
  extend 1g "Okay. "
  extend 3b "Now where are we going?"
  mc "Keep going straight until you see a bridge."
  s 2a "Alrighty~"
  "Kotonoha... What are you up to...?"
  "She appeared out of the blue knowing who I am, I bet she also knows the others too."
  scene black with wipeleft
  scene bg st with wipeleft
  show sayori 1n at t11 zorder 1 
  s "That bridge, [player]?"
  mc "Yeah."
  "When me and Sayori get to the bridge, the sight of the enormous hotel fills our vision."
  s 4m "Woah! It's so big [player]!"
  mc "Yeah. The best part is climbing the stairs, especially if you're out of shape."
  s 4a "Ehehe~ "
  extend 2x "That's the hotel your friend is staying at?"
  "Sayori points at the hotel."
  mc "Yup."
  s 2o "Oooooh! Really?"
  s 2m "Wow! "
  extend 1n "That's one of the most expensive hotels in the city."
  mc "Also one of the best, don't forget it."
  s 1a "Yep. "
  extend 3x "I bet she's from a wealthy family if is she is staying at a hotel like this."
  mc "You think so?"
  s 3q "Mhm~"
  mc "Well... Actually I don't know. I barely know her, you know?"
  s 3y "Ehehe... "
  extend 3l "You're right, I guess..."
  mc "Well, let's go."
  s 1y "Yep!" 
  show sayori at thide
  hide sayori
  "Sayori and I both head to the bridge."
  "Holy crap, I really should start getting some more exercise. I barely managed to climb 15 stairs and I'm already exhausted."
  "These are the consequences of staying at home doing nothing but watching anime and playing video games."
  "Though physical exhaustion is nothing compared to the stress I am about go through..."
  "But well, it will be worth it to see 5 cute girls happy and smiling. As long as I manage to do that, then I can deal with this stress."
  scene black with wipeleft
  scene bg hotel with wipeleft
  "As expected, Kotonoha and Monika are already waiting for us in the waiting room."
  "It looks like they were having a nice conversation before we arrived."
  "Once they see me, they stand up from the couch and walk towards us."
  $ kt_name = "Koto & Moni"
  show monika 1b at h21 zorder 1
  show kotonoha 1c at h22 zorder 1
  kt "Good morning [player]!"
  $ kt_name = "Kotonoha"
  mc "Morning girls. Are you ready for school?"
  m 2k "Of course! Let's go~"
  "From behind, Sayori greets them."
  stop music fadeout 2.0
  show monika 1b at t31 zorder 1
  show kotonoha 1c at t32 zorder 2
  show sayori 1k at t33 zorder 3
  s "Good morning..."
  kt 4b "Oh... "
  extend 4d "G-good morning. You must be Sayori, aren't you?"
  s "Y-yeah... I'm Sayori. Nice to meet you Kotonoha."
  m 2p "...Good morning Sayori."
  show kotonoha 1w at t32 zorder 2
  s 1f "..."
  s 1g "Good morning Monika..."
  "God... I can literally feel the tension in the air. I think it's up to me to break up this unsettling environment."
  mc "Girls... We're going to be late for school if we stay here."
  kt 7a2 "Y-yeah... You're right, [player]..."
  mc "Then let's get going already."
  "Monika still looking away, gets her backpack and walks out of the hotel."
  "Sayori, Kotonoha and I do the same."
  scene black with wipeleft
  scene bg st with wipeleft
  scene black with wipeleft
  scene bg bus with wipeleft
  play music nday fadein 3.0
  "I hope we make it on time, we can't be late again, or else they won't let us get in the school."
  "The city environment is the only audible sound between us while we're waiting for the bus."
  show monika 2n at t11 zorder 1
  m "Well, do you guys have anything planned for today after school?"
  show monika 2m at t21 zorder 1
  show kotonoha 1e at t22 zorder 2
  kt "Uhm... "
  extend 2f "Well, maybe doing homework, studying and after that nothing. It's not like I'm the most important nor busy person after all."
  m 1n "What about you Sayori? Are you up to anything after school?"
  show monika 1n at t31 zorder 1
  show kotonoha 4a at t32 zorder 2
  show sayori 2g at t33 zorder 3
  s "Not really..."
  m "Oh... I-I see..."
  m 1b "And you [player]?"
  "..."
  mc "Well... Maybe some anime and video games."
  "You're a weeb [player]. A real weeb."
  m 2e "O-oh! Well... I was thinking that we all can hang out somewhere when school finishes."
  mc "\"We all\"?"
  m 3b "The five of us and you, [player]~"
  "What?! 5 girls and me hanging out around the city?"
  "It's almost like a dream! I really have to accept."
  mc "Well, I think that it's a great idea, it might help us forget everything that's been going on lately."
  m 2k "Okay! What about you Kotonoha?"
  kt 3f "Well, I don't think I can join you. I have to get my homework done."
  m 3b "We should have plenty of time to get our assignments done before school ends, then we can all go out!"
  kt 3a2 "Well, if that's the case, then I accept!"
  m 1b "We can even do our homework together!~"
  kt 5h "Oh! That's a great idea Monika!"
  m "Ahaha!~"
  extend 2b " Do you accept, Sayori?"
  "Sayori looks at me with a doubtful glance, I nod."
  "Still doubtful, Sayori accepts."
  s 2l "Okay... I'm in."
  m 1k "Good!"
  mc "Girls, the bus has arrived. We should ride this one."
  python:
    kt_name = "Everyone"
  kt "Okay!"
  python:
    kt_name = "Kotonoha"
  "With that, we all step on the bus."
  scene black
  with wipeleft
  scene bg st
  with wipeleft
  scene black
  with wipeleft
  scene bg street
  with wipeleft
  scene black
  with wipeleft
  scene bg residential_day
  with wipeleft
  scene black
  with wipeleft
  scene bg school_front
  with wipeleft
  "Aaaaahhhhhh... Nothing like walking around, feeling the soft breeze."
  mc "Hey girls, let's take the train next time okay? I hate the bus."
  show monika 1b at t11 zorder 1
  m "We'll do that for sure!"
  show monika 1b at t21 zorder 1
  show kotonoha 1a at t22 zorder 2
  kt "Yeah, I think it might be easier too."
  show monika 1a at t31 zorder 1
  show kotonoha 1a at t32 zorder 2
  show sayori 1k at t33 zorder 3
  s "Yeah..."
  "I can't help but notice Sayori's attitude when Monika is around... She's still scared of her evidently."
  "I just hope today's meeting with the others gets her to relax and enjoy herself a little."
  "Like I said: I just want everything back to normal."
  scene black
  with wipeleft
  scene bg corridor
  with wipeleft
  "As we get in the building, I notice Monika and Kotonoha standing to my left. They look like they're having a cheerful conversation."
  "Meanwhile Sayori is walking behind me. She doesn't say anything, even though it seems she wants to join their conversation."
  "As I get close to our classroom, I wait for Sayori before stepping in."
  mc "{i}You'll be alright Sayori... Just calm down.{/i}"
  "Sayori listening to me, starts nodding. I then talk to Kotonoha and Monika."
  mc "Alright, this is where we part ways. See you at the club then."
  show monika 5a at t11 zorder 1
  m "See you [player]!"
  show monika 5a at t21 zorder 1
  show kotonoha 1a 3a at t22 zorder 1
  kt "You know it~"
  mc "Okay, see you around."
  "With that, Sayori and I enter our classroom."
  scene black with wipeleft
  scene bg class_day with wipeleft
  "Before I can sit in my chair, Sayori stands in front of me."
  show sayori 1g at t11 zorder 1
  s "Uhm, [player]..."
  mc "Yeah?"
  s 3h "Well... I just wanted to know if that Kotonoha friend of yours is a reliable person."
  mc "What? Why are you asking that?"
  s 2h "I mean... Somebody who wasn't exposed to the epiphany isn't able to understand what we went through."
  "Looking away, Sayori stands straight."
  s 1k "Don't you think so, [player]?"
  mc "{i}*sigh*{/i}"
  # here
  mc "Kotonoha went through the epiphany too, Sayori."
  s 2b "Oh Really?"
  mc "Yeah. She wouldn't have brought Monika back for no reason to begin with."
  s "Well... That makes sense..."
  mc "So yeah, don't worry. We can believe in Kotonoha."
  s 1d "If you say so..."
  python:
    mi_name = "???"
  mi "Oh, [player]!"
  mc "Gh--"
  "Turning around, I meet Mio who is sitting 4 desks behind me."
  "She wasn't here earlier... Was she?"
  python:
   mi_name = "Mio"
  mc "What a nice surprise to see you here, Mio."
  show sayori 1b at t21 zorder 1
  show mio 7e at t22 zorder 1
  mi "Right? My father is in charge of all my class changes!"
  s 2c "Huh? Why would you change to our class?"
  mi 5a "Well, me and [player] made a bet yesterday. Since [player] was talking about me with Monika, he said that he was willing to do whatever I want when that happens again."
  mc "But I didn't--"
  mi 1e "Soooo to make sure he isn't doing that again, I asked my father to change my class."
  mi 2a "By the way [player], I didn't know Monika was your girlfriend~"
  "God... This girl..."
  mc "She's not my girlfriend yet."
  mi 2g "Oh... I'm sorry. "
  extend 4e "So, is there someone you're into?"
  mc "I'm not telling you anything Mio."
  mc "Are you finished already? I was talking to Sayori."
  mi 6h "Ehhh? But I wanted to join your conversation too!"
  mc "So, Sayori..."
  "As I ignore Mio, Sayori looks at her. I thought she would ignore her too, but Sayori's sweet personality is something that will never change."
  s 1i "[player], don't be a meanie! She's a clubmate of ours in the Literature Club!"
  mc "Unfortunately we're not in the clubroom, so we can quit being hypocritical."
  mi 1h "..."
  mi 5k "Okay, I'm leaving then."
  show mio at rhide
  hide mio
  show sayori 3i at t11 zorder 1
  "Saying nothing else, Mio returns to her desk."
  "Sayori watches her go back to her desk, and once Mio returns, Sayori turns to see me."
  s 2j "That was so mean [player]!"
  mc "You'll understand soon Sayori. {i}*shrugs*{/i}"
  play sound school_ring
  window hide(None)
  window auto
  pause 4.0
  mc "Alright... The class is starting."
  s "Uh-huh. Bye [player]."
  show sayori at lhide
  hide sayori
  "Sayori returns to her desk kind of pissed off."
  "I don't know why I upset her, Mio isn't somebody to worry about. But well, it's Sayori we are talking about..."
  "Hopefully I will make her understand why I dislike her. Sometime soon."
  stop music fadeout 2.0
  scene black with dissolve_scene_full
  show text("{size=100}{color=#6debab}{b}Meanwhile on{/b}{/size}{/color}\n{size=60}Kotonoha's classroom{/size}"):
      truecenter
  with Dissolve(1.0)
  pause 2.0
  scene bg kt_classroom with dissolve_scene_full
  play sound school_ring
  window hide(None)
  window auto
  pause 4.0
  "..."
  "Phew... The class has finally finished... It was about time."
  "While walking to our respective classrooms, me and Monika were talking about what happened last night."
  play music t6 fadein 2.0
  "It seems that she's more relaxed now, which is also a relief to me."
  "Monika also invited me to hang out with her and the others, I'm feeling anxious about this already."
  "I can't believe I'll be hanging out with [player]! I can't describe this happiness that I'm feeling..."
  "Even if it's not gonna be just the two of us, I'm still happy! I can't help but feel nervous."
  $ am_name = "???"
  am "Hey you."
  kt "Ah--!"
  am "What? Did I ruin your perfect daydream?"
  "While lost in my thoughts, a brown-haired girl with yellow eyes who is about as tall as Sayori appears."
  "The description fits well for a girl I met in \"the other world\". Her name is Aimi."
  "You can say she was a \"friend of mine\", but not as good of a friend like Naomi was."
  show aimi 1b at t11 zorder 1
  am "Are you going to respond to me anytime soon?"
  kt "Oh! Y-yeah... I'm sorry!"
  am 4b "Finally."
  am 2c "Do I know you or something? I kinda feel like I've seen you somewhere already."
  "..."
  "Why?! Just why?! Is Aimi self-aware too?!"
  "Not to mention that Mio didn't come to class today..."
  "This is just wrong!"
  kt "W-well... I don't t-think so. I'm a new student here."
  am "Hm... I see. "
  extend 4a "Whatever, what's your name girl?"
  kt "I-I'm Kotonoha."
  am 1a "Kotonoha? Huh... Isn't that a Japanese poetry style? "
  extend 4a "Whatever, I'm Aimi. "
  $ am_name = "Aimi"
  extend 2a "Nice to meet you."
  "I met Aimi in the bathroom, so she really doesn't impress me."
  "As I said, we used to talk every now and then. Having said that, I have to say that she wasn't an actual friend of mine."
  "I don't know why, but she kind of used to make fun of Naomi; that's why she has earned my disdain for her." 
  "But she's a nice person after all."
  am "Where are you living at?"
  kt "Well... I'm living in that hotel located downtown."
  am 4b "Oh, really? That's a really expensive one."
  am 4h "Then tell me, why are you in a public school then, you rich girl?"
  "..."
  "She just called me a... \"rich girl\"?"
  kt "I-I'm not a rich girl!"
  am 1g "Living in such an expensive hotel, I don't know what you are then..."
  am 1a "Whatever, I didn't come to argue. I just... kind of wanted to get to know you a little bit, since you kind of remind me of someone."
  "Odd. Aimi is kind of a troublemaker."
  "Not that she was with me, we used to get along ok."
  "Not as good as with Naomi though."
  am 2v "By the way, you look cute in that dress you were wearing yesterday. Very girly looking, but cute anyways."
  kt "W-well... Thank you."
  am 4v "Hahaha! Doncha worry, I'm not harassing you. I'm just interested in you."
  am 2b "Quit stuttering like that by the way."
  kt "Yeah... I'm sorry..."
  show aimi 2b at t21 zorder 1
  show natsuki 4b at t22 zorder 1
  n "Hey! Leave her alone!"
  am 2y "Huh? I'm just talking to her! Don't think for a second you're that important."
  am 4y "You suck Natsuki! Whatever, see you later {i}Kotonoha{/i}."
  "With that, Aimi walks away."
  stop music fadeout 2.0
  show aimi at thide
  hide aimi
  show natsuki 4b at t11 zorder 1
  "On the other hand Natsuki sees Aimi leaving. As she sits, Natsuki \"yells\" at me."
  play music tnatsuki_c fadein 2.0
  n 2b "Are you a dummy or something? Why are you even talking to her?"
  kt "Why not?"
  n 2v "Don't do it!"
  kt "But she didn't do anything to me!"
  kt "And just so you know, I'm old enough to do whatever I want, am I not?"
  n 3g "Hmph."
  "Natsuki changes her expression and her voice starts to break."
  "She sighs and stares at me."
  n 1n "Kotonoha...I just wanted to apologize to you because of everything I said yesterday..."
  n 1o "But you have to understand me, I didn't expect you to know who Monika was!"
  kt "..."
  kt "No Nat, it was my fault for lying to you..."
  kt "It's just that I thought it would be better if you girls didn't know that."
  n 3q "Well... Thank you, "
  extend 3b " but that doesn't mean I'm gonna accept Monika's \"apologies\"."
  n 3h "I just felt bad for everything that I said {b}to you{/b}."
  kt "Okay! It's not like I can blame you."
  "Natsuki goes to take her backpack from the chair she was at and comes back to me."
  "She then points to the table to my left."
  n 1t "W-will it be okay with you if I sit here?"
  kt "O-oh! Of course."
  "With that, Natsuki sits down."
  "Will Natsuki know why Mio isn't here today?"
  kt "Hey, Nat?"
  n 1c "What?"
  kt "Um... Do you know why Mio didn't come to class today?"
  n "Not really."
  extend 1k " It's not like I care about her or anything."
  kt "Oh... "
  show natsuki 2k at t11 zorder 1
  extend "I see."
  n 2a "Yeah."
  kt "Well... Is there a reason why you dislike her?"
  n 2w "She's so annoying! She thinks she is a know-it-all and fakes concern for other people."
  kt "Well... "
  extend "Actually she seems to be a really kind person for me."
  "Staring at me for a moment, Natsuki sighs."
  n 2c "Kotonoha, I think that you have to quit thinking that everybody in the world is a good person. The world just doesn't work like that."
  kt "I know... But Mio is being very kind towards me."
  n "She isn't, I know her better than you."
  kt "..."
  kt "Okay..."
  stop music fadeout 2.0
  show natsuki at thide
  hide mio
  "I want to tell her that I already know Mio, but it would be counter-productive at this time."
  "If Mio left, then it would be fine. But if not...I need to investigate why this is happening..."
  play sound nday fadein 2.0
  play sound school_ring
  window hide(None)
  window auto
  pause 4.0
  "Well, here we go again. Wait for me, [persistent.playername_b]..."
  scene bg class_day with dissolve_scene_full
  "It's been quite a while since class started again. I want it to end already since Mio is here."
  "She's just staring at me while smiling, but everytime I try to look at her she just blushes and looks away, Sayori notices this as well."
  "Hopefully Sayori will understand why I am trying to avoid Mio."
  "This is the final class: English. I kind of hate English, it's a very messed up language. I would prefer learning Spanish or something."
  "Fortunately the class is about to finish."
  play sound school_ring
  window hide(None)
  window auto
  pause 4.0
  "Aaahh... Finally!"
  "Putting my belongings in my backpack as quickly as I can, I walk towards Sayori."
  mc "You ready, Sayori?"
  show sayori 2l at t11 zorder 1
  s "Sure, I suppose."
  mc "Well, let's get going then before Mi--"
  show sayori 2l at t21 zorder 1
  show mio 1h at t22 zorder 1
  mi "[player], I just want to apologize to you..."
  "Before I can finish my sentence, Mio rushes towards me while Sayori looks away."
  mc "Hm? Why?"
  s 2l "Um... [player], I think it would be better if I go to the club already..."
  show sayori at thide
  hide sayori
  mc "Eh?! No, wait!"
  show mio 1h at t11 zorder 1
  "I tried to reach Sayori, but Mio stands in front of me blocking the way."
  mc "{i}*sigh*{/i}"
  mi 3h "So... Do you accept my apology?"
  mc "What are you apologizing for?"
  mi 3e "Because the generous side of myself is gonna pardon you for acting rude towards me!~"
  mc "{i}*sigh*{/i}"
  mc "Whatever, I'm heading to the club."
  mi 8e "I'm coming with you~"
  mc "Mhm."
  "Saying no more, I leave the classroom ignoring Mio, but she catches up to me."
  "I don't know if she's too fast or I'm too slow."
  scene black with wipeleft
  scene bg corridor with wipeleft
  "Once out, Mio walks close to me."
  "Humming a song, Mio cheerfully comes even closer to me while we go to the clubroom."
  mc "We're here."
  show mio 4e at t11 zorder 1
  mi "Yes!~"
  stop music fadeout 2.0
  scene bg club_day with wipeleft
  "As we get in the classroom, Sayori is with Yuri looking for something in the closet."
  "But Kotonoha nor Natsuki are here yet."
  play music t3 fadein 2.0
  "Monika cheerfully comes to me and greets me."
  show monika 5a at t11 zorder 1
  m "Hello [player]!~"
  mc "Hey Monika, is everybody here already?"
  m 2l "Well... Not really. Kotonoha and Natsuki are not here yet."
  mc "Oh... I see. Well, do you know where they could be at?"
  m 3d "I saw them together during the recess, so they're probably still in the school somewhere. "
  extend 3b "I bet they fixed their problems already~"
  show monika 3b at t21 zorder 1
  show mio 3e at t22 zorder 1
  mi "Hello Monika!"
  "Suddenly, Mio pops up out of nowhere, interrupting our conversation yet again."
  m 2c "..."
  m 2g "Hello."
  mi 7f "So, are we doing poems today?"
  m 4b "Yeah, did you even write yours?"
  mi 5x "Oh, of course I did! "
  extend 1e "Who do you think I am?"
  m "Hm... "
  extend 3n "Nevermind. Let's wait for Kotonoha and Natsuki."
  show monika at thide
  hide monika
  "With that, Monika returns to her desk and resumes whatever she was doing."
  show mio at rhide
  hide mio
  "Mio finally gives me a break by going to take a seat at the end of the classroom."
  "I take a seat myself."
  "So... Kotonoha and Natsuki were together during the recess..."
  "Well, hopefully they fixed their problems. Problems that I caused to begin with."
  scene black with wipeleft
  scene bg club_day with wipeleft
  "Monika was writing down something while we are waiting for Kotonoha and Natsuki, and she seems to be happy."
  "I don't know if I'll distract her if I go to her..."
  "Well, I guess it wouldn't hurt to try talking to her."
  "I walk towards Monika, she raises her head while smiling."
  show monika 2b at t11 zorder 1
  m "Hello [player]~"
  mc "Hello again. Um... Am I interrupting something?"
  m 3b "Not really, I was just editing my poem but I'm done now."
  mc "Ah, I see."
  m "Are you up to something [player]?"
  mc "Not really, that's why I came to talk to you. Are you doing alright?"
  m 2e "Ahaha! I see. "
  extend 3b "Yeah, I'm alright - I was talking with Kotonoha last night."
  mc "Oh? What about?"
  m 1a "I can't tell you, "
  extend 5a "girl stuff~"
  mc "Huh... "
  extend "Alright then."
  m 3k "Ahaha!~"
  mc "And how are you feeling?"
  m 2l "Still kind of worried, but I'm trying to stay as calm as possible."
  mc "Awesome!"
  m 1k "After all, I have to be grateful to you!"
  m 3n "And I also want them to trust me..."
  mc "Fair enough."
  "The clubroom door opens, and Kotonoha and Natsuki both step in."
  "Kotonoha greets Monika while smiling. Natsuki just ignores us."
  "I can see that Kotonoha is very happy, but Natsuki isn't changing her attitude."
  show monika 3n at t21 zorder 1
  show kotonoha 7c at l22 zorder 1
  kt "Hello Monika!"
  m 3b "Hey Kotonoha! May I know why you are this late?"
  kt 4v "W-well... It's hard to explain..."
  "Kotonoha discreetly looks at Natsuki, Monika understands where she's coming from, so she avoids asking."
  m 2b "Well, go get ready. It's time for the club activities."
  kt 6k "Mhm~"
  n "Whatever."
  show kotonoha at thide
  hide kotonoha
  show monika 1q at t11 zorder 1
  "Kotonoha and Natsuki makes their way to two empty tables. I do the same myself."
  "Before she says anything, Monika places her hands on her cheeks and slaps herself."
  m 1q "{i}*sigh*{/i}"
  m 2n "O-okay everyone! I hope you all have brought your poems, because it's time to share them!"
  "With that, everyone starts to take their poems out. I take mine from my pants pocket."
  "Hopefully everything will turn out well..."
  jump poemresponse_start_d2

label act1_ch2_d2_p2:
  scene black with wipeleft
  scene bg club_day with wipeleft
  "Phew... Finally the day is over."
  "Poem sharing went well so far. If it weren't for Natsuki's stubbornness, we probably would be having fun like we used to."
  "Well, it's not like I can blame her, but...Talking to her is very frustrating sometimes."
  play music t3 fadein 2.0
  "On the other hand, it seems that we're gonna be finishing today's meeting on a high note."
  "Everyone is doing something different while I'm just sitting on my chair by myself."
  "Kotonoha is, like usual, talking to Monika."
  "Yuri, Sayori and Mio are talking and hanging out across the clubroom."
  "And Natsuki is... Well, sitting on the floor reading her manga \"Parfait Girls\"."
  "I can't help but notice how stubborn Natsuki is behaving right now. I mean,  I understand why she's being like that but..."
  "...but it's becoming ridiculous."
  "Will it be okay if I go talk to her?"
  "Well, I don't think it would hurt to try."
  scene black with wipeleft_scene
  scene bg closet with wipeleft
  "Natsuki is lying against the wall while reading her manga. Once I get there, she stares at me for a while, getting back to her book seconds later."
  "Unfortunately for her, I'm a persistent person and I'm not giving up anytime soon."
  "Natsuki realizing my persistence, sighs and closes her manga as she locks her gaze on me."
  show natsuki 1b at t11 zorder 1
  n "What? Did you miss anything?"
  mc "I don't know. Probably."
  n 1g "Hmph."
  n 2e "What do you want? I'm too busy to listen to your fairy tales."
  mc "I just wanted to talk about what we were discussing when sharing poems."
  n "I said I'm gonna consider it, now get lost!"
  mc "But I--"
  n 2w "I said get lost!"
  mc "..."
  n 2b "I'm done with you."
  mc "Well... Okay then..."
  show natsuki at thide
  hide natsuki
  "Saying nothing else, Natsuki resumes reading her manga."
  "God...This is gonna be difficult..."
  "What if I tell Kotonoha to talk to her instead of me? Natsuki and her get along so well."
  "It might work..."
  "Well... It's not like I have a choice here."
  scene black with wipeleft
  scene bg club_day with wipeleft
  "Monika and Kotonoha are still cheerfully talking while sitting at two tables they slid together."
  "I'm kind of curious... What are they talking about?"
  "Well... As Monika said: \"girls stuff\"."
  "I walk closer to Kotonoha and as she notices me, both girls stop laughing and Kotonoha starts staring at me."
  show kotonoha 1a at t21 zorder 1
  show monika 1a at t22 zorder 1
  kt "Oh! Hello [player], how are you?"
  mc "Hello again. I'm doing fine."
  kt 2a "Did something happen?"
  mc "Yeah, but before that...Am I interrupting anything?"
  kt 7a2 "W-well...Kinda... "
  extend "But even so, what happened?"
  mc "I would prefer if we talk outside, just the two of us."
  kt 4e "..."
  show kotonoha 7e at t21 zorder 1
  show monika 1c at t22 zorder 2
  "Monika and Kotonoha stare at each other, Kotonoha then nods and stands up."
  show kotonoha 4c at t21 zorder 1
  kt 4c "Well...Be right back Monika."
  show monika 2e at t22 zorder 2
  m 2e "No worries. We'll continue this later~"
  "With that, Kotonoha and I both head out of the classroom. As I open the door, I let Kotonoha step out first."
  scene black with wipeleft
  scene bg corridor with wipeleft
  "Kotonoha closes the door delicately as she leans against the door."
  show kotonoha 2e at t11 zorder 1
  kt "What is it [player]?"
  mc "Well...I wanted to talk to you about Natsuki."
  kt 4f "Natsuki?"
  mc "Yeah. She has been kind of rude towards me, refusing to talk with me as well."
  kt "Yeah..."
  mc "And I wanted to ask you a favor. Can you talk to her? You two get along so well."
  kt 1e "What would I talk to her about?"
  mc "Monika's meeting after school. Can you?"
  kt 7e "Hm..."
  kt 5f "Well, I can try..."
  mc "You're the only one who can do it, since she isn't acting so rude towards you."
  kt 5d "Well... Okay [player]~"
  extend 7e "That's it?"
  mc "Yeah. I can stay with Monika while you talk to her."
  kt 5a "Okay~"
  mc "Then let's go."
  "Kotonoha happily nods and opens the door."
  scene black with wipeleft
  scene bg club_day with wipeleft
  "We both head back to the desks Monika and her were sitting at."
  "As we do so, Kotonoha has a very cute smile on her face. I note that everytime I'm with her."
  "This does confirm that Kotonoha has a crush on me, but why? Why would she love me?"
  "I don't get it."
  show kotonoha 2d at t11 zorder 1
  kt "We're back~"
  show kotonoha 2d at t21 zorder 1
  show monika 1b at t22 zorder 1
  m "Oh! "
  extend 3b "What were you guys talking about?"
  kt 3f "Uhm... Natsuki."
  m 1d "Oh... I see... "
  extend 2e "Why didn't you guys talk about that here with me?"
  mc "You forgot that Natsuki is over there."
  "I smoothly point to the window."
  m 2l "Ahaha!~Y-yeah, you're right..."
  kt 3a "Well, I'm gonna talk to Natsuki then. [player] will stay here for a while."
  m 5a "Okay~"
  mc "Alright, so let's go."
  show kotonoha at thide
  hide kotonoha
  show monika 5a at t11 zorder 1
  "Kotonoha nods and makes her way to Natsuki, letting myself sit down."
  "In fact, now that I think about it...Kotonoha only seems to get along well with Monika and Natsuki..."
  "I wonder if she does with Mio..."
  m 2b "So, [player]... What do you want to talk about?"
  "Well... Hopefully Kotonoha will get through to Natsuki..."
  stop music fadeout 2.0
  scene bg club_day with dissolve_scene_full
  "[player] asked me to talk with Natsuki."
  "Actually I don't understand how stubborn of a person Natsuki could be, since she's not like that with me..."
  "I come to the conclusion that it's because of what happened yesterday nonetheless..."
  "I need to think of something that would make Natsuki calm down a little."
  "Whatever, I come closer to Natsuki, who is reading manga."
  kt "Hello Nat."
  play music tnatsuki_c fadein 2.0
  show natsuki 1c at t11 zorder 1
  n "Oh, hi Kotonoha."
  kt "Can I sit next to you?"
  n 2c "Weren't you talking with Monika?"
  kt "Yeah, well... I--"
  n 4c "I don't need you to lie Kotonoha, [player] asked you to talk to me, didn't he?"
  kt "{i}*sigh*{/i}"
  n "What?"
  kt "Um...It's nothing..."
  kt "Ehm..."
  "This time I sit next to Natsuki without asking."
  scene n_cg1_3 with char_fade
  "Natsuki stares at me for a bit before talking again."
  n "I didn't say you can sit there!"
  kt "You didn't say I can't either."
  n "Hmph."
  n "What?"
  kt "Well..Actually I want to talk to you about Mio..."
  "I mean, she appeared in the club, but she didn't come to class today."
  "She wasn't at the classroom at least."
  scene n_cg1_1 with char_fade
  n "Oh..."
  n "Well, I heard that her father changed her to [player]'s classroom."
  kt "Her father? Who is her father?"
  "That's some information I don't know about for real."
  n "{i}*shrug*{/i}"
  n "I've heard it's the principal, though I'm not sure."
  kt "Oh, really?"
  n "Yeah. Supposedly."
  kt "Oh... I see."
  n "Why?"
  kt "Oh! It's nothing, I just think that it's kind of odd that her father changed her classes for no reason."
  n "Besides, why are you that concerned for Mio? Aren't you happy she left our group?"
  kt "No. I'm not sad for that either."
  n "Uh? What is that supposed to mean?"
  kt "All I can say about it is that I don't care."
  n "Ah... I see."
  kt "Yeah."
  scene n_cg1_4 with char_fade
  n "It would have been better if she would have left the school."
  n "What do you think?"
  kt "{i}*shrugs*{/i}"
  n "Are you finally following my advice?"
  kt "Not really... But I prefer staying away from problems."
  n "You're so weird, Kotonoha..."
  kt "I love you too Nat."
  "Natsuki stares at the wall, just focusing on it."
  "I think the conversation is going pretty good so far. I think it's time to tell her what I came here for."
  kt "So... Natsuki?"
  n "Yeah?"
  kt "Um..."
  kt "I want to ask you something."
  n "What is it?"
  kt "Well, today Monika did organize a meeting after school and she invited everybody... And you're included too."
  kt "Then, I would wa--"
  scene n_cg1_2 with char_fade
  n "I told [player] that I'll consider it!"
  kt "Oh...Will you?"
  n "Well...Yeah...That's what I'm trying to tell that dummy!"
  kt "Ah. I think that you should start being straightforward with him."
  scene n_cg1_4 with char_fade
  n "That dummy doesn't deserve it. "
  scene n_cg1_3 with char_fade
  extend "Why does he allow her to walk around and pretend nothing happened?! I don't get it!"
  kt "Sometimes it's better trying to trust. Trust and give people a second chance."
  kt "Despite the situation."
  n "It's easy for you to say that! You don't know what she did to all of us."
  "Somehow I do know what happened, but I can't imagine the pain they went through."
  "But even so, it's my task to recover the already collapsed Literature Club and write a happy story."
  "Not just for Monika, but for the others as well. Monika says that happiness cannot be found here."
  "I'll prove her wrong."
  "We need to walk down a rainy day before watching the beautiful rainbow in the sky."
  "I pat Natsuki's head before standing myself up."
  scene n_cg1_2 with char_fade
  n "Uwa--!"
  n "W-what did you just do?! You're looking for a trip to the hospital, aren't you?"
  kt "No."
  n "Do I look like a dog?!"
  kt "No. I just wanted to pat your head."
  n "D-don't do that again!"
  kt "Uhuhu~"
  kt "Alright then. So, will you be there?"
  n "Um... Well... Okay. "
  extend "I'll be there."
  stop music fadeout 2.0
  kt "Okay!"
  "Finally Natsuki stands up."
  scene bg club_day with dissolve_scene_full
  kt "Let's go get a seat, Natsuki."
  show natsuki 1a at t11 zorder 1
  n "Yeah."
  "Well, with this I've done what was supposed to be [player]'s task."
  "Hopefully it will go well."
  scene bg club_day with dissolve_scene_full
  play music t3 fadein 2.0
  "The club day is coming to an end."
  "Kotonoha has finished talking with Natsuki since they both are sitting at their chairs already."
  "Hopefully we'll be free of Mio for some time - who is still talking with Yuri and Sayori."
  show monika 3b at t11 zorder 1
  m "Okay everyone!~ The club meeting has finished already, so it's time to call it a day~"
  m "Did you all have fun?"
  show monika 3b at t21 zorder 1
  show yuri 1j at t22 zorder 2
  y "Y-yes, I had fun sharing poems again..."
  show monika 3b at t31 zorder 1
  show yuri 1j at t32 zorder 2
  show sayori 1d at t33 zorder 3
  s "I had fun talking with Yuri and Mio too!"
  show monika 3b at t41 zorder 1
  show yuri 1j at t42 zorder 2
  show sayori 1d at t43 zorder 3
  show mio 2e at t44 zorder 4
  mi "Mhm~"
  show monika 3b at t51 zorder 1
  show yuri 1j at t52 zorder 2
  show sayori 1d at t53 zorder 3
  show mio 2e at t54 zorder 4
  show natsuki 4c at t55 zorder 5
  n "Whatever."
  m "Well, shall we get going already then?"
  mi 1e "Okay!~"
  mi "See you all in one hour then!"
  show mio at rhide
  hide mio
  show monika 3f at t41 zorder 1
  show yuri 1g at t42 zorder 2
  show sayori 1d at t43 zorder 3
  show natsuki 4c at t44 zorder 4
  "With that, Mio takes her backpack and heads out of the classroom."
  "..."
  "How did Mio know that?"
  m 2f "Um..."
  s 5a "Ehehe..."
  mc "Huh? What was that, Sayori?"
  s 5b "W-well...I kind of mentioned it accidentally while we were talking to her..."
  show sayori 1l at t43 zorder 3
  m 1q "{i}*sigh*{/i}"
  mc "Oh well...I think we have no choice but to take her with us."
  m 1r "Yeah..."
  y 2q "Well...I-I think that I'm coming with you guys."
  n 2c "Me too."
  m 2k "Oh, that's great! Then, see you all at..."
  mc "...my place?"
  n 2w "Ha! You won't."
  show monika 2k at t51 zorder 1
  show yuri 2q at t52 zorder 2
  show sayori 1l at t53 zorder 3
  show natsuki 4c at t54 zorder 4
  show kotonoha 7e at t55 zorder 1
  kt "How about our place, Monika?"
  m 1b "Ahaha!~ That's a good idea, Kotonoha~"
  m 3b "What do you girls think?"
  y 1u "It's okay for me."
  s 2l "Same~"
  n 1c "As long as it's not at [player]'s place."
  kt 4h "Okay! See you there then~"
  "With that, we all leave the clubroom."
  scene black with wipeleft
  scene bg corridor with wipeleft
  "Now that I think about it, Mio doesn't know where we are going to gather..."
  "Meh, it's not like she'll know it. It's not like she's self-aware or anything."
  stop music
  scene black with dissolve_scene_full
  voice "mod_assets/mio/mi_vc1.ogg"
  $ pause(3.0)
  #mi "That's.. what you think.."
  voice "mod_assets/mio/mi_vc2.ogg"
  $ pause(4.0)
#  mi "That's what you think..."
  scene bg mc_lr with dissolve_scene_full
  "It's been a long time since we left the school."
  "I'm done with my homework already. How did I do it that fast?"
  "Well, basically I didn't have math class. With that said, I'm just chilling on the couch."
  "Rarely do I ever feel like something good will come up when today's meeting finishes."
  "It's kind of odd, but I think everything will turn out just fine."
  "Well...I think that I'm gonna watch some TV."
  scene black with wipeleft
  scene bg mc_lr with wipeleft
  window hide(None)
  window auto
  pause 2.0
  "Oh! An anime I was looking for. Regularly I barely manage to watch a full chapter, but it seems that it's just starting."
  "Aaaaahhhhhh...How good it feels to be lying on the couch doing nothing..."
  $ ad = 40.0
  $ ac = 1.0
  "..."
  $ ac += 5.0
  show black at malpha(ac / ad) onlayer front:
    truecenter
  "...I'm feeling sleepy..."
  $ ac += 5.0
  show black at malpha(ac / ad) onlayer front:
    truecenter
  "..."
  $ ac += 5.0
  show black at malpha(ac / ad) onlayer front:
    truecenter
  "No [player], you can't fall asleep..."
  $ ac += 5.0
  show black at malpha(ac / ad) onlayer front:
    truecenter
  "..."
  $ ac += 5.0
  show black at malpha(ac / ad) onlayer front:
    truecenter
  "I--"
  scene black
  hide black onlayer front
  $ mi_name = "???"
  $ m_name = "???"
  $ kt_name = "???"
  "..."
  play music t6s
  mi "{alpha=0.1}[player]!{/alpha}"
  "{i}*yawn*{/i}"
  "..."
  "I hear a voice in the distance."
  "I swear I was lying on my couch..."
  voice "mod_assets/mio/mi_vc1a.ogg"
  mi "{alpha=0.1}Finally...{/alpha}"
  mi "{alpha=0.1}[player]...{/alpha}"
  voice "mod_assets/mio/mi_vc1b.ogg"
  mi "{alpha=0.1}It's been a long time hasn't it?~{/alpha}"
  mc "Huh? Who is this?"
  voice "mod_assets/mio/mi_vc1c.ogg"
  mi "{alpha=0.1}That's not important.{/alpha}"
  "This female voice is barely audible... I barely understand what she is saying."
  "It's a low-pitched voice. Who could this voice belong to?"
  "Is this a nightmare? It must be..."
  "Is Monika...? "
  extend "Impossible! Monika promised that she wouldn't do that again!"
  voice "mod_assets/mio/mi_vc1d.ogg"
  mi "{alpha=0.1}Don't worry [player], I'm not Monika.{/alpha}"
  mc "..."
  mc "Who are you then?"
  voice "mod_assets/mio/mi_vc1e.ogg"
  mi "{alpha=0.1}Your number one admirer~{/alpha}"
  mc "What? Show yourself!"
  voice "mod_assets/mio/mi_vc1f.ogg"
  mi "{alpha=0.1}Uhuhu~ I don't think I will.{/alpha}"
  show screen invert(0.5, 0.1)
  voice "mod_assets/mio/mi_vc1g.ogg"
  mi "{alpha=0.1}Unfortunately you can't know who I am either.{/alpha}"
  "..."
  mi "{alpha=0.1}[player], "
  voice "mod_assets/mio/mi_vc1e2.ogg"
  extend "don't you think that it's awesome that we're finally alone?{/alpha}"
  voice "mod_assets/mio/mi_vc2a.ogg"
  mi "{alpha=0.1}Nobody else is here. Just the two of us...{/alpha}"
  "What am I doing here?"
  "Where's everyone?"
  "I can't move my hands!"
  "What if I try screaming?"
  voice "mod_assets/mio/mi_vc1j2.ogg"
  mi "{alpha=0.1}Uhuhu~ Do whatever you want, you can't leave this place!{/alpha}"
  voice "mod_assets/mio/mi_vc1k2.ogg"
  mi "{alpha=0.1}I'll do everything I can for us to be together!{/alpha}"
  #  mi "{alpha=0.1}{/alpha}"
  $ gtext = glitchtext(20)
  $ style.say_dialogue = style.edited
  mc "[gtext]"
  $ style.say_dialogue = style.normal
  voice "mod_assets/mio/mi_vc1l2.ogg"
  mi "{alpha=0.1}Hahahaha! Did you say something, [player]?{/alpha}"
  $ gtext = glitchtext(20)
  $ style.say_dialogue = style.edited
  mc "[gtext]"
  $ style.say_dialogue = style.normal
  voice "mod_assets/mio/mi_vc1m2.ogg"
  mi "{alpha=0.1}Uhuhu~{/alpha}"
  $ gtext = glitchtext(6)
  $ m_name = "[gtext]"
  m "[player]!"
  "Wait...I know that voice!"
  "That's [gtext]'s voice!"
  "..."
  "What...?"
  mc "[gtext]!"
  voice "mod_assets/mio/mi_vc1n2.ogg"
  mi "{alpha=0.1}Geez...That freaking depressed girl has come to ruin our time...{/alpha}"
  voice "mod_assets/mio/mi_vc1o2.ogg"
  mi "{alpha=0.1}Well...{/alpha}"
  mi "{alpha=0.1}[player], "
  voice "mod_assets/mio/mi_vc1p.ogg"
  extend "I want to tell you something...{/alpha}"
  $ gtext = glitchtext(80)
  $ style.say_dialogue = style.edited
  python:
      currentpos = get_pos()
      startpos = currentpos - 0.3
      if startpos < 0: startpos = 0
      track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/6s.ogg"
      renpy.music.play(track, loop=True)
  mi "[gtext]"
  mi "[gtext]"
  mi "[gtext]"
  mi "[gtext]"
  mi "[gtext]"
  play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
#  show screen invert(0.5, 0.3)
  show mio dark at t11:
        alpha 0
        0.5
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
  show layer master:
        0.5
        zoom 3.0 xalign 0.5 yalign 0.4
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
  show layer screens:
        0.5
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
  pause 2.0
  scene bg mc_lr
  play music "<silence 0.9>"
  mc "GAAAAAAAAAAAAAAAH!"
  $ style.say_dialogue = style.normal
  play music door
  $ s_name = "Sayori"
  $ m_name = "Monika"
  $ mi_name = "Mio"
  s "[player]! You there?"
  "Ah...So it was Sayori who saved me from that nightmare..."
  "What was that?"
  "A nightmare? It would make sense...But it felt too real!"
  stop music
  mc "{b}Ah...Yeah! Just a moment!{/b}"
  "Phew...My heart's beating so fast..."
  s "Can I come in?"
  mc "You know where the key is."
  s "Oh, yep!"
  "I keep a copy of my key below the welcome mat if I forget my keys at home, but Sayori also uses it to come into my house."
  "The door slowly opens and Sayori steps in."
  show sayori 1ba at l11 zorder 1
  s "Hello [player]~"
  mc "Hey Sayori, what's up?"
  s 1bl "Well...We got to go already...Did you forget?"
  mc "Ah, yeah. Just a moment, I'm heading to my bedroom to get a sweater."
  s 1bx "Alrighty~"
  "With that, I make my way to my bedroom."
  scene black with wipeleft
  scene bg bedroom with wipeleft
  "God...That nightmare made me forget about the meeting..."
  "I'm still doubtful...What was that? Why could I not move? Why couldn't I talk?"
  "I thank Sayori for saving me from that nightmare."
  "Well, whatever. Where did I put my sweater?"
  window hide(None)
  window auto
  pause 2.0
  "..."
  "Oh, it's over here."
  "Let's get going then."
  scene black with wipeleft
  scene bg mc_lr with wipeleft
  "Once I'm back in the living room, a happy Sayori appears in my field of vision sitting on the couch."
  "She is watching television, and as I'm coming down the stairs, she turns it off and stands up."
  mc "Alright, let's go Sayori."
  show sayori 1bx at t11 zorder 1
  s "Oh, okay [player]!"
  "I open the door, letting Sayori step out first."
  play sound closet_open
  scene black with wipeleft
  scene bg house with wipeleft
  play sound closet_close
  play music nday fadein 2.0
  "Since Sayori knows where Kotonoha lives now, she just waits for me, so we both head to her place."
  "I still can't help but think of that dream I had..."
  "I mean, that voice. Who could it be? I don't understand at all what that voice was trying to say."
  "Well, maybe it was just a nightmare."
  scene black with wipeleft
  scene bg street with wipeleft
  scene black with wipeleft
  scene bg st with wipeleft
  "A quiet and noiseless walk later, we are finally at Kotonoha's hotel."
  "Since Monika is living with her, they both should be on time for sure."
  show sayori 2bn at t11 zorder 1
  s "Uwaaaa--"
  s 2bp "[player], Natsuki nor Yuri know how to get here!"
  mc "..."
  mc "I thought you told them..."
  s 2bl "Ehehe...I forgot to..."
  mc "..."
  mc "Oh well...I'm calling Monika then."
  s 2bx "Alrighty~"
  "I take my phone out from my pocket, then I dial Monika's number."
  show sayori 1ba at t11 zorder 1
  window hide(None)
  window auto
  pause 2.0
  m "{i}Hello?{/i}"
  mc "Hey Monika, it's [player]."
  m "{i}Oh, hello! Are you guys on your way here?{/i}"
  mc "We have nearly arrived actually, I just wanted to know where Natsuki and Yuri are."
  m "{i}W-well...Natsuki arrived first, while Yuri arrived 5 minutes later.{/i}"
  mc "How did Yuri know where the hotel is at?"
  m "{i}She asked Kotonoha~ It's not that difficult to find considering how famous this hotel is.{/i}"
  mc "Oh...I see. Well, Sayori and I are almost there. See you in a couple of minutes."
  m "{i}Alright, we'll wait for you patiently!~{/i}"
  "With that, Monika hangs up."
  "For now let's forget everything and have fun."
  mc "You ready, Sayori?"
  s 2br "Yes!"
  "This bridge will kill me soon..."
  scene black with wipeleft
  scene bg hotel with wipeleft
  "Once we arrive, the usual scene greets us."
  "Monika and Kotonoha are talking."
  "Natsuki and Yuri are barely interacting. I don't understand why Natsuki is mad at Yuri..."
  "I'm guessing it's because Yuri doesn't agree with her, but that's just normal. Yuri is a nice person, kind of shy though."
  show monika 1ba at t11 zorder 1
  m "Hello guys!"
  mc "Oh, hello Monika!"
  show monika 1bb at t21 zorder 1
  show sayori 2bl at t22 zorder 1
  m "Sayori! I'm glad you've come today~"
  s "Yeah, well...I gotta have fun every now and then I suppose."
  m "That's right."
  "Kotonoha, who is behind Monika, stares at me. I stare at her in return and she shrugs."
  "Yuri stands up from the couch and comes to greet us."
  show monika 1ba at t31 zorder 1
  show sayori 2bl at t32 zorder 2
  show yuri 1bb at t33 zorder 3
  y "Greetings, [player] and Sayori."
  $ kt_name = "Kotonoha"
  mc "Oh, hey Yuri. Glad to see you around."
  y 2bj "W-well, if it weren't for Kotonoha's instructions I would not be here."
  mc "It's not like the hotel is that difficult to find anyhow."
  y "Affirmative..."
  s 1bx "Yuri~"
  y "Hello, Sayori."
  m "So... Is everybody ready to go?"
  hide yuri at thide
  hide yuri
  show monika 1ba at t31 zorder 1
  show sayori 2ba at t32 zorder 1
  show kotonoha 1ba at t33 zorder 1
  kt "I'm ready~"
  m "Let's get going then!"
  n "Whatever."
  "With that, Natsuki nods and makes her way to the exit."
  "Me and the girls head out as well."
  scene black with wipeleft
  scene bg st with wipeleft
  "Once we all are out, Sayori stares at me while Kotonoha does the same thing with Monika."
  show kotonoha 4bc at t11 zorder 1
  kt "So...Where are we supposed to go?"
  show kotonoha 4ba at t21 zorder 1
  show monika 1ba at t22 zorder 2
  m "Hm..."
  m "I'm not sure...W-what do you girls think?"
  show kotonoha 1ba at t31 zorder 1
  show monika 1ba at t32 zorder 2
  show yuri 1bi at t33 zorder 3
  y "What if we go to a library or a book store?"
  m 2bb "Well...It's a good suggestion, Yuri. But maybe we should do something a little different for a change."
  m "We're always reading in the club after all."
  y 3bq "You're right, Monika. Perhaps a change of pace would be good for us."
  kt 2bc "What if we go to the park? It's quite close to here."
  show yuri at thide
  hide yuri
  show kotonoha 2bc at t21 zorder 1
  show monika 2bb at t22 zorder 2
  m "Ahaha!~ Yes, me and [player] did go to that park yesterday."
  kt 2be "Oh..."
  extend 3ba2 "I see..."
  "Kotonoha seems to look rather dejected upon hearing that me and Monika were there yesterday."
  "Monika realizing this too, continues her speech."
  m 3bl "W-we didn't do anything! We just went to drink a coffee!"
  kt "..."
  kt 4bs2 "W-well...G-glad to hear that you guys had a good time..."
  "With that, Monika turns to look at the others."
  m "So, shall we get going to the park then?"
  show kotonoha 4bs2 at t31 zorder 1
  show monika 2bb at t32 zorder 2
  show sayori 2bl at t33 zorder 3
  s 2bl "What time are we eating?"
  m 1bd "Hm... "
  extend 3bd "How about after we're done with the park?"
  s "Well... "
  extend 3bx "Okay then!"
  show monika 3bk at h32 zorder 2 
  m "So, let's get going!~"
  "Kotonoha takes the lead, Natsuki walking next to her."
  show sayori at thide
  hide sayori
  mc "Phew, hopefully Mio won't c--"
  show kotonoha 3be at t21 zorder 1
  show monika 3bc at t22 zorder 2
  python:
    mi_name = "???"
  mi "Heeeeey! Wait for me!"
  mc "Uwa--!"
  "Like if it were a generic anime scene, Mio appears running from the distance waving her right hand, yelling at us to wait for her."
  show kotonoha 3be at t31 zorder 1
  show monika 3bc at t32 zorder 2
  show mio 5bk at t33 zorder 4
  $ mi_name = "Mio"
  mi "Haaaaaaaah... Haaaaaaaah... I finally caught up to you guys!"
  mi 5bl "I'm sorry that I took so long, I got super busy and I didn't keep track of the time."
  "Monika and Kotonoha stare at each other, while the other girls admire Mio's dress."
  show kotonoha at thide
  hide kotonoha
  show monika at thide
  hide monika
  show sayori 1bx at t21 zorder 1
  show mio 5bl at t22 zorder 2
  s 1bn "Oh wow, "
  extend 2br "that dress is so cute, Mio!"
  mi 2bx "Uhuhu~ "
  extend 3be "Thanks Sayori! It's my favorite dress~"
  show sayori 1bx at t31 zorder 1
  show mio 3be at t32 zorder 2
  show yuri 2bu at t33 zorder 3
  y "It certainly does fit you well."
  mi 5bx "Oh, thanks Yuri! That truly means a lot coming from you."
  y 3bd "Oh... Uhuhu~"
  mi 8be "Oh, hey Nat!"
  show yuri at thide
  hide yuri
  show sayori 4ba at t31 zorder 1
  show mio 8be at t32 zorder 2
  show natsuki 2bq at t33 zorder 3
  n "...Hey."
  show black zorder 120 with char_fade:
    alpha 0.64
  "Natsuki has barely talked to us, and her behavior has changed suddenly since we left school."
  "That's what I can see at least."
  "Natsuki will tell her how she feels eventually. Will it be soon? I don't know, honestly."
  hide black  
  show sayori at thide
  hide sayori
  show mio 5bb at t21 zorder 1
  show natsuki 2bq at t22 zorder 2
  mi 5bb "Are you alright? You look sick."
  n "I'm fine, it's not like you care or anything."
  mi 4bd "Of course I do! You're my friend."
  n 2bb "Are we? I don't remember giving you that title."
  mi 2be "Well, we've known each other for a long time~ It's just normal that I would care about you, isn't it?"
  n 4bs "Hmph."
  n "Whatever."
  mi 3bx "Uhuhu~"
  mi 6be "You should start saying how you feel, or you might regret it later." 
  mi 8be "So, where are we going?"
  show natsuki at thide
  hide natsuki
  show mio 8be at t11 zorder 1
  "Mio focuses her red eyes towards me."
  mc "Well...We are going to the park, aren't we Monika?"
  show monika 2bb at t21 zorder 1
  show mio 8be at t22 zorder 2
  m "Oh! Y-yeah."
  mi 3bx "Alrighty!~ "
  extend 6be "Shall we get going then?"
  "As she says that, Mio stands next to Kotonoha and hugs her left arm."
  show monika at thide
  hide monika
  show mio 5ba at t44 zorder 2
  show kotonoha 3bs at t22 zorder 1
  kt "Uwa--!"
  mi 1bx "Uhuhu~"
  "Letting her go, Mio now takes the lead, Sayori and Yuri are catching up to her."
  mi 1be "Come on! The day is coming to an end soon!"
  show mio at rhide
  hide mio
  show kotonoha 3bs at t11 zorder 1
  "Mio crosses her arms, Sayori and Monika walking next to her."
  "God... What even is wrong with that girl?"
  mc "{i}*sigh*{/i}"
  mc "Whatever, let's go."
  "Kotonoha kind of blushing in embarrassement, walks towards us."
  kt 4bs "W-what's wrong with her?!"
  mc "{i}*shrugs*{/i}"
  kt 4bq "Well... "
  extend 4bp "Let's just move on."
  "With that, Monika nods and starts walking to my left, while Kotonoha walks to my right."
  "And here I am, walking between two girls."
  "Who would have thought? [player] walking with two cute girls."
  "Now I'm really regretting that I had invited Mio to the club. Why did I think it was a good idea?"
  "Even as I'm walking with two girls, there's one thing I can't help but focus on: Me being an idiot."
  stop music fadeout 2.0
  "But oh well... We have to play along."
  scene black with wipeleft
  scene bg city with wipeleft
  "On our way to the park, Monika and Kotonoha are having a nice conversation regarding what they are gonna do tonight."
  "I can tell already that I'm not welcome in their chat, so I decide to keep my mouth shut."
  play music hp fadein 2.0
  "While Sayori, Mio and Yuri are having a chat as well, Natsuki just walks alone staring at the ground."
  "Mio tries to include her, but Natsuki doesn't even respond."
  "What's happening with Natsuki? Is she doing alright?"
  "Even if I try asking her, she's most likely to either ignore me, yell at me, or insult me."
  "I'll try asking her whenever I have the chance."
  scene black with wipeleft
  scene bg park with wipeleft
  "As we enter the park, the trees announce our arrival to our destination."
  "As well as the smell of wet dirt and singing birds in the distance."
  "We reach a place full of trees, where Monika decides to stop and call for us."
  "Mio, Sayori and Yuri are not walking anymore, while Natsuki stands before Kotonoha."
  show monika 3bb at t11 zorder 1
  m "Okay everyone!~ I kind of have a plan for us, and I have all the material we need in my purse!"
  "Monika raises her purse and points at it."
  m "I was...thinking that we could write tomorrow's poems here~"
  m 1bb "What do you all think?"
  show monika 1ba at t21 zorder 1
  show sayori 1bl at t22 zorder 2
  s "Well... "
  extend 2bl "It might work."
  show monika 3bb at t31 zorder 1
  show sayori 2bl at t32 zorder 2
  show yuri 3bn at h33 zorder 3
  y "Ah--"
  m 1bd "Um...Did something happen?"
  y 2bo "N-no! It's just that...I'm not used to writing anywhere else other than my room or a library."
  m "Ahaha!~ It's not that different, you'll see. Just give it a shot, will you?"
  y 2bq "Well...I'll try..."
  m "What do you think Kotonoha?"
  show monika 3bb at t41 zorder 1
  show sayori 2bl at t42 zorder 2
  show yuri 3bn at t43 zorder 3
  show kotonoha 2bb at t44 zorder 4
  kt "I don't know. I'm not used to writing poetry so wherever works for me."
  m 2bn "So... Is that a 'yes'?"
  kt 4ba "Yeah, sure~"
  m 4bb "Okay! Well then, everyone please take a sheet of paper and a pen!"
  "Monika opens up her purse revealing a set of pens and thick paper sheets."
  "Her red pen with a heart is in a small case, it looks very cute and expensive."
  m "Okay everyone! Let's get started!"
  "Everybody takes a seat on the grass."
  "Hopefully this time I'll write a good poem..."
  scene black with wipeleft
  scene bg park with wipeleft
  "Just like yesterday, my brain isn't working properly."
  "I won't be able to come up with something good if I'm like this..."
  "Can I for once come up with a good idea for a poem right away?"
  "Hm..."
  window hide(None)
  window auto
  pause 2.0
  "Let's see..."
  "What if I do something for Natsuki?"
  "Like, something to try to get her to learn something."
  "Let's see what I can come up with..."
  window hide(None)
  window auto
  pause 2.0
  "..."
  "There! I got it!"
  "I just hope it isn't too combative."
  call showpoem(mc_poem2, music=False) from _call_showpoem_14
  "Huh..."
  "I think I went too far with this..."
  "I'll leave it be."
  "I decide to lie down on the grass since I'm done writing my poem."
  scene bg sky with Dissolve(1.0)
  stop music fadeout 2.0
  "Aaahhhh... I forgot how soft the grass is."
  "Wow...These days have been very weird, it's almost looking impossible for everyone to accept Monika back..."
  "But, it's only been like a week that has passed already."
  y "Um...[player]"
  mc "Oh? Yuri?"
  y "Yes. Would you mind if I talk to you about something?"
  "A shy Yuri appears before me. I nod and Yuri takes me a short distance away from the others."
  "We both sit again on the grass."
  scene bg park with Dissolve(1.0)
  play music tyuri_c fadein 2.0
  "As she sits, Yuri's long hair waves as the wind softly blows."
  "She brushes her hair off her face and stares at me."
  show yuri 1bv at t11 zorder 1
  y "[player]..."
  y 2bv "I...I'm still concerned about some things."
  mc "What is it?"
  y 3bw "I mean, "
  extend 2bt "it's about Monika."
  "Yuri looks away."
  mc "Monika? What's up with Monika?"
  "Yuri's shyness shows once again, as she still looks away."
  "Yuri sighs and stares at me again."
  mc "..."
  mc "Yuri?"
  y 3bt "Yes?"
  mc "I know you're afraid, and you're not the only one."
  mc "But trust me, Monika is just as scared as you are."
  # aqui 5
  y 1bt "Monika? Why would Monika be scared? What for?"
  mc "Well, Monika doesn't want to lose your friendship. That's why she's behaving like nothing happened."
  y 2bh "I'm afraid I don't understand."
  y 1bh "Does Monika think that being like this will change what she has done?"
  mc "No, but she's trying to get you all to accept her apologies and trust her once again."
  mc "Look..."
  "Yuri locks her gaze on me, kind of curious."
  y 2be "Hm?"
  mc "Wouldn't you like someone to help you when you make a mistake?"
  mc "I make mistakes in my life all the time, you will make mistakes too, and even that couple walking around will do the same thing."
  mc "And when that moment comes--and you realize you did wrong--wouldn't you want the support and forgiveness of another person?"
  y 3bg "Well... You're right."
  mc "What I mean is..."
  mc "Placing your trust in people who have wronged you might be hard at first, but as Sayori said, you all have to be empathetic."
  mc "What would you have done if you had been in Monika's place?"
  y 2bh "I don't know, but I wouldn't have killed my friends at all."
  y 1bk "That's just wrong."
  mc "No, you would have killed them all. Just look at Sayori when she almost deleted both you and Natsuki."
  mc "When she realized the truth of this world."
  y 1be "..."
  y 1bh "I-I don't know what to say..."
  mc "For now, try to give Monika one final chance. I swear she's remorseful for all she did."
  y 2bh "Well...Okay [player]."
  y "I'll try."
  mc "Great Yuri! That's the spirit!"
  y "..."
  y 1bs "Sure, I suppose."
  mc "So, how is your poem coming along?"
  y 2bb "I finished it already actually."
  mc "Oh, can I know what it's about?"
  y 2bg "Um... "
  extend 2bj "I think you can read it first."
  mc "Oh, well I wasn't asking you to let me see it first, I just wanted to know what your poem is about."
  y "It's sort of hard to explain it."
  mc "{i}*sigh*{/i}"
  mc "Alright...I'll give it a check."
  y 1bb "Okay [player]. Here, my poem."
  "Yuri hands her poem to me, I reach out and take it."
  mc "Would you mind if we lie down on the grass?"
  y 2bd "N-not really, it's okay with me!"
  "I nod and we both lay on the grass."
  scene bg sky with Dissolve(2.0)
  mc "Today is a nice day, isn't it?"
  y "Oh? Yes, indeed it is."
  mc "Did you miss this environment while you were at that void?"
  y "..."
  y "Sort of."
  mc "Huh? How so?"
  y "As you might or might not know, I...don't like the nature. It sort of scares me."
  "Yuri's shy voice pitch has changed to her typical delicate voice as she smiles while watching the sky."
  y "I'm used to writing when I'm home and at my own pace."
  y "So this is a new experience for me."
  mc "Ah...I see."
  y "Um...[player]?"
  mc "Yeah?"
  y "Are you going to read my poem?"
  mc "Oh! God, I almost forgot it. I'm sorry."
  y "Uhuhu~ "
  extend "It's okay [player]."
  "With that, I put Yuri's poem in front of my face and start reading through it."
  call showpoem(y_poem2, music=False) from _call_showpoem_15
  mc "Oh..."
  y "Did you like it, [player]?"
  "Honestly I have no idea...What I like from Yuri's poems is that she always uses difficult language."
  "Yuri's poetry is without a doubt another level I barely understand."
  mc "Yeah, I like it. Very complex and difficult language as usual, eh?"
  y "Yes."
  mc "I see. Well, it's not that bad actually."
  y "Oh really?"
  mc "Of course! I truly do like your poem."
  y "Oh...I-I'm glad to hear that."
  y "Would you change something about my poem that you didn't like?"
  mc "Why would I change something? This is how you write."
  mc "I can't change the way you write, you know?"
  y "Well...Thanks for your review [player]."
  mc "You're welcome Yuri."
  "And then, our voices fade into total silence."
  "Meanwhile everyone else is still writing their poems."
  "I think we just have to wait."
  y "And...[player]..."
  mc "Yeah?"
  y "What are you going to do with Natsuki?"
  mc "Hm?"
  y "She has been very rude towards me as well, [player]."
  mc "Really? Why?"
  y "I'm not sure to be honest... It's probably because I didn't agree with her."
  y "She's been rude towards Sayori as well."
  "Wow...Natsuki is being very stubborn even with Yuri and Sayori."
  "Isn't that kind of childish? I mean, it's not like Yuri and Sayori did anything wrong, did they?"
  "However, Natsuki has all the right in the world to hate me and Monika, but hate them for no reason? That's way too much."
  "We've got to do something...But what can we do?"
  mc "Hm...I see."
  mc "Well, there's nothing I can do on my end as you might know."
  y "Yes, I know, [player]."
  mc "So, for now we have to be as careful with her as we can."
  mc "Me and Kotonoha are going to deal with it in the coming days and hopefully we'll manage to reach her."
  y "I trust you [player]."
  "I kindly smile at Yuri as Monika calls for everyone."
  m "Okay everyone!~ Who's done already?"
  stop music fadeout 2.0
  n "Me."
  kt "I'm done too!"
  s "Yep, me too!"
  mi "Uhuhu~ I was done quite a long time ago!"
  play music nday fadein 2.0
  "As me and Yuri both hear Monika, we stand up and return to the group."
  scene bg park with dissolve_scene_full
  "We slowly make our way to the girls, Monika asking us to sit."
  show monika 3bb at t11 zorder 1
  m "So...Do any of you want to share their poems?"
  show monika 3bb at t21 zorder 1
  show yuri 1bj at t22 zorder 2
  y "Honestly I would prefer waiting for tomorrow, so the poem assignment fulfills it's purpose."
  show monika 3bb at t31 zorder 1
  show yuri 1bj at t32 zorder 2
  show kotonoha 2bb at t33 zorder 3
  kt "Yeah, me too."
  m "Oh! Well, Ok then! We'll wait until tomorrow to share our poems."
  show monika 3bb at t41 zorder 1
  show yuri 1bj at t42 zorder 2
  show kotonoha 2bb at t43 zorder 3
  show mio 3be at t44 zorder 4
  mi "Great!~"
  n "Whatever."
  show monika 3bb at t51 zorder 1
  show yuri 1bj at t52 zorder 2
  show kotonoha 2bb at t53 zorder 3
  show mio 3be at t54 zorder 4
  show sayori 2bx at t55 zorder 5
  s "So...It's time to eat, isn't it?!"
  m  2bl "Ahaha!~ Sure, "
  extend 2bb "what would you want to have?"
  show sayori 2bq at h55 zorder 5
  s "I want a burger!"
  m 4bn "W-well...I don't think I can eat a burger... "
  extend 3bb "But hey, I know a good restaurant where they have both meat and vegetarian options!"
  m "What do you all think?"
  s 4br "Mmmmmm~ I'm imagining the delicious smell of a burger~ "
  extend 3bx "What are we waiting for, then? Let's go!"
  show sayori at rhide
  hide sayori
  show monika 3bb at t41 zorder 1
  show yuri 1bi at t42 zorder 2
  show kotonoha 1be at t43 zorder 3
  show mio 3bg at t44 zorder 4
  m 2bl "Hey Sayori, we don't have--"
  m 2bm "{i}*sigh*{/i}"
  mc "Sayori is still the same, isn't she?"
  y 2bj "She truly is."
  mc "Oh well...Let's catch up to her."
  "With that, Monika and Yuri nod and slowly start to make their way out of the park."
  "I think it's better if they stay together, they may need to have a serious talk."
  "Having said that, Kotonoha shrugs and she just walks next to me. Mio, Sayori, and Natsuki following us."
  scene black with wipeleft
  scene bg city_b with wipeleft
  show orange zorder 100 with char_fade:
    alpha 0.18
  "I'm surprised with how fast time passes here..."
  "Anyway, we have been walking around the city for a while now, still looking for that restaurant Monika mentioned before."
  "As I expected, Monika and Yuri are having a conversation. It seems to be going well."
  "Mio and Sayori get along well, actually. It almost seems Mio is just a normal high school girl like all of us."
  "On the other hand, me and Kotonoha are walking together saying nothing. Kotonoha has a cute smile on her face."
  "She says something every now and then, but that's it. We haven't had time to have a good conversation."
  "I'm going to break this silence."
  mc "So, Kotonoha."
  show kotonoha 1bb at t11 zorder 1
  kt "Hm?"
  "Kotonoha turns to look at me."
  mc "Um...Do you wanna talk?"
  kt 7bc "S-sure! What a-about?!"
  "Kotonoha realizing she screamed, quickly blushes and looks away."
  show kotonoha 5bs at h11 zorder 1
  kt "Oh, I-I'm sorry! I didn't mean to scream like that!"
  mc "Yeah, don't worry about it."
  kt 4bs "Well..."
  extend 4ba2 "What do you want to talk about?"
  mc "Ah...Well, it seems Monika and you have gotten along well so far, haven't you?"
  kt 3bd "Hm... Yeah? We have more in common than I would ever have imagined."
  kt 4bd "She's a very nice person, you know?"
  mc "Yeah, I know. Monika is a very mature girl too."
  kt 5bh "Indeed she is! Talking to her is always amusing."
  mc "How so?"
  kt 2ba "Like...She always has something to talk about."
  mc "Hm, I see."
  mc "I should try asking her out on a date, but I'm kind of afraid."
  kt 1bf "Why are you afraid?"
  mc "I don't know...It's like somehow I think she might reject me even when I already know the answer."
  kt 4bf "Oh...I see."
  kt 5ba "Well, I would suggest you to be more confident in yourself [player]."
  kt "I mean, asking her to go on a date is kind of sudden, isn't it?"
  mc "What do you mean?"
  kt 6bb "What I'm trying to say is that you should get to know her a little bit better before asking her to go on a date."
  kt "Don't you think so?"
  mc "Well...I didn't think of it actually."
  mc "Maybe you're right..."
  kt 7bb "I am. Try to get to know her a little bit better. "
  extend "Then try and ask her to go on a date with you."
  mc "Yeah, you're right. I'm gonna do that."
  kt 3bj "Uhuhu~"
  kt "Glad to hear that!"
  m "Okay, we're here."
  "Monika points in the direction of the restaurant as Sayori catches up."
  show kotonoha 6ba at t21 zorder 1
  show sayori 2bq at t22 zorder 2 
  s "Oh, it smells delicious from outside! How did you find this restaurant, Monika?"
  show kotonoha 6ba at t31 zorder 1
  show sayori 2bq at t32 zorder 2
  show monika 1ba at t33 zorder 3
  m "Well, I'm kind of a regular here~"
  s 2bx "Oooooh, great!"
  s "Then let's get inside already!"
  m 2bk "Sure!"
  "Monika nods and then Sayori makes her way to the restaurant entrance."
  scene black with wipeleft
  scene bg restaurant with wipeleft
  show orange zorder 100 with char_fade:
    alpha 0.18
  "The smell of delicious food fills the environment as soon as we get in."
  "I got to admit how good the restaurant looks like from outside." # aqui
  show sayori 1bn at t11 zorder 1
  s "Oooh! I didn't know this place even existed!"
  s "I truly do like it!"
  show sayori 1bn at t21 zorder 1
  show mio 1be at t22 zorder 2
  mi "Yeah, it's certainly a comfortable place to eat at."
  show sayori 1bn at t31 zorder 1
  show mio 1be at t32 zorder 2
  show yuri 1bb at t33 zorder 3
  y "Agreed."
  show sayori 1bn at t41 zorder 1
  show mio 1be at t42 zorder 2
  show yuri 1bb at t43 zorder 3
  show monika 1bj at t44 zorder 4
  m "Well, let's order!"
  "With that, everyone but Natsuki and I follow them."
  show sayori at rhide
  hide sayori
  show mio at rhide
  hide mio
  show yuri at rhide
  hide yuri
  show monika 4bb at t11 zorder 1
  m "Are you guys coming?"
  show monika 4bb at t21 zorder 1
  show natsuki 3bq at t22 zorder 2
  n "No."
  mc "Erm... I'll wait here."
  m 2bl "Oh, okay [player]. Do you want me to order an appetizer for you?"
  mc "I'm gonna take just a chocolate cornet."
  m 2bb "What about you Natsuki?"
  n 3bb "I don't want anything right now. I...I would rather wait for dinner."
  m "Oh don't worry, me and Kotonoha are paying so you can have as much food as you want, Natsuki!"
  stop music fadeout 2.0
  show natsuki 1bv at h22 zorder 1
  n "I said no!"
  m 1bo  "..."
  m 2bp "Well... Okay."
  "Monika finally goes to sit at a table as Natsuki leaves the restaurant."
  show monika at rhide
  hide monika
  show natsuki at lhide
  hide natsuki
  "What is up with her? Is she sick or something? I have to find out what's going on."
  "Slowly walking, I exit the restaurant."
  scene black with wipeleft
  scene bg city_b with wipeleft
  show orange zorder 100 with char_fade:
    alpha 0.18
  "After leaving the restaurant and searching the block, I see Natsuki sitting on the sidewalk."
  "She doesn't appear to be sick at all, but she seems to be upset as she has her head placed on her arms."
  play music t9 fadein 2.0
  "Geez...Seeing her like this is really heartbreaking..."
  "To think she's not like that when me and Monika are around. However, I don't think she's willing to talk to me..."
  "--but I should give it a shot."
  "I make my way towards Natsuki who is still sitting on the sidewalk."
  "I slowly sit as she notices me. Natsuki looks away, like if she were hiding something from me."
  show natsuki 12ba at t11 zorder 1
  n "W-what? Did you miss anything?"
  mc "Yes. I have lost a pink haired girl around 4'11\", she's wearing a white blouse and a pink skirt. Have you seen her?"
  n 42bb "I'm not in the mood for your crap."
  "My attempt to cheer her up has failed, so I think that I will try plan B."
  "What would that be? I don't know. Be straightforward, I suppose."
  mc "Are you alright?"
  n 12bb "I'm alright. Go away now."
  mc "No Natsuki, I'm not going anywhere!"
  n 3bn "..."
  mc "You're NOT alright at all. Would you mind talking to me and tell me how you feel?"
  n 42bc "Why? It's not like you care about me or anything."
  mc "Wha--"
  mc "Why on earth would you think that?"
  show natsuki 2bo at h11 zorder 1
  n "Why on earth did YOU bring Monika back? Wasn't that a very irresponsible choice of yours?"
  mc "I don't think it was irresponsible...I'm just trying to re-write the fate of this world."
  mc "If I didn't care about you, I wouldn't have brought you back."
  n 5bb "Did you?"
  mc "Eh?"
  n "Pffft. Forget it."
  mc "No, what was that?"
  n 3bb "I said forget it already!"
  mc "I'm sorry but I don't think I will."
  n 2bh "{i}*sigh*{/i}"
  show natsuki at rhide
  hide natsuki
  "Pissed off, Natsuki stands herself up heading back to the restaurant."
  mc "H-hey!"
  "She stares at me above her shoulder since I'm still sitting on the sidewalk."
  show natsuki 42ba at t11 zorder 1
  n "Bad choices annoy me."
  stop music fadeout 2.0
  show natsuki at thide
  hide natsuki
  "Having said that, Natsuki enters the restaurant."
  "What was that supposed to mean?"
  "Was this really a bad choice? What was even the bad choice that I made?"
  "Bringing Monika back? Bringing Natsuki back? I don't understand..."
  "I'm getting worried already..."
  "Oh well...I don't know what I have to do..."
  mc "{i}*sigh*{/i}"
  "I stand up, making my way back to the restaurant."
  scene black with wipeleft
  scene bg restaurant with wipeleft
  show orange zorder 100 with char_fade:
    alpha 0.18
  play music nday fadein 2.0
  "The girls were already eating, while Natsuki at the end of the table is having a small sandwich on a plate."
  "My chocolate cornet is there lying on the table, waiting for me to eat it."
  "I sit down next to Kotonoha and listen to their conversation while I eat my chocolate cornet."
  show monika 2bb at t11 zorder 1
  m "So, I have an idea girls! What if we have a sleepover tonight?"
  show monika 2bb at t21 zorder 1
  show kotonoha 4bb at t22 zorder 2
  kt "Uhhh.. We gotta go to school tomorrow, Monika..."
  show monika 2bb at t31 zorder 1
  show kotonoha 4bb at t32 zorder 2
  show sayori 2bd at t33 zorder 3
  s "Um... Well, I think it might be a good idea, I suppose."
  show monika 2bb at t41 zorder 1
  show kotonoha 4bb at t42 zorder 2
  show sayori 2bd at t43 zorder 3
  show mio 6bl at t44 zorder 4
  mi "I don't think I can go, I'm terribly sorry!"
  show monika 2bb at t51 zorder 1
  show kotonoha 4bb at t52 zorder 2
  show sayori 2bd at t53 zorder 3
  show mio 6bl at t54 zorder 4
  show yuri 1bh at t55 zorder 5
  y "I think I'll go...But I still need to finish tomorrow's assignments."
  show yuri at thide
  hide yuri
  show natsuki 1bb at t55 zorder 5
  n "Don't count me in."
  m 2bg "Oh...Why is that?"
  n 2bq "I don't think my father would let me stay at somebody else's place."
  m 3bb "It's okay, we can ask him! Just tell us where your house is at and we'll kindly go to talk to him!"
  n "I don't think you can convince him."
  kt 5ba "What if we politely ask him?"
  n "{i}*sigh*{/i}"
  n 2bm "You can try but don't get your hopes up. Kotonoha knows where my place is at."
  m 3bk "Okay!"
  m 3bl "O-oh! [player]...I-I don't think you can come with us this time..."
  mc "Huh?"
  "I dissimulate that I wasn't listening to their chat and I try to escape the situation."
  m 2bn "Um...We're organizing a sleepover tonight."
  mc "Oh, I'm sorry. I wasn't listening."
  n 3bc "She said you're not invited."
  mc "Huh?! What for?!"
  m 4be "Well...Because it's a girls night and we might need some privacy for us to talk."
  mc "Ah alright, don't mind me. I need some time for myself as well."
  m 4bk "Sounds like a plan!"
  $ m_name = "Everyone"
  show natsuki at thide
  hide natsuki
  show mio at thide
  hide mio
  show monika 4bk at h41 zorder 1
  show kotonoha 4bj at h42 zorder 2
  show sayori 2br at h43 zorder 3
  show yuri 1bd at h44 zorder 4
  m "Yes!"
  $ m_name = "Monika"
  m "Alright! Do you all wanna go and hang out around the city?"
  show monika 3bb at t51 zorder 1
  show kotonoha 4bj at t52 zorder 2
  show sayori 2br at t53 zorder 3
  show mio 8be at t54 zorder 4
  show yuri 1bd at t55 zorder 5
  mi "Uhuhu~ Sure! Why not?"
  kt 7ba "I'm alright with that. "
  extend 7ba2 "But we didn't finish our homework either, Monika..."
  m 4bb "Well... We can finish it tonight."
  kt 4bd "Hm... Alright then."
  mc "Shall we finish eating then?"
  m 2bb "Yes!"
  scene black with wipeleft
  scene bg restaurant with wipeleft
  show orange zorder 100 with char_fade:
    alpha 0.18
  "The day is slowly coming to an end and Natsuki has left already, Mio following her."
  "I thought it would be annoying to have Mio around, but it was kind of hilarious."
  "She actually seems to be a very nice person."
  "As for the others, they are barely saying anything since Mio and Natsuki left."
  "With that, we were supposed to hang out around the city, but it's getting late...Not to mention that Natsuki and Mio have left."
  "We'll probably be returning to our respective homes soon."
  "Or probably not, since Monika is organizing a sleepover, which I'm not invited to."
  "Well, I just need some time for myself just like they all do...They might resolve their problems."
  show monika 1ba at t11 zorder 1
  m "Well... Since Mio and Natsuki have left, do you want to walk around the city?"
  mc "It sounds good to me."
  show monika 1ba at t21 zorder 1
  show kotonoha 2ba at t22 zorder 2
  kt "I'm down too!"
  m "Okay! Are you girls ready?"
  $ m_name = "Sayo & Yuri"
  show monika 1ba at t41 zorder 1
  show kotonoha 2ba at t42 zorder 2
  show sayori 2bx at t43 zorder 3
  show yuri 3bd at t44 zorder 4
  m "Yes!"
  $ m_name = "Monika"
  m "Good, let's enjoy the rest of the day together!"
  stop music fadeout 2.0
  scene bg restaurant with wipeleft
  show orange zorder 100 with char_fade:
    alpha 0.18
  "They all happily nod and in the blink of an eye, They all walk out of the restaurant."
  "...Well? Okay I suppose."
  scene black with wipeleft
  scene bg city_b with wipeleft
  show orange zorder 100 with char_fade:
    alpha 0.18
  play music city fadein 2.0
  "As the sun descends, the air starts to cool down."
  "A soft breeze blows, making the leaves on the trees wave as well as Monika, Yuri and Kotonoha's long hair."
  "Sayori and Yuri are seemingly trying to accept Monika back, but I can still feel a weird stagnating air."
  "They all are talking about what they're going to do tonight at Kotonoha's hotel when night comes."
  "Sayori is eventually returning to her usual self around Monika; Yuri on the other hand is still kind of afraid."
  "And Kotonoha is...Well, being Kotonoha. I mean, she's having a nice conversation with Yuri and Monika, Monika joining every now and then."
  "Well...Now they're not my concern. It's Natsuki..."
  "Lost in my thoughts, I realize they all are turning to look at me and laughing."
  "Kotonoha then asks me to catch up to her, I start walking faster to do so."
  "As I reach her, she stares at me."
  show kotonoha 2ba at t11 zorder 1
  kt "Hey [player]!"
  mc "Uwa--!"
  mc "What?"
  kt 4ba2 "You did see me in my nightgown yesterday, didn't you?"
  mc "Eh?!"
  kt 7bd "Uhuhu~ Don't worry, we're just talking about what our pajamas are like."
  kt 4ba "They don't believe that I wear a nightgown, and since you saw it..."
  mc "I did, but you yelled at me 'Close your eyes!' while blushing."
  show kotonoha 6bs2 at h21 zorder 1
  show sayori 3br at t22 zorder 2
  s "Awwww, how cute!"
  show kotonoha 6bs2 at t31 zorder 1
  show sayori 3br at t32 zorder 2
  show monika 2bn at t33 zorder 3
  m 2bn "Ahaha... Also, I pushed [player] to the left and hugged Kotonoha."
  kt 4bw2 "...!"
  s 2bx "Oh? Why?"
  m 3bn "So [player] couldn't see her like that, I suppose..."
  mc "It still hurts by the way."
  show kotonoha 7bs2 at t41 zorder 1
  show sayori 2bx at t42 zorder 2
  show monika 2bn at t43 zorder 3
  show yuri 2bj at t44 zorder 4
  y "Well, that was sort of exaggerated, wasn't it Monika?"
  mc "Thanks Yuri. Finally somebody understands what I went through."
  show kotonoha 7bj at h41 zorder 1
  show sayori 3br at h42 zorder 2
  show monika 2bk at h43 zorder 3
  show yuri 3bd at h44 zorder 4
  "They all laugh while we wait to cross the street."
  "This is how I want everyday to be."
  "No, this is how it {b}will{/b} be everyday. I'll give it my best effort to see them all smile and laugh like this everyday."
  "I'm willing to pay whatever price to give them that happiness they all deserve."
  stop music fadeout 2.0
  scene black with wipeleft
  scene bg city_c with wipeleft
  "After walking a very long time around the city, the night has arrived."
  "Despite this, there's still a bit of warmth in the air, giving this day a peaceful and comfortable end."
  play music night fadein 2.0
  "It may be time to wrap this day up since the girls have stopped talking and appear to be getting sleepy."
  mc "Hey girls, are you tired already?"
  show sayori 2bl at t11 zorder 1
  s "Ehehe... I'm kinda sleepy, yes."
  show sayori 2bl at t21 zorder 1
  show kotonoha 3ba2 at t22 zorder 2
  kt "Yeah, me too."
  $ m_name = "Yuri & Moni"
  show sayori 2bl at t41 zorder 1
  show kotonoha 3ba2 at t42 zorder 2
  show monika 2bm at t43 zorder 3
  show yuri 2bq at t44 zorder 4
  m "Yep..."
  $ m_name = "Monika"
  mc "Well, I'm gonna stop by your place just to make sure nothing bad happens on your way back, Kotonoha."
  kt 4bd "Okay [player], let's get going."
  y 3bb "All right."
  "Yuri nodding, Kotonoha takes the lead."
  scene black with wipeleft
  scene bg cafe3 with wipeleft
  "I'm also tired to be honest... We were walking for a large amount of time and my legs are yelling at me to stop."
  "Unfortunately, another day of Natsuki not talking to me has passed, and I'm losing all hope already."
  "She can't be like that everyday, you know? She has to agree to talk to us sometime."
  "But what if she doesn't? What if she's really not going to accept Monika back? It'll be a big problem for the future."
  "Having said that, Natsuki needs to at least listen to us...But she's just so stubborn."
  "I'm also kind of concerned about her...Why didn't she even talk? Was she sick for real?"
  "These are some questions that won't have answers anytime soon."
  scene black with wipeleft
  scene bg st3 with wipeleft
  "We eventually reach Kotonoha's place, but despite being 9:54 pm I feel that I should stay with them till 10:15 pm."
  "So I can rest for a little bit too."
  stop music fadeout 2.0
  scene black with wipeleft
  scene bg hotel with wipeleft
  show black onlayer front:
   alpha 0.6
  with wipeleft
  show kotonoha 1ba at t11 zorder 1
  kt "Okay, you all wait here. I'm gonna talk to the recepcionist."
  show kotonoha at thide
  hide kotonoha
  "Monika, Yuri and Sayori nod, and we all go sit down on the couch in the reception area."
  show sayori 1ba at t11 zorder 1
  s "Hey, [player]?"
  play music hotel fadein 2.0
  mc "Hm?"
  s 2bb "Are you staying too?"
  mc "Yeah, I need some rest. My legs are killing me."
  s 2bl "Eh, I mean...Are you staying with us tonight?"
  mc "Ahhh...No, I won't. I'll be heading back at 10:15 pm."
  s 2bx "Oh, I see. Well, alright then~"
  "Kotonoha finally got her key, so she gestures at us to follow her."
  "Thank God this hotel has an elevator..."
  hide black onlayer front
  scene black with wipeleft
  scene bg hotel2 with wipeleft
  "The smell of carpet fills the elevator's air, and despite it being kind of pleasant, I can't help but feel anxious."
  "I hope whatever Monika has planned for tonight helps re-establish the girls' trust in her."
  "I suppose Kotonoha was down for this to begin with, but who am I to judge her choice? It was hers after all."
  scene black with wipeleft
  scene bg hotel_hw with wipeleft
  s "Ohhh, look at this upholstered wall! It's so soft!"
  kt "I know, I know. It really makes the wall look charming~"
  s "Yes! Indeed it does!"
  y "Sayori, d-don't yell that loud!"
  s "Ehehe...I'm sorry Yuri, this is so soft! Look, feel it yourself!"
  "Sayori takes Yuri's hand, putting it on the wall."
  y "Oh...Well, you're right, this upholstery is very soft. But even so, please don't yell that loud."
  s "Alrighty, I'll try~"
  kt "Okay, here it is."
  "Kotonoha slides her card in the door's card terminal, the door's lock clicks and unlocks."
#  stop music fadeout 2.0
  play sound closet_open
  scene black with wipeleft
  scene bg hotel3 with wipeleft
  play sound closet_close
  show kotonoha 1ba at t11 zorder 1
  kt "Don't forget to take your shoes off~"
  "Since Monika is living with Kotonoha, this room now smells like both Kotonoha and Monika's perfume. It's a pleasant sweet smell to be honest."
  "I take my shoes off and let myself into the room."
  kt "Alright, just a moment, be right back!"
  $ m_name = "Everyone"
  m "Okay!"
  $ m_name = "Monika"
  "Kotonoha then takes a white nightgown from the drawer and walks to the bathroom."
  show kotonoha at thide
  hide kotonoha
  show yuri 3bb at t11 zorder 1
  y "So...Are we going to Natsuki's place?"
  show yuri 3bb at t21 zorder 1
  show monika 2bd at t22 zorder 2
  m "Oh God, me and Kotonoha almost forget about that! As soon as she comes out of the bathroom, I'll remind her."
  y 2bc "Sounds like a plan."
  m 3bk "Mhm~"
  "Kotonoha is done putting on her 'pajamas', and she finally steps out of the bathroom."
  show yuri 2bc at t31 zorder 1
  show monika 3bk at t32 zorder 2
  show kotonoha 3ca at t33 zorder 3
  kt "I'm back~"
  mc "Should I close my eyes?"
  kt 7ca2 "Um... N-no, t-this is k-kinda embarrassing enough..."
  y 2bd "Uhuhu~"
  show yuri 2bd at t41 zorder 1
  show monika 3bk at t42 zorder 2
  show kotonoha 7ca2 at t43 zorder 3
  show sayori 1bx at t44 zorder 4
  s 1bx "Ohhh, I like it Kotonoha!"
  kt 4ch1 "Ah, well... Thanks Sayori!"
  m 2be "Um... Kotonoha?"
  kt 6ca "Yeah?"
  m "Aren't we missing something?"
  m 2bn "I mean, {i}someone{/i}?"
  kt 6cf "..."
  kt 4cf "...!"
  kt 4cp "Oh, Natsuki!"
  mc "{i}*sigh*{/i}"
  mc "You're too silly, Kotonoha."
  kt 3cp "Well...Then I'm going to put my dress back on and we'll go to her place."
  m "Oh... Okay..."
  show kotonoha at rhide
  hide kotonoha
  show yuri 2ba at t31 zorder 1
  show monika 2bn at t32 zorder 2
  show sayori 1bx at t33 zorder 1
  "Kotonoha runs to the bathroom again."
  "I take my phone out of my pocket, the display says that it's 10:24 pm already."
  mc "Oh God, I gotta go girls! Tell Kotonoha I said goodnight for me."
  m 1bg "Why is that?"
  mc "Because it's 10:24 pm already, and I need to get some sleep."
  m 2be "I see. Well, take care [player]!"
  show yuri 2bi at t31 zorder 1
  show monika 2bn at t32 zorder 2
  show sayori 1bx at t33 zorder 3
  s "See you tomorrow at school~"
  y 2bb "You have a goodnight, [player]."
  mc "Same for y'all girls. See you."
  "With that, I run to the door."
  play sound closet_open
  scene black with wipeleft
  scene bg hotel_hw with wipeleft
  play sound closet_close
  "Running as fast as my legs will allow me, I reach the elevator."
  scene black with wipeleft
  scene bg hotel2 with wipeleft
  "Phew...Fortunately the bus stop is near here, otherwise I would not even catch the last bus home."
  "Hopefully Monika and Kotonoha will manage to at least clear things up with Sayori and Yuri."
  "Well, I believe they can do it."
  "Mio... I don't know why Monika says she's self-aware about this world, she doesn't seem to even know we are self-aware."
  "But I'm gonna trust her, it's the least I can do."
  stop music fadeout 2.0
  "And Natsuki... Well, actually I'm not expecting her to accept the fact that Monika is back anytime soon."
  "I really hope we can make our way into her heart and fully convince her."
  "The elevator has stopped already, so I get myself ready to run again."
  scene black with dissolve_scene_full
  show text("{size=100}{color=#6debab}{b}Kotonoha, night 3{/b}{/size}{/color}\n{size=60}The sleepover{/size}"):
      truecenter
  with Dissolve(1.0)
  pause 4.0
  scene bg hotel4 with dissolve_scene_full
#  scene bg hotel4 with wipeleft
  "God...I almost forgot we gotta go to Natsuki's place..."
  "Hopefully I remember her address. I'm a genius after all, aren't I?"
  "Somehow I knew this will happen, and that's why this was a good move."
  "Natsuki was behaving very weird, it wasn't like her at all. Mio was right, Natsuki was looking like she was sick or something."
  "I just hope she's not...She's too thin, and I don't think she can overcome a sickness that easily."
  "Now... why did I put on my nightgown if [player] was here? I didn't even feel that embarrassed this time."
  "I have to calm down..."
  kt "{i}*sigh*{/i}"
  kt "Well, let's get going."
  "I open the door as I hear them all speaking."
  scene black with wipeleft
  scene bg hotel3 with wipeleft
  "As soon as I step out, Yuri, Monika and Sayori are having a conversation."
  "It seems to be going well so far, but I'm afraid I have to interrupt them."
  kt "Okay, let's go!"
  show monika 4ba at t11 zorder 1
  m "We'll follow you~"
  "With that, we all head out of the room."
  play sound closet_open
  scene black with wipeleft
  scene bg hotel_hw with wipeleft
  play sound closet_close
  play music night fadein 2.0
  "I'm kinda getting used to this hotel, I might even call it my new home."
  "I used to live around the same residential area as [player]. My house was next to Naomi's, but now it's different."
  "I'm living in a place I wouldn't ever be able to afford and I have new friends."
  "But even so, why do I feel this empty? I still miss Naomi..."
  "She's the only one I could call 'a good friend of mine'."
  "But I can't even talk to her for now..."
  "Will the same thing happen with Aimi and Mio? Would she kinda remind me?"
  "Oh, I'm also forgetting [persistent.playername_b]'s stuff"
  "I hope they have managed to get some information about Mio."
  scene black with wipeleft
  scene bg hotel2 with wipeleft
  scene black with wipeleft
  scene bg hotel with wipeleft
  show black onlayer front:
   alpha 0.6
  with wipeleft
  "I tell the girls to wait for me at the lobby since I'm going to stop by the reception area to give the recepcionist my card."
  "Or my room's key? I don't know."
  $ mi_name = "Recepcionist"
  mi "Goodnight ma'am, are you heading out?"
  kt "Yes, I'm going with my friends somewhere and we'll be back in thirty minutes."
  mi "All right then, your card please."
  kt "Sure! Here."
  "I hand my card to the recepcionist."
  mi "See you in 30 minutes then!"
  kt "Mhm~"
  "He smiles at me as I turn around."
  "I really like him, he's a very nice guy."
  kt "Okay girls, let's go!"
  $ mi_name = "Everyone"
  mi "Yes!"
  $ mi_name = "Mio"
  "We then leave the hotel."
  hide black onlayer front
  scene black with wipeleft
  scene bg st3 with wipeleft
  kt "Natsuki's place is literally two blocks ahead of us. It should be an easy walk."
  m "Okay!"
  y "Uuuu...O-okay..."
  "I take the lead as they follow me."
  scene black with wipeleft
  scene bg st3 with wipeleft
  "Since we all are sleepy already, we're barely talking to each other."
  "With that said, I can barely keep myself awake. I'm starting to feel kinda dizzy."
  "But well, this may be a necessary thing to do."
  scene black with wipeleft
  scene bg n_house3 with wipeleft
  "We have finally arrived at Natsuki's home, and I got to admit that...Well, it looks okay. Just that."
  kt "Okay, we're here."
  show monika 1bn at t11 zorder 1
  m "Ohhh...It's so cold here, isn't it?"
  kt "Yeah..."
  show monika 1bn at t21 zorder 1
  show sayori 1bb at t22 zorder 1
  s "Where is Natsuki's place?"
  kt "Hm..."
  kt "Here."
  play sound door
  "I knock on the door."
  $ nd_name = "???"
  show monika at thide
  hide monika
  hide sayori at thide
  hide sayori
  show natsukidad 1bd at t11 zorder 1
  nd "Who the fuck are you?"
  kt "Oh... Um... I-I'm Kotonoha, a friend of Natsuki..."
  "A tall and pink haired man reveals himself at the door. I suppose this rude guy is Natsuki's father."
  nd 2b "I'm sorry, I didn't ask for a thot to come. Piss off."
  kt "Ehhh?! I-I'm not a thot!"
  show natsukidad 2b at t21 zorder 1
  show monika 2bl at t22 zorder 2
  m "G-good night mister, we are Natsuki's friends and--"
  nd 5x "Ah, I see. You are those girls she talked about."
  nd 5i "{b}Natsuki! Get'cho ass over here, there is a silver haired girl with big titties waiting for you!{/b}"
  kt "Hey, stop being rude!"
  nd 5f "Shut the fuck up you baby rich girl."
  m "I'm sorry mister, we're not--"
  nd "Natsuki! Get the fuck over here or I won't let you go anywhere!"
  show natsukidad 5f at t31 zorder 1
  show monika 2bo at t32 zorder 2
  show sayori 2bl at t33 zorder 3
  s "E-excuse me sir, what is your name?"
  nd "Mitsuo. The name is Mitsuo."
  $ nd_name = "Mitsuo"
  show natsukidad 5f at t41 zorder 1
  show monika 2bo at t42 zorder 2
  show sayori 2bl at t43 zorder 3
  show natsuki 42ba at t44 zorder 4
  n "I said I was coming already!"
  nd 1d "Whatever, I want her back tomorrow after school."
  show natsukidad at thide
  hide natsukidad
  show monika 2bo at t31 zorder 1
  show sayori 2bl at t32 zorder 2
  show natsuki 42ba at t33 zorder 3
  "With that, he closes the door."
  "..."
  kt "God..."
  kt "What's wrong with him?"
  n 2bn "He's just like that."
  n "I... I really appreciate that you've come, Kotonoha..."
  "Natsuki's voice starts to break, but she holds back the urge to cry."
  kt "Let's get out of here, he might hear us."
  m 1bo "Indeed."
  show monika 2bo at t41 zorder 1
  show sayori 2bl at t42 zorder 2
  show natsuki 42ba at t43 zorder 3
  show yuri 3bv at t44 zorder 4
  y 3bv "I concur."
  n "Come on."
  stop music fadeout 2.0
  show monika at rhide
  hide monika
  show sayori at rhide
  hide sayori
  hide yuri at rhide
  hide yuri
  show natsuki at rhide
  hide natsuki
  "Natsuki looking to the ground, starts walking away."
  "Hm...What kind of father is that?"
  "Would that be Nat's problem? She can't stand her father?"
  "I mean, he doesn't seem to be a very nice person."
  "He called me a rich girl and a thot..."
  "He even ignored Monika."
  "Now everything makes sense."
  scene black with wipeleft
  scene bg st3 with wipeleft
  scene black with wipeleft
  scene bg hotel with wipeleft
  play music late fadein 2.0
  "We have finally arrived back at the hotel; I ask Natsuki to wait with the others."
  "I take my card, the girls standing up as I ask them to follow me."
  scene black with wipeleft
  scene bg hotel2 with wipeleft
  "Since Natsuki is coming with us, the air now feels kind of stagnating."
  "She's on the edge of crying, but she's holding back."
  "I actually really feel bad for her..."
  scene black with wipeleft
  scene bg hotel_hw with wipeleft
  pause 2.0
  scene bg hotel3 with wipeleft
  kt "W-well... M-make yourself at home, girls."
  "When we get back to the room the girls all sit down on the beds, while I take my nightgown and make my way to the bathroom."
  scene black with wipeleft
  scene bg hotel4 with wipeleft
  kt "{i}*sigh*{/i}"
  "Now what? I don't even know how to break the silence..."
  "This is becoming unsettling..."
  "I take my dress off, putting on my nightgown."
  "Once I finished, I step out of the bathroom."
  scene black with wipeleft
  scene bg hotel3 with wipeleft
  "The first thing I see is a very worn out group of 3 girls, meanwhile Natsuki is lying in the bed almost crying."
  "I think it's up to me to cheer her up."
  kt "Hey Nat, are you okay?"
  "Natsuki then sits on the bed and hugs me."
  show natsuki 12bh at t11 zorder 1
  n "You...You saved me tonight Kotonoha..."
  n "I thought you had forgotten me!"
  "Natsuki starts sobbing on my shoulder."
  kt "Did something happen with your father when we weren't around?"
  n "He..."
  "Despite willing to tell me what happened, I can say that she's having problems saying how she feels."
  "I give her some time to recover. She's still crying on my shoulder."
  "After a few minutes she lets go of me and tries again."
  n "He's been just terrible towards me since my mom left."
  n 12bd "He barely feeds me and he also..."
  n "..."
  kt "Oh..."
  n "Tonight instead of getting dinner, he decided to buy beer. I haven't eaten anything yet..."
  "Monika and the others was listening to our conversation, and despite being worn out, they come to us."
  show natsuki 12bd at t21 zorder 1
  show sayori 2bg at t22 zorder 2
  s "Natsuki..."
  show natsuki 12bd at t31 zorder 1
  show sayori 2bg at t32 zorder 2
  show yuri 1be at t33 zorder 3
  y "I-I didn't know you were going through that..."
  show natsuki 12bd at t41 zorder 1
  show sayori 2bg at t42 zorder 2
  show yuri 1be at t43 zorder 3
  show monika 4bh at t44 zorder 4
  m "Is there anything we can do to help?"
  n 12ba "N-no...I can deal with this myself!"
  n 12bh "I just..."
  "Natsuki once again bursts into tears."
  "Yuri and Sayori sit on the bed trying to cheer her up, but nothing seems to be working."
  kt "Natsuki?"
  n "Hm?"
  kt "Take this, go take a shower..."
  "I hand a towel, a bar of soap, and a bottle of shampoo to her."
  "She takes it and hugs me again."
  n 12bb "Thank you so much, Kotonoha... "
  extend "I really appreciate this."
  kt "Y-you can give me your clothes and I'll go to the laundry room to wash it."
  "I sweetly smile to her."
  n "Y-yes..."
  show natsuki at rhide
  hide natsuki
  show sayori 2bg at t31 zorder 2
  show yuri 2be at t32 zorder 3
  show monika 4bh at t33 zorder 4
  "With that, Natsuki goes to the bathroom."
  m 3bf "Geez...I hope Natsuki is alright..."
  y 2bh "I have never seen her like this before..."
  s 3bf "Neither have I..."
  kt "Well, I'm going to get the clothes basket."
  "I make my way to the bathroom."
  scene black with wipeleft
  play sound door
  "I knock on the door."
  kt "Can I come in?"
  n "Yes, come in."
  play music_bg2 shower
  scene bg hotel4 with wipeleft
  kt "Excuse me a moment."
  "I take the basket where Natsuki's clothing lies."
  n "Kotonoha?"
  kt "Yeah?"
  n "Thanks for this..."
  kt "Sure, you're welcome Nat. Actually, if it weren't for Monika and Yuri we would have forgotten you."
  n "Monika?"
  kt "Yeah."
  n "..."
  play sound closet_open
  "I was about to step out, but Natsuki stops me."
  n "Hey, Kotonoha?"
  kt "Hm?"
  n "Do you think I'm exaggerating?"
  kt "Huh? What about?"
  n "Am I being too rude towards Monika?"
  kt "Well, yeah. But I don't blame you."
  play sound closet_close
  "I close the door yet again."
  n "You don't blame me? If this is how Monika feels, I think I'm going way too far, aren't I?"
  kt "..."
  kt "Well..."
  n "I knew it..."
  kt "I-I don't know what to say..."
  window hide(None)
  window auto
  pause 2.0
  kt "..."
  kt "I'll get your clothes clean as soon as possible..."
  n "Thank you."
  "With that, I exit the bathroom."
  scene black with wipeleft
  stop music_bg2
  scene bg hotel3 with wipeleft
  show monika 2bf at t11 zorder 1
  m "Hey Kotonoha?"
  kt "Hm?"
  m 3bg "Do you think something happened with her father while we weren't around?"
  kt "Probably...I'd say yes."
  m "{i}*sigh*{/i}"
  m "Are you going to the laundry room?"
  kt "Yeah, I have to wash Nat's clothes."
  m 3bq"Oh...I see."
  m 1bp "Well, I can come with you if you want."
  kt "Actually I'd rather go alone."
  m "Hm..I see. Well, I'll wait with the others."
  kt "Yeah, do that."
  "I open the door and head out into the hallway."
  play sound closet_open
  scene black with wipeleft
  scene bg hotel_hw with wipeleft
  play sound closet_close
  stop music fadeout 2.0
  kt "{i}*sigh*{/i}"
  mc_b "What a difficult day, huh?"
  kt "Ah--!"
  kt "H-Hey, don't do that!"
  mc_b "And why not?"
  kt "I'm still not used to it!"
  mc_b "You should know that I'm coming already."
  kt "Well...Yeah, but don't do it out of the blue!"
  mc_b "Heh."
  "Thankfully there is a laundry room on each floor where a maid takes charge of washing clothes."
  "I make my way to the laundry room, and I politely talk to her."
  $ m_name = "Maid"
  kt "Good evening! I just stopped by to ask you to wash this."
  m "Oh, okay ma'am! I'll get it ready in around 20 minutes, okay?"
  kt "Sure!"
  kt "Oh, by the way...Would you please send a dinner for 5 people to my room as well?"
  m "Sure, I'll send it with your clean clothing!"
  kt "Okay, thank you~"
  m "For your convenience."
  "She takes a bow, and I leave the laundry room."
  scene bg hotel2 with wipeleft
  scene black with wipeleft
  scene bg hotel with wipeleft
  scene black with wipeleft
  scene bg st3 with wipeleft
  play music mend fadein 2.0
  kt "{i}*sigh*{/i}"
  "Since I'm all out of energy, I just rest against the wall."
  kt "Well [persistent.playername_b], what's new?"
  mc_b "Well...I didn't manage to get information about that 'Mio' girl."
  mc_b "Her memories are supposed to be gone."
  mc_b "However, I've found something that might resolve this question."
  kt "Oh? What is it?"
  mc_b "Look, it might be a dèjá vu thing but I'm not really sure."
  mc_b "Somehow, there are people who are able to recognize you even when they don't know you."
  mc_b "I tried to search a concept for that, but unfortunately I wasn't able to come up with something useful."
  kt "What does that mean?"
  mc_b "Considering the fact that we brought this world back, nobody knows you. But since this is basically a copy of the first world, the second world has information about the first world."
  mc_b "Meaning that--{b}"
  kt "--the people who used to know me in the first world, recall my face in this world..."
  mc_b "That's right."
  mc_b "As you may know we're not able to know if she's self-aware unless she has had played that piano in the school."
  kt "The same piano in Monika's space room..."
  mc_b "And since we don't know if she managed to get there--"
  kt "We won't know if Mio played the piano unless we know for sure she got access to that room and become self-aware."
  mc_b "Yep."
  mc_b "You did do your assignments, didn't you?"
  kt "Heh."
  kt "Kinda."
  mc_b "I see. "
  extend "Well Kotonoha, it seems this world is now stable and you won't need me anymore."
  kt "What? No! Don't leave me alone!"
  mc_b "You can do it girl. You're very intelligent."
  kt "W-what will happen with Naomi?!"
  mc_b "That's up to you."
  mc_b "See you soon Kotonoha, we'll meet each other again."
  kt "But wa--"
  call k_updateconsole("gm.localpersistent.unlink_mc_b(\"kotonoha.chr\")", "Unlinked " + persistent.playername_b + " from 'Kotonoha'.\nOperator commands transferred to 'kotonoha.chr'.") from _call_k_updateconsole_42
  kt "Huh?!"
  show screen invert(0.5, 0.6)
  call k_hideconsole from _call_k_hideconsole_3
  stop music
  kt "Noooo!!!"
  kt "[persistent.playername_b]!!!"
  kt "{i}*sob*{/i}"
  kt "Why...Just why?!"
  kt "This wasn't because I needed help..."
  kt "This was because you're the only one I need to recover Naomi!"
  kt "..."
  kt "Now what? What do I have to do?!"
  window hide(None)
  window auto
  pause 2.0
  kt "..."
  "So...They left for real..."
  kt "[persistent.playername_b]...I will never forgive you!"
  "Naomi, wherever you are...I swear I'm coming to you..."
  "I won't be okay until I manage to reach you again..."
  window hide(None)
  window auto
  pause 2.0
  "Right, [persistent.playername_b]?"
#  $ persistent.title[1] = True
  $ persistent.volume = 2
  scene black with dissolve_scene_full
  call act1_ch2_d3 #from _call_act1_ch2_d3

image bg mc_br = "mod_assets/houses/mc_bathroom.png"
image bg mc_brb = "mod_assets/houses/mc_bathroom-b.png"
image bg mc_brc = "mod_assets/houses/mc_bathroom-c.png"

label act1_ch2_d3:
 stop music fadeout 2.0
 scene black 
 with dissolve_scene_full
 show text("{size=100}{color=#6debab}{b}Day{/b}{/size}{/color}\n{size=60}3{/size}"):
  truecenter
 with Dissolve(1.0)
 pause 4.0
 scene black
 with dissolve_scene_full
 play sound clock
 window hide(None)
 window auto
 pause 5.0
 scene bg bedroom 
 with dissolve_scene_full
 "{i}*yawn*{/i}"
 $ perspective = "mc"
 call perspective_window
 "Oh my God...this is the first time I have had enough sleep since this all of this happened."
 "I mean, I'm still kind of sleepy, but overall I'm alright."
 "6:00 AM. How did I manage to wake up an hour before my alarm clock went off?"
 "I should probably try and get some more sleep...but oh man, I wouldn't want to oversleep again."
 "Like, this is the first time I have woken up in a good mood, and falling asleep and being late for school would really annoy me."
 "Whatever, I'm gonna take a shower and...I don't know, maybe some video games as well--"
 play sound doorbell
 "...?"
 "Huh? Who has come to my place this early?"
 "I don't think they know that it's rude to pay a visit to others' places without letting them know first."
 "Well, I think I don't have much of a choice then to go open the door and see who's there."
 "Yawning, I slowly make my way to the door."
 scene black with wipeleft
 scene bg mc_lr with wipeleft
 play sound doorbell
 mc "Yeah, yeah! Just a moment, I'm coming already!"
 scene black with wipeleft
 scene bg mc_hw with wipeleft
 "As I come close to the door, I see an orange head of hair through the glass."
 "Wha?! Is that Mio?"
 "What is she doing here?!"
 mc "Who is this?"
 mi "It's Mio, [player]! May I come in?"
 "I open the door, finding Mio in my field of vision."
 play music t6 fadein 2.0
 show mio 1bf at t11 zorder 1
 mi "Hello, [player]!~ I've come to visit you!"
 mc "Huh?! How did you even get here?"
 mi 3by "{i}*That's not important.*{/i}"
 "Somehow the way she said that sends a shiver to my spine. What is wrong with her?"
 "It's only 6:05 AM!"
 "She has also brought some bags; I'm unsure of their contents, though."
 mc "I'm sorry Mio, but I think you should leave. I'm kind of busy and need to get ready for school."
 mi 8bx "That's why I'm here! Don't you need someone to make breakfast for you?"
 mc "...No?"
 mc "I mean, I've been living by myself for quite some time and I can manage making breakfast on my own."
 mi 5bm "Awwww..."
 extend 5bl "Can I at least stay here until it's time for school?"
 mc "No."
 mi 4bh "Pleeeaseeee?"
 "God...this girl is so insistent... she clearly won't stop until I tell her what she wants to hear."
 "Now that I think about it, Mio isn't even wearing her school uniform. What time does she wake up exactly??"
 mc "Did you go somewhere else before coming here?"
 mi 7bb "Oh, well...yeah. I went to the grocery store and I got some delicious meals for breakfast!"
 mc "Huh..."
 mc "Are you going to school today?"
 mi 2be "Yes, I have my uniform here with me."
 mc "{i}*sigh*{/i}"
 mc "Alright fine, but next time you come over, please let me know before you do."
 show mio 3bx at h11 zorder 1
 mi "Of course!"
 mc "Good. You can come in."
 "Mio nods, stepping in and making her way right to the living room."
 scene black with wipeleft
 scene bg mc_lr with wipeleft
 "Mio is looking around like she's never been in a living room before. I'm walking behind her."
 "She places that heavy looking bag on the couch and then sits down."
 show mio 1ba at t11 zorder 1
 mi "Hey [player], can I take a shower in your bathroom?"
 mc "As long as you have clean underwear and a clean uniform, go for it."
 mi 3bl "O-oh! W-well... that's... sort of inconsiderate of you to mention my underwear, but...I'll let it pass for now!"
 mi 5bl "Here, can you please take this to the kitchen? I won't take too long."
 mc "Please don't, I need a shower myself."
 mi 8be "Sure! Thank you~"
 mc "The bathroom is in my bedroom, it's the first door to the left. Just climb those stairs."
 show mio at rhide
 hide mio
 "With that, Mio nods. She then takes her purse and goes to the bathroom."
 "I take the bag of supplies Mio brought with her."
 mc "Wha?--"
 mc "Man, this is incredibly heavy! What did you bring, Mio?"
 "I know she can't hear me, but I needed to say that out loud."
 "Saying nothing else, I make my way to the kitchen."
 scene black with wipeleft
 scene bg kitchen with wipeleft
 "Thank God the kitchen is next to the living room so I don't have to go very far. When I get to the kitchen I put the bag on the table."
 mc "Let's see what Mio has here..."
 "I open the bag, revealing that Mio bought a whole bunch of groceries."
 "3 cereal boxes, 3 gallons worth of milk, 4 yogurt jars and a dozen eggs."
 "Is Mio gonna feed a family of 5 people or something?!"
 "Whatever, I just put everything back in the bag and wait for her to finish."
 scene black with wipeleft
 scene bg kitchen with wipeleft
 "It's been 20 minutes already, what is she doing in there?"
 "Man, it's getting late...I haven't even taken a shower!"
 "Not to mention that I don't even know anything about what happened with the girls...I wonder how their sleepover went."
 "I hope everything went alright."
 "We're also supposed to share poems again. Hopefully that'll go well, too..."
 "Everyone's poems felt way too depressing last time."
 "Well... Mio's poem was just meh, if you can call it a poem. It was just okay."
 show mio 1a at t11 zorder 1
 mi "I'm back [player]!"
 mc "Ah!--"
 mc "God, don't do that Mio! You scared me!"
 mi 3y "Uhuhu~"
 mi 3x "Was this the first time?"
 mc "..."
 mc "What?"
 mi 1m "Oh, nevermind."
 "That was... {i}really{/i} creepy..."
 show mio 1d at t21 zorder 1
 "What did she mean by that..?"
 show mio 1d at t41 zorder 1
 "Mio comes close to me, grabbing the bag and taking everything out."
 show mio 1d at t43 zorder 1
 "Her movement is as delicate as Yuri's, now that I think about it."
 show mio 4d at t11 zorder 1
 mi 4d "Um...[player], weren't you going to take a shower?"
 mc "Oh, yeah. Be right back then."
 mi 4a "Mhm~ I'll have breakfast ready before you come back!"
 mc "Alright. Don't do anything else after that while I'm gone."
 mi 8e "I won't, don't worry!"
 "I head right to the bathroom."
 stop music fadeout 2.0
 scene black with wipeleft
 scene bg bedroom with wipeleft
 scene black with wipeleft
 scene bg mc_br with wipeleft
 "Man... I can't help thinking why Mio knows where my house is."
 "Does she live near here?"
 "Honestly I don't think so... it'd be a freaky coincidence."
 "Well, I have to drop it for now and take a shower already, it's very late."
 scene kitchen with dissolve_scene_full
 $ perspective = "mio"
 call perspective_window
 "[player] has gone to take a shower, meaning I can start cooking breakfast for the two of us."
 "This place is just like I remember... when [player] and I became one..."
 mi "Uhuhu~"
 "I laugh to myself, taking my hand to my mouth."
 "It's a shame [player] doesn't remember the {i}good time{/i} we had on this table..."
 "It really makes me sad, but I swear [player] will be mine again, and so it shall be!"
 "Hopefully he'll realize how much I love him, and he'll stop pursuing that fucking bragger Monika..."
 "Just like I did in the old world, I'll manage to keep him by my side... but there's something I don't understand..."
 "Why are certain things different in this one?"
 "Things didn't happen the way it did in the world when that [persistent.playername_b] person made me self-aware..."
 "In that world, Kotonoha didn't even know [player], but she does in this one."
 "[player] was pursuing Monika too, but I managed to get him to be with me anyway."
 "He thought I was so cute, but this world's [player] hates me to the core..."
 mi "{i}*sigh*{/i}"
 "Why does he hate me? What did I do?"
 "I would have preferred waking up in my bed with no memories of everything I went through."
 "The excitement he made me feel when I let him take my virginity on this table...~"
 "But this is no time for giving up! [player] was and will continue to be mine forever!"
 "{i}Even if I have to kill all of his friends...{/i}"
 "{i}...including Kotonoha.{/i}"
 "Well, Kotonoha and I known each other in the Music Club, and we used to be good friends in the world I came from."
 "But it seems she hates me in this world as well."
 "This world is so full of paradoxes..."
 mi "Mmmmm~"
 "Eggs with bacon were [player]'s favorite breakfast! But I wonder if this world's [player] loves it too."
 mi "Now, time for some cereal!"
 "I take a bowl from the pantry, grabbing a milk jug and a cereal box."
 mi "{i}*humming*{/i}"
 mi "Aaannndd... There we go!"
 "As I put mine and [player]'s breakfast on the table, I hear the water has stopped from his room."
 mi "Just in time as usual!~"
 "You'll be mine yet again, [player]..."
 "{i}You'll be mine...{/i}"
 scene bg mc_br with dissolve_scene_full
 $ perspective = "mc"
 call perspective_window
 "Aaahhhh... there's nothing quite as relaxing as a shower in the morning!"
 play music nday fadein 2.0
 "I'd be more relaxed if Mio wasn't lurking around in my home."
 "For now I'll just ignore the fact that she came to my house with no knowledge of where I live."
 "Now, let's put on my uniform."
 scene black with wipeleft
 scene bg bedroom with wipeleft
 mc "There!"
 mc "Huh? Did I iron my uniform?"
 "I mean, it's not like I don't iron my uniform, but I always do that {i}after{/i} I'm done."
 "Whatever. I probably did, but can't remember."
 "Damn my lousy memory."
 "Having my coat on my bed and hastily tying my tie, I make my way to the kitchen."
 scene black with wipeleft
 scene bg kitchen with wipeleft
 "As I see the orange-haired girl cooking breakfast on the stove, the smell of eggs and bacon fills the whole room."
 show mio 1a at t11 zorder 1
 mi "Oh, hey [player]!"
 mc "I'm back."
 mi 2x "Mhm~"
 mi 2e "There, sit down, your bowl of cereal is ready!"
 "Mio has put a bowl with cereal on the table, along with a glass of milk and some strawberries on a small plate."
 mc "Huh..."
 mi "Oh? Did something happen, [player]?"
 mc "Ehh...no, I'm okay."
 mi 4e "Okay! Come on, school starts in an hour.~"
 "This is some serious dèjá vu..."
 "Why do I feel like I've seen this happen before? It feels like Mio has come to my home before, but I can't recall her ever being here..."
 "It feels so weird..."
 "Whatever, I should start digging in if I want Mio to leave me alone."
 mi 2e "And here is your eggs with bacon!"
 mc "Hm...thanks."
 mi 5x "Don't be shy [player]! This is the least I can do to show my gratitude to you!"
 mc "Gratitude? What are you feeling grateful for?"
 mi 5a "Because you allowed me to stay here for a while and take a shower."
 mi 8e "So I cooked this for you!"
 mc "You really didn't need to do that."
 mi 6f "I wanted to, though."
 mc "{i}*sigh*{/i}"
 mc "Alright then. Thanks for the meal"
 show mio 5x at h11 zorder 1
 mi "Come on, we still have a school day ahead us!"
 mc "Yeah."
 show mio at thide
 hide mio
 "I take my phone out of my pocket, I start dialing Monika's number--"
 show mio 8q at t11 zorder 1
 mi "[player], put your phone down! We're having breakfast, don't you think it's impolite to play on your phone while we're eating?"
 mc "Well, I actually always do this, so don't mind me."
 mi 2r "I'm here, just so you know."
 mc "It's not like you're my mom or anything."
 mi 8t "You're so mean [player]!"
 show mio 8u at t11 zorder 1
 "Mio pouts, looking kind of mad."
 "Well, if it weren't for my mom teaching me to respect women, I would just ignore her and call Monika. I don't think that's the wisest idea right now, though."
 "I put my phone back in my pocket, then look back at Mio."
 mi 2v "Thanks."
 mc "Mhm, sure."
 show mio 2r at t11 zorder 1
 "Mio's sweet and harmless aura has turned into a heavy and weirdly aggressive one."
 "I think I really made her mad..."
 "I mean, I don't really care about her, but now that I think about it... I shouldn't be {i}this{/i} rude to her."
 $ style.say_dialogue = style.normal
 "And, to be honest, I feel bad for being that rude..."
 "I think I should apologize."
 mc "I'm sorry for all that."
 mi "..."
 mi 1i "Do you hate me or something?"
 mc "No."
 mi 3i "Then why are you this rude to me? I didn't do anything!"
 mc "I'm sorry. It's just the way I am."
 mi 3k "..."
 stop music fadeout 2.0
 mi 2j "Fine."
 "Mio resumes eating her food."
 "I think that's it."
 scene black with wipeleft
 scene bg kitchen with wipeleft
 "We continue to eat our breakfast in silence, but I have to say this silence feels different."
 play music t6 fadein 2.0
 "Not a common silence, but an awkward and unsettling one."
 "She's probably really mad right now, and despite the fact that I don't like her at all, I'm feeling remorseful about it."
 "I can't be too kind , though, or she might think I want to be her friend or something."
 "Honestly, I don't want to be rude to her again, but I don't want her to be around me either."
 "I'll try to just be neutral. I don't want her to overthink things."
 "Whatever. I'm done with my breakfast, so I stand up and take my dish to the dishwasher."
 show mio 1c at t11 zorder 1
 mi "Eh? Oh, it's okay [player], I'll wash both of our dishes."
 mc "We don't have enough time for that, I'm just going to put my dishes in the dishwasher."
 mi 3g "Oh... well, I guess you're right..."
 mc "Come on, we gotta go to school. I'm just gonna head up to my bedroom for a minute."
 mi "Sure, just don't take too long~"
 mc "I won't."
 "I leave the kitchen and climb the stairs to my bedroom."
 scene black with wipeleft
 scene bg bedroom with wipeleft
 mc "Geez..."
 "I don't know why Mio is behaving like my mom, but even so I'll try to respect her... despite everything weird so far."
 "Fortunately it's just gonna be today... I don't think I could stand this everyday."
 "Well, I'm gonna call Monika."
 play sound closet_close
 "I close the door so Mio doesn't hear me. I then take my phone out of my pocket and I dial Monika's number."
 window hide(None)
 window auto
 pause 1.0
 m "{i}Hello?{/i}"
 mc "Hey Monika, it's me."
 m "{i}Oh, hello [player]! How are you?{/i}"
 mc "Well, I woke up at six in the morning, so... I'm sleepy. What about you?"
 m "{i}I'm very good!{/i}"
 mc "Nice to hear that. Um... hey, I have a question..."
 m "{i}Hm? Did something happen?{/i}"
 mc "Kind of."
 m "{i}What is it?{/i}"
 mc "Did you tell Mio where I live?"
 m "{i}Ehm... No, why?{/i}"
 mc "Because she's at my place right now. She didn't even allow me to call you because 'it's impolite to play on the phone out while having a meal.'"
 m "{i}Why on earth is Mio there? *sigh* Just a moment... I'm going to ask the others.{/i}"
 "I hear Monika call for the others, she then asks them the same question I asked her."
 "Kotonoha, Sayori, Yuri and Natsuki reply, saying the one thing I didn't want to hear at all."
 kt "{i}{alpha=0.3}Um... no, I don't think I did.{/alpha}{/i}"
 s "{i}{alpha=0.3}Neither did I.{/alpha}{/i}"
 y "{i}{alpha=0.3}No, she might live near there?{/alpha}{/i}"
 n "{i}{alpha=0.3}No.{/alpha}{/i}"
 m "{i}*sigh*{/i}"
 m "{i}No [player], none of us told her where you live.{/i}"
 mc "..."
 mc "Well, I was kind of expecting that answer."
 mc "Whatever... since Mio is here with me, it'd be better if you girls go to school without me."
 m "{i}Oh, that's a shame...{/i}"
 m "{i}... but we're actually at Sayori's house right now!{/i}"
 mc "Really?"
 m "{i}Yep.{/i}"
 mc "Hm... alright then..."
 mc "Well, it's too late anyway. I think it's time to go. I'll see you all at the club, alright?"
 m "{i}Alright! Stay safe~{/i}"
 mc "Same to you."
 "I hang up and grab my backpack."
 scene black with wipeleft
 scene bg kitchen with wipeleft
 "I see Mio washing her dish in the sink, she comes to me afterwards and grabs her belongings."
 show mio 1a at t11 zorder 1
 mi "Let's go [player]!"
 mc "Wait wait wait, you're not gonna take all that with you?"
 "I point at the groceries lying on the pantry."
 mi 3f "Oh! Well, actually I'm gonna stay with you for a couple of days!~"
 mc "Wha-!?"
 mc "I didn't even give you permission to stay here in the first place!"
 mi 5x "Uhuhu~"
 show mio at lhide
 hide mio
 "Saying nothing else, Mio makes her way outside, leaving me alone."
 mc "God, this woman!"
 mc "{i}*sigh*{/i}"
 "How am I supposed to explain this to Monika?!"
 "Even if I don't say anything to Monika, she'll realize it eventually!"
 "Man... Mio is such a meddler..."
 "Well, that's yet {i}another problem{/i} I have to solve."
 "I open the door and leave."
 scene black with wipeleft
 scene bg house with wipeleft
 show mio 6l at t11 zorder 1
 mi "Um... where is our school, [player]?"
 mc "So you managed to come to my house, but you don't know how to get to school from here? You're unbelievable, woman."
 mi 1l "A-Ahaha... w-well, I'm not perfect... we all know that."
 mc "Me? Why would I know that?"
 mi "Just forget it, I'll follow you!"
 mc "...!"
 show mio at thide
 hide mio
 "Mio walks past me as she waves her hand."
 "Man I'm starting to freak out... why would I freaking know if she's not perfect??"
 "...Unless she meant that in another way and actually it's me overthinking."
 "I decide to just catch up to her and we both walk to the train station."
 scene black with wipeleft
 scene bg street with wipeleft
 "Thank God the train is only 4 blocks away from my home, so it'll just take a short while to get there."
 "Mio is, curiously enough, acting really happy and defenseless right now. It's showing in her behavior."
 "Is this girl trying to get me to hate her for real?"
 "I'll talk to Monika and Kotonoha about this."
 "With that said, Mio has been walking very close to me and trying to start a conversation."
 "I reply with disdain, but still trying not to be rude about it."
 mc "This time we're going to school in the train, so we won't be late."
 show mio 1c at t11 zorder 1
 mi "Well, it's almost eight, so I'd say we are somewhat late..."
 mc "{i}*sigh*{/i}"
 mc "Well, even so we're using the train this time. Is that okay with you?"
 mi 4c  "Oh, yeah, it is."
 mc "Fine."
 scene black with wipeleft
 "We both enter the station, I take my badge out and I hand it to Mio."
 mc "Have you ever gone to school using the train?"
 mi "Not really."
 mc "Well, then take this. Just stick it to that glass pane and the turnstile will unlock itself. Got it?"
 mi "Uhuhu!~ "
 extend "Even if I haven't gone to school by train doesn't mean I have never used it before!"
 mc "Oh... well, that's fine then."
 "Saying nothing else, Mio takes my badge and quickly passes it through the sensor, immediately unlocking the turnstile."
 "She gives it back to me and I do the same myself."
 scene bg train with wipeleft
 stop music fadeout 2.0
 "Mio and I walk to the platform, and as we see the train coming--"
 $ sk_name = "???"
 play music nday fadein 2.0
 sk "Hey you!"
 "I turn to see a girl with the same hair color as Sayori's, wearing a red ribbon on her head."
 sk "Hey!"
 show naomi 1g at t11 zorder 1
 mc "Huh?"
 sk 2i "Yeah, I'm talking to you!"
 mc "Me?"
 sk 2d "Mhm."
 show mio 6c at t41 zorder 1
 show naomi 2d at t42 zorder 2
 mi "Oh? Naomi?"
 $ sk_name = "Naomi"
 sk "Oh... "
 extend 4a "Hello Mio!"
 mi 8f "Hellooo~"
 sk 3b "How are you doing?"
 mi 3e "I'm alright! What about you?"
 sk 2e "Well, I'm on my way to school. Have you seen Akane?"
 mi 3l "A-Akane?"
 sk 2b "Yeah! The flutist girl from our club."
 mi 5l "O-oh! I haven't, actually..."
 sk 1a "I see."
 mi 1m "Oh, by the way, I'm not a member of the music club anymore."
 "I pull Mio's sleeve, just so she knows the train is about to arrive."
 mi 1d "Eh?"
 mc "Are you even paying attention? The train is arriving already."
 mi 1l "Ahaha...I'm sorry, [player]..."
 sk 2g "Oh yeah, so, you're {i}[player]{/i}..."
 show mio 1a at t41 zorder 1
 "The girl whose name seems to be Naomi, raises her finger and points at me."
 "I can feel a sweet aura, just like Mio's!"
 mc "Yeah?"
 sk 4h "You called me 'Sayori' the day before yesterday! "
 extend 4p "Who is Sayori?!"
 mc "Guh!--"
 "What? I didn't expect her to be another person!"
 "But now that I think about it, she looks almost exactly like Sayori... how was I supposed to know?"
 mc "Well, I just confused you with a friend of mine. You both look so alike that you could be twins."
 sk 1n "A friend of yours?"
 extend 2n "Oh wow, I didn't expect to have a twin!"
 extend 2e "Can I meet her?"
 mc "I don't know, she's going through some difficult times at the moment, but if you want you can meet her in the Literature Club today."
 sk 4g "The Literature Club? But I'm perfectly fine in my club!"
 mc "I'm not asking you to become a member. I'm just saying that if you want to meet her, you shoud pay us a visit."
 mi 2x "Do it, Naomi!~ It'd be so much fun having you there at, least for today!"
 "Naomi stares at me for a while. It seems like she doesn't know what to say."
 show mio 2w at t41 zorder 1
 "Mio's expression is begging her to go. She sighs and returns her gaze at me."
 sk 2h "Well, we're not having a meeting today so... I think I might go."
 sk 4h "But don't get your hopes up, alright?"
 mc "Don't worry, I'm getting used to that."
 sk 3b "Tehehe!~ "
 sk 3k "You kinda remind me of Akane, you know?"
 mc "Yeah I don't think I know that Akane girl you're talking about, but thanks I suppose."
 sk 4a "The train's here. Let's go!"
 mi 5w "Yaaaaaayyy! Today is gonna be so much fun having you around!"
 sk 3b "Tehehe!~  Well, I'm not gonna stay, but if I like the environment, you guys are gonna see me lurking around every now and then!"
 mc "Sure. Come on, let's go."
 show mio at rhide
 hide mio
 show naomi at rhide
 hide naomi
 "Mio and Naomi both nod and we step into the train."
 scene black with wipeleft
 scene bg train_a with wipeleft
 "The girls take a seat, I decide to just stand while we arrive to school."
 "And since it's just 4 stations away anyway, it would be senseless if I took a seat."
 "I usually prefer taking the train to school by default because it's faster than walking."
 "It's even faster than taking the bus, surprisingly."
 "Mio and Naomi are having a conversation in the meantime."
 show naomi 1a at t11 zorder 1
 sk "So Mio, where did you meet [player]?"
 show naomi 1a at t21 zorder 1
 show mio 1a at t22 zorder 2
 mi 3c "Oh, well... basically, he crashed into me and I dropped my books..."
 mi "And then he invited me to join his club after helping pick them up!"
 sk 1b "I see. "
 extend 2q "Soooo... you stole my Mio from the Music club, didn't you?~"
 "Naomi stares at me. Despite her comment being kind of agressive, she's keeping a smile on her face."
 mc "Eh... kind of."
 sk 1g "'Kind of? What's that supposed to mean?"
 mc "Our president also didn't like that I stole another club's member, but she allowed it anyway."
 mc "And... well, she liked the club and decided to join."
 sk 4p "Even so, you still stole her!"
 show mio 3g at t22 zorder 1
 mc "I mean, as I said: she liked the Literature Club, so I don't really think I {i}stole{/i} her, per se."
 sk 1p "Uwa--"
 sk 1i "Well... I guess you're right..."
 mc "Gotcha~"
 sk 4a "So, have the Literature Club members been treating you well?"
 mi 1k "Mostly."
 sk 1f "Mostly?"
 mi 5l "Yep, if it weren't for the fact that [player] was being rude to me this morning, it would be just perfect."
 sk 1c "Eh?! Has [player] hurt you or something? Did he try to assault you?!"
 mc "Hey girl, don't make such a severe judgement about me. I'm not that kind of guy."
 mi 5x "I know you're not, [player]!"
 mi 8e "Anyway, no. [player] has been... um... kinda disrespectful towards me."
 mi 3e "But even so, I like hanging out with his friends! They're all so nice~"
 sk 1a "I've heard Sayori is the vice president, but that's it."
 mi 1a "Mhm~"
 "I was listening to their conversation and saying something every now and then, but--"
 mc "Oh God!"
 mc "Girls, we're here! We gotta leave before the train starts leaving!"
 sk 1n "Uwa--"
 mi 2i "Oh no, come on!"
 "We hastily step out of the train and land in the station in front of the school."
 scene black with wipeleft
 scene bg train with wipeleft
 "Mio, Naomi and I quickly run out of the train station. Naomi seems to be a very athletic person... she's just as fast as Monika!"
 "With that, I have to say that Mio is probably as fast as I am, but... which is only a little bit slower than Monika."
 scene black with wipeleft
 scene bg school_front with wipeleft
 "As we leave the station, the school building immediately becomes visible."
 "Fortunately it's only 8:21 AM, so I think it'd be better if I tell the girls to just walk slowly."
 mc "Hey girls, it's only 8:21, would you mind if we slow down a little? I'm... not used to running this much."
 show naomi 3l at t11 zorder 1
 sk "Tehehe!~  Sure, let's walk a little bit slower."
 mc "Thanks..."
 show naomi at thide
 hide naomi
 "Even when Naomi is walking at a normal pace, she's still faster than me! I'd say even faster than Monika somehow!"
 "Whatever, Mio's walking speed  - since she's not that tall - is more normal."
 "How did we even run past this girl? I can't believe I called her \'Sayori\'! She {i}does{/i} look just like her, though..."
 "I want to know something... is she as cheerful as Sayori?"
 "...as positive as her?"
 mc "Hey, Naomi."
 "Naomi turns to see me."
 show naomi 1b at t11 zorder 1
 sk "Yes?"
 mc "Uhm... what do you think of this morning?"
 sk 1d "Um... What kind of question is that?"
 mc "An 'asking for your opinion' one."
 sk 4g "Wow, I've never been asked such a weird question..."
 sk 2e "But if you're that interested, it's a very nice day! I am looking forward to starting the school day!"
 mc "Ahh... I see..."
 show naomi 2e at t21 zorder 1
 show mio 5x at t22 zorder 2
 mi "You're a very cute person Naomi, did you know that?"
 sk 3b "Kindaa~"
 show mio at thide
 hide mio
 show naomi 1a at t11 zorder 1
 "Now that I think about it, Naomi has the same accent as Kotonoha's... are they both from Osaka?"
 mc "Naomi... Can I ask something kind of private?"
 sk 2h "Um, it depends. What is it?"
 sk 2b "Wait wait wait, lemme guess..."
 sk 1i "No, I don't have a boyfriend, and I don't want one."
 mc "What? No, it's not about that!"
 sk "Oh... "
 extend 3h "I'm sorry! I'm getting way too used to hearing that question, y'know?"
 mc "No, I want to ask you where you are from."
 sk 4b "Ah. Well, I'm from the Kobe prefecture in the Kansai region."
 mc "I see."
 mc "Have you ever met a silver-haired girl before?"
 sk 1g "Um..."
 sk 1h "I don't think I have?"
 mc "Well, if you come to the Literature Club, you'll get to meet her."
 show naomi 1h at t21 zorder 1
 show mio 3b at t22 zorder 2
 mi "Whatever. Hey, Naomi, do you have plans today?"
 sk 1h "Other than go to your new club and getting my homework done, no."
 mi 1x "Nice! Would you want to go out somewhere after school?"
 sk 1g "Hm... sure! "
 extend 3l "Can I bring Akane with me?"
 mi 6k "Oh! Well... um... I--"
 sk 4l2 "I know you love her, you two just get along so well!"
 mi 1l "Ahaha... s-sure, why not?"
 "I can see the doubt overcoming Mio. Does she even {i}know that{/i} Akane girl Naomi is talking about?"
 "As I said, there's definitely something wrong with that girl."
 scene black with wipeleft
 scene bg school_corridor with wipeleft
 "We finally arrive at school and Naomi goes to her classroom, leaving just me and Mio."
 "Oh God, I forgot she's staying at my place! How am I going to explain this to Monika??"
 "What I am supposed to say?! Mio didn't even give me a chance to think about it!"
 "At least she's got some good cooking skills..."
 "Well...I think I'm gonna tell her about this...I shouldn't hide that from her after that."
 show mio 1c at t11 zorder 1 
 mi "[player]?"
 mc "Hm?"
 mi 4b "Please... don't talk to Kotonoha about Naomi again."
 mc "Um? Why is that?"
 "Wait, {i}again{/i}?"
 mi 4q  "Because I don't want you to!"
 mc "Like, for no reason? If she comes, she'll just see her regardless."
 mi "I said don't!"
 mc "..."
 mc "Why are you so concerned about that to begin with?"
 mi 6v "It's nothing."
 mc "Then I'm free to say whatever I want. Don't you think so?"
 "Mio ignores my question, even avoiding eye contact with me."
 "We walk into the building."
 scene black with wipeleft
 scene bg corridor with wipeleft
 "Mio seems pretty pissed, but also worried."
 "I want to know what I did to get her so mad at me. It's like I did everything wrong!"
 "Actually, on second thought, I don't care."
 scene black with wipeleft
 scene bg class_day with wipeleft
 "Mio and I step in the classroom, and I see Sayori already sitting in her chair."
 "As she sees me, she stands up and cheerfully greets me."
 show sayori 1a at l11 zorder 1
 s "Hey, [player]!"
 mc "Good morning Sayori. How's it hanging?"
 s 3x "Pretty good, actually! I haven't slept that well in my whole life~"
 mc "Was that because of you staying at Kotonoha's place?"
 s 1r "Yep."
 mc "So... I'm guessing everything went well, right?"
 s 1l "Well, yeah?"
 show sayori 1l at t21 zorder 1
 show mio 1c at t22 zorder 2
 mi "I'll talk to you later, [player]."
 mc "Oh, alright."
 show mio at thide
 hide mio
 show sayori 1l at t11 zorder 1
 "Mio, yet again butting in our conversation, takes a seat right behind me."
 mc "So, what do you mean by 'yeah?'?"
 s 2a "Kotonoha sent a nice dinner to the room, but we decided to wait for her since she was out."
 mc "Out? Why?"
 s 2b "I don't know... but the maid told us she went outside. Apparently she was on the bridge staring at nothing."
 mc "Wait wait wait, how did you even see her?"
 s 3x "Because we have a view of the street from her room!~"
 mc "Ah, that makes sense."
 s "So, yeah..."
 mc "I see."
 play sound school_ring
 window hide(None)
 window auto
 pause 2.0
 mc "Well, that's it. Let's get started."
 # 
 s "Yes!"
 "The professor's timing is perfect as he gets in the classroom."
 "And so we begin with yet another school day."
 scene black with wipeleft
 scene bg class_day with wipeleft
 $ persistent.still_in_perspective = True
 call perspective_window
 "The teacher just started today's math topic: square roots and other useless things we will never use in our life."
 "Why does school keep teaching us this kind of stuff? I mean... I can't think of any reason I'll ever need this stuff."
 "Even so, I really don't want to fail, so I'll just have to bear it."
 "This may be the first time I {i}don't{/i} want the club to start... I don't know, I have a bad feeling something is going to go wrong today."
 "My concern is even greater for Natsuki specifically... she was behaving differently earlier; she's not acting like the Natsuki I know."
 "Almost like she was... in pain? Or something?"
 "She was probably just sick. I don't know."
 "I'm not giving it my all to those I want to protect..."
 "I'm failing them... again. Is that what Natsuki is so mad at me about?"
 stop music fadeout 2.0
 "Maybe... maybe not... but I swear I'm gonna start to give it my all!"
 "And if I want to give them that happy life I promised them, I have to try."
 scene bg kt_classroom with dissolve_scene_full
 $ perspective = "kotonoha"
 call perspective_window
 "*sigh* School and studying sure have become boring since I became self-aware."
 "Is it because of the fact that I know everything?"
 "I mean, not school stuff, but the truth of this world."
 play music nday fadein 2.0 
 "I just can't help it. And now that [persistent.playername_b] has left me, I don't think I can ever reunite with Naomi."
 "Geez... I really want to talk to her again..."
 "Or even see her one more time, just to make sure she's doing alright."
 "If I didn't have far more important things to do right now, I would definitely make the effort to try to talk to Naomi."
 "Someday I hope I'll get to see her again."
 play sound school_ring
 window hide(None)
 window auto
 pause 2.0
 "Finally! Break time."
 "I turn to Natsuki, who's looking kinda down right now."
 kt "Hey Nat, you ready to leave?"
 show natsuki 2s at t11 zorder 1
 n "Yeah, sure."
 kt "Let's eat lunch together."
 n "N-no, I would prefer--"
 kt "I'm not taking 'no' for an answer. Come on, let's get going already."
 n 2m "...Okay, Kotonoha..."
 kt "Alright~ Let's get going, then!"
 "Nat and I leave the classroom, making our way to the courtyard."
 scene black with wipeleft
 scene bg corridor with wipeleft
 "As we walk through corridor, we see [player] walking down the hallway with Sayori and Mio."
 "[player] seems to be giving Mio glances of contempt while doing so."
 "So... [player] doesn't get along with Mio after all..."
 "He then comes to us and Natsuki looks down towards the floor."
 show mc2 1a at t11 zorder 1
 mc "Good morning girls."
 kt "Hello!"
 show mc2 1a at t21 zorder 1
 show natsuki 1q at t22 zorder 1
 n "...morning."
 mc 2c "Are you two going somewhere?"
 kt "Well... yeah? I think it's lunch time, isn't it?"
 mc 2k "Hahaha! Yeah, you're right."
 mc 1d "Actually I wanted to talk to you about something, Kotonoha."
 kt "Oh? What is it?"
 mc "It would be better if we talk about it elsewhere."
 "[player] points to the classroom to my left."
 mc 2d "Sayori, Mio, please wait here with Natsuki, alright? We'll be right back soon."
 $ s_name = "Sayo & Mio"
 show natsuki at thide
 hide natsuki
 show mc2 2d at t31 zorder 1
 show sayori 1a at t32 zorder 2
 show mio 3a at t33 zorder 3
 s "Okay [player]~"
 "With that, [player] and I enter the classroom."
 scene black with wipeleft
 scene bg class_day with wipeleft
 "I close the door behind me. It's just the two of us now."
 "[player] asks me to sit in a chair as he takes a seat nearby."
 show mc2 1d at t11 zorder 1
 stop music fadeout 2.0
 mc "So..."
 kt "'So...'?"
 mc 4d "Well, Sayori told me you were out on the bridge last night."
 mc 4w "What were you doing out there?"
 kt "..."
 kt "I had some--"
 show mc2 4w at h11 zorder 1
 mc "Kotonoha!"
 kt "Ah...!"
 kt "What?!"
 mc 2w "You always have something to do, isolating yourself from the group!"
 kt "Eh?!"
 mc "You are hiding something and I bet it's everyone's concern, isn't it?"
 kt "What? Where did you get that idea from?!"
 mc 3u "So, are you hiding something from us for real?"
 kt "No, of course I'm not!"
 mc 3t "Kotonoha, please..."
 mc 5t "Just tell me. I can't help you if you don't tell me what's wrong!"
 kt "I said I'm okay!"
 mc 1t "..."
 kt "Do you really think I'm going through something?"
 mc "Well, ye--"
 kt "Why do you think that? Did I do anything wrong?"
 mc 1d "You're just... acting like you're depressed or something..."
 mc 5d "I'm drawing this conclusion from the poem you wrote."
 kt "What? My poem?"
 "[player] nods."
 kt "No... I just..."
 "I brush my hair from my face and sigh."
 kt "I'm okay, it's just that I needed to answer a call from someone."
 mc 2d "That late at night though?"
 kt "Yes."
 mc "Hm..."
 mc 3d "Well... okay then..."
 play sound school_ring
 window hide(None)
 window auto
 pause 2.0
 kt "I gotta go."
 mc 5t "Yeah, me too..."
 show mc2 at rhide
 hide mc2
 "Saying nothing else, [player] opens the door, heading out of the classroom."
 "I do the same after a couple minutes."
 scene black with wipeleft
 scene bg corridor with wipeleft
 "As I exit the classroom, Sayori, Mio and [player] are already gone."
 "Meanwhile, Natsuki waits for me while leaning against the wall."
 "As she sees me, she starts to speak."
 show natsuki 2m at t11 zorder 1
 n "Kotonoha, are you okay?"
 kt "Eh? Yeah, I'm alright. Why?"
 n 2h "I was listening in on your conversation with [player], and... well... [player] is actually right."
 kt "{i}*sigh*{/i}"
 kt "Yes, I said I'm okay."
 n 3n "Kotonoha... if there's anything that is troubling you, please let me know..."
 n 3u "I'm probably not the best person to help you with your problems, but if you ever need to talk to someone... I'm here."
 kt "...thanks Nat, but I'm okay."
 n "Well, If you say so..."
 show natsuki at thide
 hide natsuki
 "Natsuki and I return to our classroom."
 "Now that [persistent.playername_b] has gone... can I tell them that thing [persistent.playername_b] wouldn't allow me to say?"
 "Actually... It'd be better if I don't try it."
 scene bg class_day with dissolve_scene_full
 $ perspective = "mc"
 call perspective_window
 "It's been quite a long time since I talked to Kotonoha."
 "Am I wrong? Is she really okay and it's just me overthinking things?"
 "Natsuki also seems to be even more down than yesterday..."
 play music tsayori_c
 "This isn't right at all. I'm not giving it my best for all of them."
 "Come to think of it, Natsuki doesn't wanna talk to me at all... and I can't do anything if she's not willing to have a serious talk with me."
 "All I want is to settle everything and finally live a normal life."
 "--Give them all a normal life, free of pain and sadness."
 "Honestly, I'm starting to lose hope..."
 "Well, anyway, the teacher hasn't arrived yet. If he doesn't make it here soon, I'm gonna go with Sayori and get something to eat."
 "And Mio? I mean, she's been sticking around, and she follows me everywhere I go with Sayori, so I don't think I have a choice with her." 
 "If it weren't for the fact that she's been annoying, I would actually try to be her friend, but from what I can see, she just wants to take me away from Monika!"
 play sound closet_open
 "The classroom door opens, but instead of the teacher, the principal steps in."
 $ n_name = "Principal"
 n "Good afternoon dear students, I have an announcement to make."
 play sound closet_close
 "Closing the door, the principal goes to the front of the classroom."
 "Clearing his throat, he commences his speech."
 n "Unfortunately your professor will not be able to come today due to health issues. Since this is your last class, those who are not in a club can leave."
 n "On the other hand, those who are actually in a club, they must stay. With that, you can go. Have an excellent day and see you all tomorrow."
 "The principal then lets himself out--"
 mi "Hey! Just a moment, can we talk outside?"
 "He dismissively nods as Mio catches up to him."
 $ n_name = "Natsuki"
 $ s_name = "Sayori"
 "Sayori appears suddenly, taking her backpack as she asks me."
 show sayori 1a at t11 zorder 1
 s "[player], what do you want to do in the meantime?"
 mc "I don't know, why don't we get something to eat?"
 show sayori 4r at h11 zorder 1
 s "Oh, yeah! I'm terribly hungry right now!"
 mc "Then we shouldn't be waiting any longer, let's get out of here."
 "We were about to leave the classroom, but Mio cheerfully opens the door."
 show sayori 1a at t21 zorder 1
 show mio 4e at t22 zorder 1
 mi "Sayori! [player]! I have great news!"
 "Me and Sayori look at Mio quizzically."
 mi 5e "We can go to the library!"
 mc "Eh? Why?"
 mi 7x "So we can eat~"
 s 3m "Woah! The library is closed at this time, how did you even get permission?"
 mi 7l "It's better not to talk about it..."
 mc "Is the principal your father?"
 "Trying to ignore my question, Mio points to the corridor."
 mi 8l "S-so... come on!"
 show mio at rhide
 hide mio
 show sayori 3b at t11 zorder 1
 "Mio hastily walks right to the library."
 s 2c "Mio just evaded your question, didn't she?"
 mc "Yeah, she did."
 s 2h "Were you a meanie towards her?"
 mc "..."
 mc "Somewhat, yes."
 s 1g "[player]..."
 mi "{alpha=0.3}Come on guys!~{/alpha}"
 mc "{i}*sigh*{/i}"
 s 4g "Let's go, [player]. You should quit being mean to Mio... she's a nice person!"
 mc "Yeah... I bet she is..."
 "Sayori pulls my arm, dragging me along with her."
 scene black with wipeleft
 scene bg corridor with wipeleft
 "When we catch up to Mio, she starts talking."
 show mio 1a at t11 zorder 1
 mi "I have the key to the library, so we can get inside easily."
 mc "And how did you even get that key?"
 show mio 3k at t11 zorder 1
 "Ignoring my question yet again, Mio keeps walking."
 mi "Here."
 "Mio pulls out a silver key, she then uses it to unlock the door."
 scene black with wipeleft
 scene bg lib with wipeleft
 show mio 5e at t11 zorder 1
 mi "We're here~"
 mc "...hey, Mio?"
 mi "Hm?"
 mc "Can you tell me how you got that key?"
 mi 4k "I... I don't think it's that important."
 show mio 4k at t21 zorder 1
 show sayori 1x at t22 zorder 2 
 s "Come on Mio, we're friends! You can tell us whatever you want!"
 mi 5l "Oh, but... are we?"
 "Mio stares at me."
 mc "Yeah, I guess."
 mi 8l "W-well, then... make yourself at home!"
 show mio at thide
 hide mio
 show sayori at thide
 hide sayori
 "Mio drops her backpack down on the table as she sits down"
 "Me and Sayori do the same."
 "Mio proceeds to take three bento boxes out of her backpack."
 show mio 8a at t11 zorder 1
 mi "Here, this is for you!"
 "She hands one of those bento boxes to me, cheerfully smiling."
 mc "Um... well... okay, thank you."
 "I mean, it's just food. I can't say no to this; she spent time cooking this."
 "I gently open the box--"
 mc "Huh?"
 "There's a heart made of rice, covered with ketchup, and some chicken balls in each corner of this box."
 "Sayori sees it and quietly giggles."
 show mio 8a at t21 zorder 1
 show sayori 1q at t22 zorder 1
 s "{i}*Ehehe~*{/i}"
 mc "{i}*sigh*{/i}"
 mi 4y "I hope you like it, [player]!"
 mc "Yeah... thank you."
 "Mio flashes a smile at me, opening her bento box next."
 "With that being settled, we start digging in."
 stop music fadeout 2.0
 scene black with wipeleft
 scene bg lib with wipeleft
 "We talk every now and then while eating, making the library environment a little less boring."
 play music nday fadein 2.0
 "Sayori was the first one to finish, while Mio truly takes her time eating her food."
 show sayori 2x at t11 zorder 1
 s "Mmmmm~ That was delicious! Thanks for the bento, Mio!"
 show sayori 2a at t21 zorder 1
 show mio 1e at t22 zorder 2
 mi "You're welcome, Sayori~"
 mi "[player], did you enjoy yours?"
 mc "Yeah, it was good."
 s 2j "Just {i}good{/i}, [player]?"
 show mio 4c at t22 zorder 2
 "As Sayori says that, she hits my elbow."
 mc "Ack--!"
 "I kind of understand what that means, so..."
 mc "Well... I'm sorry for getting you so mad before coming to school."
 mc "I didn't mean to be rude to you, I swear I'll be nicer."
 mi 1a "Oh, it's okay! I can't stay mad at you~"
 mi 3e "So don't worry, but if it makes you feel any better... apology accepted~"
 "Mio giggles."
 mc "{i}*sigh*{/i}"
 mc "Alright, it's time to go to the club. Let's head out."
 s 2a "Yep~"
 mi 6g  "A-actually, I don't think I can go to today's meeting..."
 mc "Why is that?"
 mi 6l "I-I... gotta do something else..."
 mc "Meeting with that friend of yours is more important than your obligations to the club?"
 s 2b "A friend of yours? "
 extend 2c "Yeah, I have to agree with [player] on this one."
 mi 4l "N-no! I mean... something sorta... came up on the way, but I'll go with you guys to the club."
 mi "I have to tell that to Monika, don't I?"
 mc "So, your friend will join us even if you're gone?"
 show mio 5x at h22 zorder 2
 mi "Yes! She's an understanding person. In the meantime, I need to get some stuff done that I forgot about."
 mc "But you're basically in MY house, what do you have to get done that urgently?"
 mi 1m "Stuff..."
 show sayori 1p at h21 zorder 1
 s "[player]!"
 "Once again, Sayori hits my elbow."
 s 4j "These are questions you don't ask a girl!"
 mc "Ack--!"
 mc "{i}*sigh*{/i}"
 mc "Alright...let's head out."
 "I let Mio and Sayori step out first as we head to the clubroom."
 scene black with wipeleft
 scene bg corridor with wipeleft
 stop music fadeout 2.0
 show sayori 1c at t21 zorder 1
 s "Oh wow... it feels so lonely here..."
 show mio 4a at t22 zorder 2
 mi "Agreed..."
 show mio at thide
 hide mio
 show sayori at thide
 hide sayori
 "The sounds of our steps are the most audible thing, echoing with every single step we take."
 "This silence feels very relaxing to me, actually."
 "But I still have a lot of things to deal with today..."
 "First of all, How am I going to tell Monika that Mio is staying in my house for no reason?"
 "--then, trying to talk with Natsuki today..."
 "Not to mention this well-known friend of Mio coming today."
 "Why does everything have to be this difficult...?"
 show mio 2a at t11 zorder 1
 mi "Hey, [player]~"
 mc "Yeah?"
 mi 2e "I'm just gonna stay until Naomi arrives, then I'll leave. Is it okay with you?"
 mc "Ah... yeah, it's okay."
 mi 5x "Fine~"
 show mio at thide
 hide mio
 "Saying nothing else, the small orange-haired girl resumes her chat with Sayori."
 mc "Here we are."
 "Interrupting their conversation, Sayori and Mio stare at me, nodding as I tell them we've arrived."
 "Heh, I guess we're equals now."
 scene black with wipeleft
 scene bg club_day with wipeleft
 play music t3 fadein 2.0
 "The usual scene greets us: Yuri reading her book, Kotonoha and Monika talking with one another, and Natsuki--"
 mc "Huh?"
 $ m_name = "Monika"
 "Natsuki is sitting there with Kotonoha and Monika?"
 "Wow... that's actually really surprising.. I'm impressed, Natsuki!"
 "She's barely saying anything, though."
 "Whatever. Monika and Kotonoha greet us."
 show monika 5a at t11 zorder 1
 m "Welcome [player]~"
 show monika 1a at t21 zorder 1
 show kotonoha 4d at t22 zorder 2
 kt "Morning y'all!"
 mc "Hello girls. How are you doing?"
 m 1l "Well... we're okay."
 mc "Huh?"
 kt 4a2 "I-it's nothing, [player]."
 show monika 1m at t21 zorder 1
 "Sadly smiling, Monika looks away."
 show kotonoha at thide
 hide kotonoha
 show mio 1e at t22 zorder 2
 mi "Oh, hello! Um...I want to tell you something."
 m 3n "Hm? What is it?"
 mi "Well... I have some stuff to get done, so I'm gonna head out as soon as a friend of mine gets here."
 m "Did you bring a new member?"
 mi 3b "Oh... n-not really, she's just--"
 "Suddenly, the door opens, and Naomi steps into the room."
 show monika 2c at t31 zorder 1
 show mio 3c at t32 zorder 2
 sk "Hello?~ Is anybody here?"
 show naomi 1b at t33 zorder 3
 m 3n "Oh... Welcome to the Literature Club!"
 sk 3a "Tehehe, thank you! "
 extend 3c "Though I have to warn you, I'm not planning to become a member..."
 m 2n "Ahaha... I see..."
 sk 2b "Actually I came because of [player], he told me he has a friend that looks like me, and that's something I had to see for myself!"
 show mio at thide
 hide mio
 show sayori 1m at t32 zorder 2
 s 1m "Woah!"
 show naomi 2g at t33 zorder 3
 "Sayori hops in, staring at Naomi."
 show monika at thide
 hide monika
 show naomi 4e at t21 zorder 1
 show sayori 1m at t22 zorder 2
 sk "Oh... you must be Sayori, ain't ya?"
 s 2x "Yes I am!"
 sk 4e "Wow! You really {i}do{/i} look a lot like me!"
 s 2x "Yeah, you do!"
 "Naomi and Sayori giggle."
 sk 1a "I really wanted to meet ya', since [player] told me he has a friend lookin' like me!"
 s 2a "And your name is...?"
 sk 3l "I'm Naomi, nice to meet you!"
 show naomi 3l at t31 zorder 1
 show sayori 2a at t32 zorder 2
 show mio 1l at t33 zorder 3
 mi "A-ahaha... w-well, I got to go. Sorry to leave you all, but I need to get some things done!"
 sk 1d "Eh? But I came because of you!"
 mi 3l "I know, but... it was something unexpected, and I need to get it done as soon as possible."
 sk 4a "Oh okay, see ya then, Mio~"
 show mio at thide
 hide mio
 show naomi 1a at t21 zorder 1
 show sayori 2a at t22 zorder 2
 "Mio leaves the classroom, hastily closing the door behind her."
 stop music fadeout 2.0
 kt "..."
 show sayori at thide
 hide sayori
 show naomi 1d at t21 zorder 1
 show kotonoha 1e at t22 zorder 2
 "Now Kotonoha locks her eyes on Naomi, who is also looking at her in return."
 kt "You..."
 sk "Huh?"
 kt 4f "You... really are Naomi?"
 sk 2g "Um... yes? I just said so."
 sk "Why? Do I know ya'?"
 kt 5s "Well... a-actually... n-no..."
 sk 1g "Odd. I kinda remember your face from somewhere else, though I'm not totally sure..."
 kt 5a2 "Yeah, I... I've been getting that a lot lately..."
 "The environment feels really tense... does Kotonoha know Naomi or something?"
 sk 2a "Your dialect is similar to mine... you from the Kansai region as well?"
 kt 2a2 "Yeah, I-I'm from Osaka..."
 sk "Osaka?"
 extend 1e " Hey, that's quite close to Kobe! I'm from there, just so you know."
 kt 3a2 "Oh really? well... it's nice to meet you, {i}Naomi{/i}."
 sk 3b "Same!"
 "Monika takes note of the dense air surrounding us, so she decides to speak up."
 show kotonoha 4a2 at t32 zorder 1
 show naomi 1a at t31 zorder 2
 show monika 2n at t33 zorder 3
 m "Alright... I think it's almost time to share poems."
 kt 6a2 "Heheh... yeah, let's get started."
 sk 1a "Well, I can stay since I have nothin' else to do at home but homework, so yeah!"
 show kotonoha at thide
 hide kotonoha
 show naomi at thide
 hide naomi
 show monika 2m at t22 zorder 1
 show yuri 1e at t21 zorder 2
 "Yuri was peeking while reading her book, and as I notice that--"
 y 2p "Oh! I-I'm sorry [player], I just...!"
 mc "You just wanted to say you're ready, so don't worry."
 y 3q "Y-yes that's right! I'm ready!"
 show yuri at thide
 hide yuri
 show monika 1q at t11 zorder 1
 "Yuri takes her poem out from her backpack."
 "Kotonoha, still looking at Naomi, goes back to her desk to retrieve her poem."
 "Monika calls for the group."
 m 2n "Okay everyone~ take your poems out, we'll start sharing them soon."
 show monika at thide
 hide monika
 "Monika goes back to the teacher's desk, taking her poem out."
 "Meanwhile, Naomi just sits in the desk closest to the front."
 "Well... here we go..."
 call poemresponse_start_d3




label act1_ch2_d3_p2:
 scene black with wipeleft
 scene bg club_day with wipeleft
 play music t3 fadein 2.0
 "Phew... another great day!"
 "Well, kind of..."
 "I still need to see what Natsuki wants to talk to me about..."
 "Whatever. Kotonoha and Monika are cleaning up while Sayori and Naomi are talking."
 "Yuri as usual is reading her book. She wanted to talk with Naomi too, but... well, her shyness is preventing her from doing so."
 "I'm just thinking about stuff. What is that thing Mio needed to get done that urgently?"
 "She's staying at my place after all."
 "She won't be for long, though."
 "I'm gonna ask Sayori to invite her to her house."
 "I walk towards Sayori, who is talking to Naomi. I don't want to interrupt, but it'd be a good idea if I talk to her about this now."
 mc "Hey Sayori."
 show sayori 1a at t21 zorder 1
 show naomi 1a at t22 zorder 2
 s "Oh, hello [player]!"
 sk 2a "Heyo~"
 mc "Hello, Naomi."
 s 2x "What is it? Do you need something?"
 mc "Yeah, actually I want to talk to you."
 "I lean to Sayori."
 show layer master:
  zoom 1.0 xalign 0.15 yalign 0 subpixel True
  linear 2 zoom 2.0 yalign 0.15
 pause 2.8
 mc "Look, Mio has invited herself to my place and she doesn't want to leave. Could she stay with you?"
 s 2b "Um... are you gonna tell her?"
 mc "Yeah, I got that covered."
 s 4b "Hm... I don't know... I'm gonna think about it and I'll tell you sometime today."
 mc "Alright, just don't take too long. I don't think I could stand her staying with me."
 s 4l "Ehehe..."
 show layer master
 sk 2p "Hey [player]~"
 mc "Yeah?"
 sk 4p "You ain't a kind person... Mio is the cutest and sweetest person I've ever known!"
 mc "Yeah, I bet she is."
 show naomi 4p at h22 zorder 2
 sk "Huh?!"
 s "Ehehe... l-let's calm down you guys!"
 "Sayori holds Naomi, and I just stand there."
 sk 1q "Yeah... you're safe, [player]... for now."
 "Naomi smiles as she stares at me."
 sk 3a "Well y'all, it's time for me to leave! I had so much fun readin' your poems! You'll probably get to see me stop by every now and then~"
 show sayori 1a at t31 zorder 1
 show naomi 3a at t32 zorder 2
 show monika 2l at t33 zorder 3
 m "O-oh, Ahaha..."
 m "Well, I'm glad you enjoyed our Literature Club. It's a shame you can't join though..."
 sk 2s "Yeah, I love my club too much to leave."
 show sayori at thide
 hide sayori
 show monika at thide
 hide monika
 show naomi 1g at t21 zorder 1
 show kotonoha 1g at t22 zorder 1
 kt "W-wait, Naomi!"
 "Kotonoha shouts Naomi's name and hastily walks to the door."
 sk 3f "Eh? What?"
 kt 4v1 "C-can I have your ph-phone number?"
 sk 1f "Huh? O-oh... well... sure?"
 "Kotonoha's eyes light up as she hears Naomi's answer and takes her phone out."
 show naomi 1a at t21 zorder 1
 show kotonoha 1a2 at t22 zorder 1
 "Naomi gave Kotonoha her cell phone number. They smile to each other after."
 sk 3l "Well, I'm gonna head out. Later everyone!"
 "With that, Naomi leaves the classroom."
 show naomi at lhide
 hide naomi
 show kotonoha 4p2 at t22 zorder 1
 kt "{alpha=0.5}I finally found you...{/alpha}"
 show sayori 1c at t21 zorder 2
 s "Oh? Kotonoha?"
 kt 4w2 "Ah... nevermind..."
 show kotonoha at thide
 hide kotonoha
 show sayori at rhide
 hide sayori
 "Saying nothing else, Kotonoha goes back to sweep while Sayori returns to the closet."
 "Did she say anything? Does she actually know Naomi?"
 "Yeah, she probably does..."
 show natsuki 1s at t11 zorder 1
 n "[player]."
 mc "Yeah?"
 n 2n "Can we talk outside?"
 mc "Eh... sure, let's go."
 "Natsuki finally comes to me, and it seems it's time." 
 "Let's see what Natsuki wants to say."
 "I open the door, letting Natsuki step out first."
 scene black with wipeleft
 scene bg corridor with wipeleft
 stop music fadeout 2.0
 "We both leave the classroom and Natsuki grabs my sleeve."
 n "L-let's walk around..."
 mc "Okay. I'll follow you."
 "Natsuki nods and we start to walk to the courtyard."
 scene black with wipeleft
 scene bg yard2 with wipeleft
 "Once there, Natsuki stares at the ground as she stops walking."
 show natsuki 1m at t11 zorder 1
 n "You know something? I've been thinking that if I stopped acting annoying, maybe you'll change your mind and get Monika out of here..."
 play music late fadein 2.0
 n "But it seems you won't change your mind, will you?"
 mc "No, I'm sorry Natsuki... I won't."
 mc "But, look..."
 n 2i "Hm?"
 "Natsuki stares intently at me."
 mc "This is not just for Monika. As I said to her... I want you all to be happy."
 mc "And if you want me to understand you, trust me, I'll try."
 show natsuki 2n at t11 zorder 1
 mc "--but you also have to understand me, Natsuki. This is for you, too."
 mc "I... really do consider you a friend of mine."
 n "[player]..."
 "I take my hand to my hair, and look up to see the sky."
 scene bg sky with Dissolve(1.0)
 mc "I know I sound repetitive, but I'm gonna say this again: no one hates you, Natsuki."
 mc "We're all worried for your well-being."
 mc "There's no reason for us to hate you at all."
 n "..."
 n "Does Monika really feel bad?"
 mc "You tell me."
 n "Well..."
 n "Yesterday she told us how she feels..."
 mc "And?"
 n "It seems she's feeling just as bad as she says..."
 mc "Yeah."
 mc "So, stop saying that I hate you or that this is just for Monika. I want to create a story for you all."
 n "I think I see that now..."
 window hide(None)
 window auto
 pause 2.0
 "Natsuki pulls my sleeve, still looking away."
 n "Hey, [player]?"
 mc "Yeah?"
 n "Can I..."
 n "Umm..."
 mc "What?"
 "Natsuki hesitates a little bit as she asks, I then stare at her."
 n "Can I... h-hug you?"
 mc "Oh... um... sure."
 scene bg yard2 with Dissolve(2)
 "As I meet her face, Natsuki is blushing a deep shade of red."
 show natsuki 2h at t11 zorder 1
 n "J-just don't look! C-close your eyes!"
 mc "Heh... okay then~"
 "I close my eyes so Natsuki won't be more embarrassed."
 "She actually looks really cute this way."
 scene black with dissolve_scene_full
 n "W-well... Um..."
 "Natsuki shyly puts her arms around me, tightening her hug."
 "Wow... so that's it? This is what Natsuki was feeling like?"
 "I didn't expect her to allow herself to do this."
 "After all, she's also feeling bad too."
 n "A-are you gonna hug me back?"
 mc "Oh, yeah..."
 "I put my arms around Natsuki."
 "Are these her true colors?"
 "I have to accept that Natsuki is actually really cute."
 "But now... what will happen between her and Monika then? Will Natsuki apologize to her as well?"
 "Since she's apologized to me, it'd make sense..."
 "I'm also worried about that thing Monika said about her father... I wonder what she's going through with him?"
 "Natsuki rubs her face in my chest as she lets go of me."
 scene bg yard2 with dissolve_scene_full
 show natsuki 2h at t11 zorder 1
 n "[player]..."
 mc "Yeah?"
 n 2q "Can we go inside now? I... want to talk to Monika."
 mc "Okay, let's go."
 "I pat Natsuki's back, and we make our way back to the clubroom."
 scene black with wipeleft
 scene bg corridor with wipeleft
 scene black with wipeleft
 scene bg club_day with wipeleft
 "Everyone except Monika is sitting at their desks, waiting for her to dismiss them."
 "I look around, and the first one I see is Yuri. I walk to her, Natsuki following me."
 mc "Yuri?"
 show yuri 3e at t11 zorder 1
 y "Hm? What's the matter, [player]?"
 mc "Where's Monika?"
 y "Ah..."
 extend 2f "She's inside the closet, wiping Natsuki's manga shelf."
 mc "Is anyone else with her?"
 y 2h "Um... no."
 mc "Good. Thanks, Yuri."
 show yuri at thide
 hide yuri
 "Natsuki stops me on our way to the closet."
 show natsuki 3h at t11 zorder 1
 n "[player], just wait once we're there... I'll talk to her."
 mc "Are you sure?"
 n 4m "Not really, but I already said I wanted to talk to her. I can't hold this back for much longer."
 mc "I see... Well, if that's what you want then it's okay."
 "Natsuki nods and we go to the closet."
 scene black with wipeleft
 scene bg closet with wipeleft
 "Once there, Natsuki asks me to wait for her."
 mc "You can always do this later if you're not ready yet."
 show natsuki 2s at t11 zorder 1
 n "If I don't do this now, it'll probably be too late next time... like Mio said..."
 mc "{i}*sigh*{/i}"
 show natsuki at thide
 hide monika
 "Is she taking Mio's comments seriously?"
 "Well, I mean, it's not like she said anything wrong, but..."
 "Natsuki doesn't like Mio, and if she's taking her advice, then... it really makes her seem thoughtful."
 "I really wouldn't have expected Mio to help with this. She really does care for Natsuki, doesn't she?"
 "However, this is not the end of my goal."
 "Our goal."
 "Natsuki slowly walks to the closet, talking to Monika."
 show natsuki 1n at t11 zorder 1
 n "Hey, Monika?"
 show natsuki 1n at t21 zorder 1
 show monika 1c at t22 zorder 2
 m "Natsuki? What is it?"
 n 2q "Um... I... I want to..."
 m 2c "You want to...?"
 n 12g "I..."
 "Monika stares at me. She probably assumes that I might know something."
 "I shrug, and Monika steps out of the closet."
 m 3e "Here, follow me."
 "Natsuki looks down. I rest my back against the wall."
 m 6a "I know what are you trying to do Nat... I swear I want to do something to help you, but I can't..."
 stop music fadeout 2.0
 m 6b "I'm as bad as you are right now... A-haha..."
 n "Monika... I-I just wanted to say..."
 n "I-I thought [player] wasn't being honest with me, but..."
 n "I just want to say that..."
 "Monika starts to tear up, but Natsuki is still having problems trying to speak."
 "She then walks to Natsuki, holding her in an embrace."
 scene m_n_cg_1 with dissolve_scene_full
 play music lament fadein 2.0
 call dust
 m "Natsuki... I know what you're trying to say..."
 m "And I know it's difficult for you, don't worry, I still understand you."
 m "It's okay now, Nat. You won't be alone anymore."
 n "I...!"
 scene m_n_cg_2 with dissolve_cg
 call dust
 n "I'm sorry for everything I said to you!"
 n "I really didn't want you to feel this bad at all this week... I just wanted [player] to change his mind and get rid of you..."
 n "I actually really enjoy my time in this club!"
 "Time has stopped. Everyone is staring at Monika and Natsuki, who are now both crying."
 "Natsuki is letting her words out without hesitation, giving the whole clubroom a different environment."
 "But even so, she doesn't hug Monika back."
 n "Sometimes I just want it to be like before..."
 m "Well... that's why [player] brought us back..."
 m "I still feel kind of empty, but as a friend of mine said: this is the reality we live in."
 m "And if [player] really wants to give us a normal life, then we just have to try and let ourselves be happy."
 n "Do you..."
 extend "Do you really promise everything is gonna be different from now on?"
 m "Yes."
 m "Now you don't have to hold yourself back. We are here..."
 m "--I am here... to help you."
 scene m_n_cg_3_a with Dissolve(2.8)
 call dust
 "Hesitating, Natsuki hugs Monika in return."
 n "Okay... I trust you, Monika."
 n "I'm really sorry for everything I said to you..."
 m "I'm really sorry for making you go through that hell with your father..."
 m "And trust me, I'll help you with that, because you're a really good friend of mine and I don't want anything bad to happen to you."
 n "..."
 n "W-well... t-thank you, Monika..."
 n "And everything is gonna be different from now on... for this club."
 m "So it'll be!"
 m "Ahaha... now, don't cry!"
 "Monika wipes Natsuki's tears from her face with her sleeve, but Monika is still crying."
 scene m_n_cg_3_b with dissolve_cg
 call dust
 "Monika and Natsuki then remain silent for a while, hugging each other."
 n "Hey, Monika?"
 m "Yeah?"
 n "It's... nice to be back to 'reality'..."
 m "Yeah, you're right."
 n "So... we're okay, now?"
 m "If you want to be okay, then yeah, we're okay."
 n "Do you really promise to change for the better?"
 m "Yes. I said it once already, and I'll keep that promise."
 n "Okay..."
 "Natsuki slowly lets go of Monika, she still has tears on her face."
 stop music fadeout 2.0
 scene bg club_day with dissolve_scene_full
 show natsuki 1m at t11 zorder 1
 n "Eh? Where is everyone?"
 show natsuki 1m at t21 zorder 1
 show monika 2l at t22 zorder 1
 m "Ahaha... I-I bet they left already..."
 play music t8 fadein 2.0
 m "Oh... you're still here, [player]."
 mc "Yeah. I saw it all."
 mc "I'm glad you two finally made up."
 n 2q "Geez, I-it's not like--"
 n 3t "Um... sorry. I'm glad to be back."
 m 3n "Ahaha..."
 play sound closet_open
 "As Monika laughs, the door opens and everyone comes back into the clubroom."
 show natsuki 3t at t31 zorder 1
 show monika 3n at t32 zorder 2
 show sayori 1x at t33 zorder 3
 $ s_name = "Everyone"
 s "Hello!~"
 $ s_name = "Sayori"
 m 2e "Oh... I thought you guys had left already..."
 show natsuki 3t at t41 zorder 1
 show monika 2e at t42 zorder 2
 show sayori 1x at t43 zorder 3
 show kotonoha 5a at t44 zorder 4
 kt "Not really, we went outside so you girls can talk."
 mc "I didn't even see you leave."
 show sayori 4q at h43 zorder 4
 s "We're like ninjas!~"
 "Monika and Natsuki giggle."
 show natsuki 3t at t51 zorder 1
 show monika 2e at t52 zorder 2
 show sayori 4q at t53 zorder 3
 show kotonoha 5a at t54 zorder 4
 show yuri 1a at t55 zorder 5
 y "So... what now?"
 m "Now...you girls can go take a seat, I'm gonna call it a day soon~"
 $ m_name = "Everyone"
 m "Alright!"
 $ m_name = "Monika"
 "With that, everyone goes to sit at their desks."
 "I do the same myself."
 scene black with wipeleft
 scene bg club_day with wipeleft
 "Monika and the girls have spent the rest of the meeting talking. Natsuki has been getting involved in the conversation too!"
 "I have as well, saying something every now and then. The environment doesn't feel so unsettling anymore."
 "Hopefully we have overcome this big obstacle... now it's time to give them the happy story they all deserve!"
 "Monika stands up from her chair calling for the group."
 show monika 2b at t11 zorder 1
 m "Well, everyone...I think that's it for today! See you all tomorrow~"
 show monika 2b at t21 zorder 1
 show kotonoha 4d at t22 zorder 2
 kt "Nice! Are we writing poems for tomorrow?"
 show monika 2b at t31 zorder 1
 show kotonoha 4d at t32 zorder 2
 show yuri 3l at t33 zorder 3
 y "Actually, I'd like to put that on hold. It's becoming rather boring to be honest."
 show monika 2b at t41 zorder 1
 show kotonoha 4d at t42 zorder 2
 show yuri 3l at t43 zorder 3
 show sayori 1c at t44 zorder 4
 s "Yeah, I agree with Yuri."
 m 3l "Ahaha... then let's put the poem assignments on hold, we should find something else to do during the club meeting!"
 kt 4d "{i}*phew*{/i}"
 kt 5p2 "Finally! I don't think I could stand doing this for too much longer..."
 y 2b "Well, actually I thought your poems weren't that bad, Kotonoha."
 kt 5a2 "Hehe... t-thank you!"
 y 2c "Mhm~ You're welcome!"
 s 1a "Sooo... back to normal activities?"
 stop music fadeout 2.0
 m 5a "Yeah, Sayori. But..."
 scene black with dissolve_scene_full
 m "This time it'll be better than 'normal activities.'"
 jump act2_ch1

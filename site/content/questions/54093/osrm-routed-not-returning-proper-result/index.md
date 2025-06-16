+++
type = "question"
title = "osrm-routed not returning proper result"
description = '''Hi, I installed OSRM back-end on my ubuntu server. I downloaded france-latest.osm.pbf from GEOFABRIK and I filtered/extracted/contracted it to generate a file containing main highways as follows: ./osmconvert france-latest.osm.pbf -o=france-latest.o5m ./osmfilter france-latest.o5m --keep=&quot;highway=mo...'''
date = "2017-01-17T08:12:00Z"
lastmod = "2017-01-18T09:21:00Z"
weight = 54093
keywords = [ "osrm-routed_filter" ]
aliases = [ "/questions/54093" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [osrm-routed not returning proper result](/questions/54093/osrm-routed-not-returning-proper-result)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54093-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I installed OSRM back-end on my ubuntu server. I downloaded france-latest.osm.pbf from GEOFABRIK and I filtered/extracted/contracted it to generate a file containing main highways as follows:</p>
<p>./osmconvert france-latest.osm.pbf -o=france-latest.o5m</p>
<p>./osmfilter france-latest.o5m --keep="highway=motorway =motorway_link =trunk =trunk_link =primary =primary_link =secondary =secondary_link" -o=france.mtps.osm</p>
<p>./osrm-extract -p profile.lua france.mtps.osm</p>
<p>./osrm-contract france.mtps.osrm</p>
<p>And finally I started the back-end osrm-routed as follows:</p>
<p>./osrm-routed ../osrm_files_france.mtps/france.mtps.osrm</p>
<hr />
<p>The backend starts and responds but sometimes it return results that are different from what I would expect or from what the demo server at router.project-osrm.org returns. Here is an example where I want to get the distance between 2 GPS coordinates located on a motorway. The correct distance is 15.1 km, which is consistent with the distance returned by the demo server (15087.7 meters). However my server returns a different route with a distance of 17488.1 meters. I do not understand why I get a different route which makes little sense since the 2 points are located on a motorway same lane. Can anyone help ?</p>
<p>Find below the output returned by both my server and the demo server.</p>
<p>DEMO SERVER QUERY:</p>
<p><a href="https://router.project-osrm.org/route/v1/driving/2.865504,42.464852;2.844055,42.573679?steps=true&amp;continue_straight=true&amp;overview=false">https://router.project-osrm.org/route/v1/driving/2.865504,42.464852;2.844055,42.573679?steps=true&amp;continue_straight=true&amp;overview=false</a></p>
<p>DEMO SERVER RESPONSE:</p>
<p>{"code":"Ok","routes":[{"legs":[{"steps":[{"intersections":[{"out":0,"entry":[true],"bearings":[350],"location":[2.865512,42.464853]}],"geometry":"i|dbGmtnPqFx<a href="https://help.openstreetmap.org/users/136/acrosscanadatrails">@a</a>BV","mode":"driving","duration":7.9,"maneuver":{"bearing_after":350,"location":[2.865512,42.464853],"bearing_before":0,"type":"depart"},"ref":"AP-7","distance":192,"name":"La Catalane"},{"intersections":[{"out":1,"location":[2.865101,42.466552],"bearings":[165,345],"entry":[false,true],"in":0},{"out":2,"location":[2.862913,42.471981],"bearings":[0,150,330],"entry":[true,false,true],"in":1},{"out":1,"location":[2.862552,42.472339],"bearings":[143,318,328,335],"entry":[false,true,true,true],"in":0},{"out":1,"location":[2.861841,42.472917],"bearings":[138,311,318],"entry":[false,true,true],"in":0},{"out":3,"location":[2.858814,42.474743],"bearings":[118,124,127,303],"entry":[false,false,false,true],"in":2},{"out":2,"location":[2.857274,42.475428],"bearings":[105,120,285],"entry":[false,false,true],"in":1},{"out":2,"location":[2.852842,42.476509],"bearings":[106,107,291],"entry":[false,false,true],"in":0},{"out":0,"location":[2.819492,42.523429],"bearings":[10,14,186],"entry":[true,true,false],"in":2},{"out":0,"location":[2.82549,42.531479],"bearings":[49,224,227],"entry":[true,false,false],"in":2},{"out":0,"location":[2.843981,42.572556],"bearings":[4,5,182],"entry":[true,true,false],"in":2}],"geometry":"}febG{qnPmBVwBZ{Dl@cDh@{A^{Ad@{@<a href="https://help.openstreetmap.org/users/136/acrosscanadatrails"><code>@a</code></a><code>Ad@{B|As@j</code><a href="https://help.openstreetmap.org/users/269/qwartz"><code>@Q</code></a><code>PgAfAsBlCwDzGsD</code>IgArCaA~CUlAg@dCq@lEgBrMg@jCc@dBs@|Bs@hBq@|AwB~D{BvDmBrCqAbB}AdByAjAsA<code>AsAt</code><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@i</code></a></a><code>Bz</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>Cv@cCr@yBf</code><a href="https://help.openstreetmap.org/users/136/acrosscanadatrails"><code>@a</code></a><code>BZkAZ{@ZaAd</code><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@i</code></a></a><code>At</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>At@eAdAcAjAmA~A{AxByAzBcCfEeEhImGnLwCpGmAtCyAbDiBrDkCfEkCdE}AtCmAxC_A|CaAbEuAjHw@</code>DiAvDyAtD}AzCcAdB{AnBsA~As@r@cA|<a href="https://help.openstreetmap.org/users/4612/oapcyclist">@oA</a><code>AeAx@[PqAn@cA</code><a href="https://help.openstreetmap.org/users/521/ua-land">@uA</a>^kB<a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>BX_CTeBLeCBaFKcJYeL]}Oe@oJ]yDUoESkJ]mHGaFK}EWgBQy@KgAI_@CcC_@oBe</code><a href="https://help.openstreetmap.org/users/136/acrosscanadatrails"><code>@a</code></a><code>A[{</code><a href="https://help.openstreetmap.org/users/31/willi2006"><code>@W</code></a><code>{Ai@mAk@w@s@eCeCeBeAuA}</code><a href="https://help.openstreetmap.org/users/1211/gbee"></a><a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><code>B</code></a><code>}</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>CgAuAcAqAqAeDoE}BuDqA_CqAiCmAkCyAuDkBkF}CmJyCyJgIuWiCmHmEaLwCiGeCuE}BsD_B_CiDaEiBmByBoB{BeB}</code><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@i</code></a></a><code>@}AaAcB_AaBw@oBw@yDiAcDs@kC_</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>CSwDMaC?[?cDNqBLwBXgDn@cElAcCz@oH</code>DkK|EiEdBiEzAgFvAiFlAwDp<a href="https://help.openstreetmap.org/users/136/acrosscanadatrails">@a</a>D`@sCZmDXwDRmDLcEHaEBgIC_CE_FS","mode":"driving","duration":607.1,"maneuver":{"bearing_after":350,"type":"new name","modifier":"straight","bearing_before":350,"location":[2.865101,42.466552]},"ref":"A 9","distance":14895.8,"name":"La Catalane"},{"intersections":[{"in":0,"entry":[true],"bearings":[184],"location":[2.844077,42.573677]}],"geometry":"odzbGonjP","mode":"driving","duration":0,"maneuver":{"bearing_after":0,"location":[2.844077,42.573677],"bearing_before":4,"type":"arrive"},"ref":"A 9","distance":0,"name":"La Catalane"}],"summary":"La Catalane, La Catalane","duration":615,"distance":15087.7}],"duration":615,"distance":15087.7}],"waypoints":[{"hint":"FGY5hP<strong><em>38ozcIAEgAAAEoAAAAAAAAAFwAAAI6rkwJtugAAaLkrAFX2hwJguSsAVPaHAgAAAQHnB7e-","name":"La Catalane","location":[2.865512,42.464853]},{"hint":"hkqVg</em></strong>_3-YLQwAKwAAAEMAAAAAAAAAJwEAABkiJAJtugAArWUrAG2fiQKXZSsAb5-JAgAAAQHnB7e-","name":"La Catalane","location":[2.844077,42.573677]}]}</p>
<hr />
<p>MY SERVER QUERY:</p>
<p><a href="http://hp-ubuntu:5000/route/v1/driving/2.865504,42.464852;2.844055,42.573679?steps=true&amp;continue_straight=true&amp;overview=false">http://hp-ubuntu:5000/route/v1/driving/2.865504,42.464852;2.844055,42.573679?steps=true&amp;continue_straight=true&amp;overview=false</a></p>
<p>MY SERVER RESPONSE:</p>
<p>{"code":"Ok","routes":[{"legs":[{"steps":[{"intersections":[{"out":0,"entry":[true],"bearings":[1],"location":[2.863181,42.464999]},{"out":0,"location":[2.863187,42.465234],"bearings":[0,180],"entry":[true,false],"in":1},{"out":1,"location":[2.862516,42.466707],"bearings":[150,345],"entry":[false,true],"in":0},{"out":0,"location":[2.857643,42.470223],"bearings":[0,180],"entry":[true,false],"in":1}],"maneuver":{"type":"depart","modifier":"right","location":[2.863181,42.464999],"bearing_after":1,"bearing_before":0},"mode":"driving","distance":6375.9,"duration":284.7,"geometry":"g}dbG{enPm@Aa@?Q?E?S<a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon">@g</a></a>@JWJc@PQNMJq@h@c@RcA^e@\<em><a href="https://help.openstreetmap.org/users/39/floris">@f</a>@e@|@]^{<a href="https://help.openstreetmap.org/users/121/victor-bielawski">@v</a>@k@h@]|<a href="https://help.openstreetmap.org/users/269/qwartz">@Q</a>|<a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph">@I</a></a>~@CfAEdBGp@Or@[x<a href="https://help.openstreetmap.org/users/136/acrosscanadatrails">@a</a>@r<a href="https://help.openstreetmap.org/users/269/qwartz">@q</a>@n@y@<code>@{@TeABsDBMAMCc@Ui</code><a href="https://help.openstreetmap.org/users/31/willi2006"><code>@W</code></a><code>[Gc</code><a href="https://help.openstreetmap.org/users/15/bass"><code>@B</code></a><code>ULQN]XqB</code>B</em><a href="https://help.openstreetmap.org/users/15/bass">@b</a><a href="https://help.openstreetmap.org/users/31/willi2006">@W</a>^Uj@Kj@Cd@AdA@|ADp@Vz@^p@^\b@RnAPh@T\^Th@Hv@?t<a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph">@I</a></a>d@Sd@c@<a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><code>@Nc@?]Iw@[k@Sk@De@P_@XSVOd@M</code>AWbIIdAK|<a href="https://help.openstreetmap.org/users/1283/olathoen">@OlA</a>?n@F~@DlAAj<a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph">@I</a></a>^M\a<a href="https://help.openstreetmap.org/users/15/bass">@b</a>@k@\<em>Bp@oCbAo@Ve@<a href="https://help.openstreetmap.org/users/269/qwartz"><code>@q</code></a><code>@x@e@Zo@Tc@</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@I</code></a></a><code>c@Ua</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>@]Sk</code><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@I</code></a></a><code>g@Fa@TYb@Uj</code><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@I</code></a></a><code>v@EzCElAQbA]</code>AqAvCg@z@c@Tg@Dc@EsAS</em>@<a href="https://help.openstreetmap.org/users/136/acrosscanadatrails">@a</a>@P_@^q@z@sAzAkC~BwFhFMTMZIXAXAj@@zBCxBU|BYtBK^O\o@l<a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon">@g</a></a>@L[AWGqAq@cAm<a href="https://help.openstreetmap.org/users/136/acrosscanadatrails">@a</a>Ao<a href="https://help.openstreetmap.org/users/521/ua-land">@uA</a>i<a href="https://help.openstreetmap.org/users/269/qwartz">@q</a>@Om@MYC}<a href="https://help.openstreetmap.org/users/15/bass">@B</a>}@VcAb<a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph">@i</a></a>Ax@m@r@}<a href="https://help.openstreetmap.org/users/121/victor-bielawski">@v</a>A}@rB_BjDINkBbEgBrDeAdBs<a href="https://help.openstreetmap.org/users/121/victor-bielawski">@v</a>Au@zAc@jA{@dBcAlBkAlBeAtAwAjBeB|Bu@~@{@hBc<a href="https://help.openstreetmap.org/users/15/bass">@b</a>Be<a href="https://help.openstreetmap.org/users/39/floris">@f</a>CgAbG]dBk@jAoA<code>CmBxCq@r@eBrAmAz@}Ap</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>@Jw@HaAJm@C}AWs</code><a href="https://help.openstreetmap.org/users/269/qwartz"><code>@Q</code></a><code>a@S","name":"Avenue de France - Avinguda Catalunya","ref":"D 900"},{"intersections":[{"out":1,"location":[2.820866,42.500462],"bearings":[15,30,195],"entry":[true,true,false],"in":2},{"out":0,"location":[2.82127,42.500976],"bearings":[45,210,240],"entry":[true,false,false],"in":1}],"maneuver":{"type":"fork","modifier":"slight right","location":[2.820866,42.500462],"bearing_after":27,"bearing_before":22},"mode":"driving","distance":1779.5,"duration":90.1,"geometry":"{zkbGm}ePgAo</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>@m@o@m</code><a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><code>Aq</code><a href="https://help.openstreetmap.org/users/521/ua-land"><code>@uA</code></a><code>eAaCQYg@m@sB{A_BeAm</code><a href="https://help.openstreetmap.org/users/269/qwartz"><code>@Q</code></a><code>o@MaACg@Hk@VyAhAuAh</code><a href="https://help.openstreetmap.org/users/136/acrosscanadatrails"><code>@a</code></a><code>ADm@GmAWu</code><a href="https://help.openstreetmap.org/users/31/willi2006"><code>@W</code></a><code>u@c</code><a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><code>@]q@e</code><a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><code>A_</code><a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><code>@]k@UCCe</code><a href="https://help.openstreetmap.org/users/269/qwartz"><code>@Q</code></a><code>_@Ya</code><a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><code>@}BuEe</code><a href="https://help.openstreetmap.org/users/136/acrosscanadatrails"><code>@a</code></a><code>@EEEEaA{</code><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@I</code></a></a><code>GgAcAiD}Cw@s@o</code><a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><code>@o</code><a href="https://help.openstreetmap.org/users/31/willi2006"><code>@W</code></a><code>gDuAgAc</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>@SUS{@]g@U","name":"","ref":"D 900"},{"intersections":[{"out":0,"location":[2.830111,42.51384],"bearings":[90,195,300],"entry":[true,false,false],"in":1},{"out":0,"location":[2.83021,42.514115],"bearings":[15,120,270],"entry":[true,false,true],"in":1},{"out":1,"location":[2.831084,42.515735],"bearings":[15,30,210],"entry":[false,true,false],"in":2},{"out":0,"location":[2.831206,42.515916],"bearings":[25,36,207],"entry":[true,true,false],"in":2},{"out":1,"location":[2.831861,42.516932],"bearings":[15,30,195],"entry":[true,true,false],"in":2},{"out":2,"location":[2.832601,42.516816],"bearings":[89,97,282],"entry":[false,false,true],"in":0},{"out":1,"location":[2.831113,42.51715],"bearings":[105,285,300],"entry":[false,true,true],"in":0}],"maneuver":{"exit":1,"type":"roundabout","modifier":"right","location":[2.830111,42.51384],"bearing_after":94,"bearing_before":22},"mode":"driving","distance":926.6,"duration":61.4,"geometry":"onnbGewgP?KAKCKGEECGAG@EBEDCFCFmAi@cFyBQIc@Y_@SeAw@cAg</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>@Ma@SGEa</code><a href="https://help.openstreetmap.org/users/136/acrosscanadatrails"><code>@a</code></a><code>@Oa@Ge@</code><a href="https://help.openstreetmap.org/users/54/glennon"></a><a href="https://help.openstreetmap.org/users/54/glennon"><code>@g</code></a></a><code>@Hm@J_@R[PCN?TLN\\D\\?z@KtAc@pCQ</code>AQ<code>AeApFc@rA","name":"","ref":"D 900"},{"intersections":[{"out":2,"location":[2.829154,42.517766],"bearings":[120,135,315],"entry":[false,true,true],"in":0}],"maneuver":{"type":"new name","modifier":"slight right","location":[2.829154,42.517766],"bearing_after":313,"bearing_before":300},"mode":"driving","distance":678.3,"duration":30.5,"geometry":"agobGeqgPEHQXyHlK_@l</code><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@I</code></a></a><code>RMXW|</code><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@I</code></a></a><a href="https://help.openstreetmap.org/users/2905/kfjm">@Kf</a>@MfACt@Cn@?fCApBE|<a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph">@I</a></a>b@K\Qd@S^ORYPY@","name":"","ref":"D 900"},{"intersections":[{"out":0,"location":[2.822531,42.520756],"bearings":[45,180,240],"entry":[true,false,false],"in":1},{"out":2,"location":[2.821924,42.520958],"bearings":[15,165,240],"entry":[false,true,true],"in":0}],"maneuver":{"exit":1,"type":"roundabout","modifier":"right","location":[2.822531,42.520756],"bearing_after":43,"bearing_before":358},"mode":"driving","distance":512.5,"duration":29.4,"geometry":"wyobGygfPIMUK[BQJEFIZAZDXNXDDPFH@DPZn@Tr@H<a href="https://help.openstreetmap.org/users/4745/dzmaricelgomez"><code>@Dz</code></a><code>@C|</code><a href="https://help.openstreetmap.org/users/1303/craig"><code>@Cr</code></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@I</code></a></a><code>x@Mz@Mt@c@</code>C]lB[fBO<a href="https://help.openstreetmap.org/users/712/ajxn"><code>@AJ</code></a><code>","name":"","ref":"D 900"},{"intersections":[{"out":0,"location":[2.817484,42.521392],"bearings":[0,120,195],"entry":[true,false,false],"in":1},{"out":2,"location":[2.817357,42.521642],"bearings":[135,300,330],"entry":[false,true,true],"in":0}],"maneuver":{"exit":1,"type":"roundabout","modifier":"right","location":[2.817484,42.521392],"bearing_after":0,"bearing_before":285},"distance":189.6,"duration":13.4,"geometry":"u}obGghePS?MDKHCFMNQD_</code><a href="https://help.openstreetmap.org/users/15/bass"><code>@B</code></a><code>]E[Gq@M_@GgA[","name":"","mode":"driving"},{"intersections":[{"out":0,"location":[2.817553,42.523017],"bearings":[0,15,195],"entry":[true,true,false],"in":2}],"maneuver":{"type":"fork","modifier":"slight left","location":[2.817553,42.523017],"bearing_after":7,"bearing_before":16},"distance":1311,"duration":82.6,"geometry":"{gpbGuhePkAMe@GMAIAsDg@c@M[WKOOa@GYGUGuB@mAFoDBcBAq@Gg@G]Ma</code><a href="https://help.openstreetmap.org/users/269/qwartz"><code>@Q</code></a><code>_@Y]c@Os@CuACmBUiDu@kFmA}@[y@c@c</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>@y@u</code><a href="https://help.openstreetmap.org/users/136/acrosscanadatrails"><code>@a</code></a><code>BsBaE}F","name":"","mode":"driving"},{"intersections":[{"out":0,"location":[2.82549,42.531479],"bearings":[49,224,227],"entry":[true,false,false],"in":1}],"maneuver":{"type":"merge","modifier":"slight left","location":[2.82549,42.531479],"bearing_after":49,"bearing_before":44},"mode":"driving","distance":5714.7,"duration":179.1,"geometry":"w|qbGizfPqA_CqAiCmAkCyAuDkBkF}CmJyCyJgIuWiCmHmEaLwCiGeCuE}BsD_B_CiDaEiBmByBoB{BeB}</code><a href="https://help.openstreetmap.org/users/101/iknowjoseph"></a><a href="https://help.openstreetmap.org/users/101/iknowjoseph"><code>@i</code></a></a><code>@}AaAcB_AaBw@oBw@yDiAcDs@kC_</code><a href="https://help.openstreetmap.org/users/231/_jeremy"><code>@_</code></a><code>CSwDMaC?[?cDNqBLwBXgDn@cElAcCz@oH</code>DkK|EiEdBiEzAgFvAiFlAwDp<a href="https://help.openstreetmap.org/users/136/acrosscanadatrails">@a</a>D`@sCZmDXwDRmDLcEHaEBgIC_CE_FS","name":"La Catalane","ref":"A 9"},{"intersections":[{"in":0,"entry":[true],"bearings":[184],"location":[2.844077,42.573677]}],"maneuver":{"bearing_before":4,"location":[2.82549,42.531479],"bearing_after":0,"type":"arrive"},"mode":"driving","distance":0,"duration":0,"geometry":"odzbGonjP","name":"La Catalane","ref":"A 9"}],"summary":"D 900, La Catalane","duration":771.2,"distance":17488.1}],"duration":771.2,"distance":17488.1}],"waypoints":[{"hint":"XYcCgPOkCIDktwEAEgAAAAAAAAAAAAAASQEAADj0AwBtFRMABBAAAE2wKwDn9ocCYLkrAFT2hwIAAAEBm5ShTg==","name":"Avenue de France - Avinguda Catalunya","location":[2.863181,42.464999]},{"hint":"40wAgP___38gMgAAJwAAAD0AAADYBgAA5gsAAPZyEAAcAQgABBAAAK1lKwBtn4kCl2UrAG-fiQI0AAEBm5ShTg==","name":"La Catalane","location":[2.844077,42.573677]}]}</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm-routed_filter" rel="tag" title="see questions tagged &#39;osrm-routed_filter&#39;">osrm-routed_filter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '17, 08:12</strong></p>
<img src="https://secure.gravatar.com/avatar/7998acb6628483825d62dc4f11055d2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="06pboivin06&#39;s gravatar image" />
<p><span>06pboivin06</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="06pboivin06 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54093" class="comments-container">
&#10;</div>
<div id="comment-tools-54093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54093-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="54095"></span>

<div id="answer-container-54095" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54095-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>I checked with my own server and indeed, I got 15km too (taking AP-7 motorway).</p>
<p>Are you sure you don't have "ignore_toll_ways = true" in your profile.lua ? It could force osrm to calculate an "alternative" route if the speedway isn't free.</p>
<p>And just to be sure, coordinates from your example are in spain. You spoke about france-latest.pbf. I suppose it's another test...</p>
<p>Feel free to post your profile.lua file. It could be usefull to compare parameters.</p>
<p>Regards,</p>
<p>Thibaut</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '17, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/816af79b74293db229a512509be4b0e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThibPhil&#39;s gravatar image" />
<p><span>ThibPhil</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThibPhil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54095" class="comments-container">
&#10;</div>
<div id="comment-tools-54095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54095-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54118"></span>

<div id="answer-container-54118" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54118-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just to be sure, do you have such problem everywhere on highways or only near the French/Spanish border ?</p>
<p>If not a lua configuration problem, it could be a snapping problem due to a missing motorway segment at the border (as you are using france-latest.pbf extract, I don't know where the road is "cut" in this file. If the last (close to the border) segment is missing, it'll snap on the first found way (and as you imported only motorway, trunk, primary and secondary, the nearest object is indeed "D900 - Avenue de France).</p>
<p>If you want, I can import the same PBF file and do some tests. If needed, feel free :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '17, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/816af79b74293db229a512509be4b0e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThibPhil&#39;s gravatar image" />
<p><span>ThibPhil</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThibPhil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54118" class="comments-container">
&#10;</div>
<div id="comment-tools-54118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54118-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54102"></span>

<div id="answer-container-54102" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54102-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks Thibaut for the hint, I'll check my profile.lua . The initial coordinate I gave (42.464852,2.865504), according to google maps (<a href="https://www.google.fr/maps/place/42%C2%B027&#39;53.5%22N+2%C2%B051&#39;55.8%22E/@42.4648559,2.8653672,21z/data=!4m5!3m4!1s0x0:0x0!8m2!3d42.464852!4d2.865504)">https://www.google.fr/maps/place/42%C2%B027'53.5%22N+2%C2%B051'55.8%22E/@42.4648559,2.8653672,21z/data=!4m5!3m4!1s0x0:0x0!8m2!3d42.464852!4d2.865504)</a> is close to the border with Spain but in France. When I try to feed my coordinates to OSM directions (<a href="https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=42.4652%2C2.8657%3B42.5789%2C2.8450#map=12/42.5220/2.8417)">https://www.openstreetmap.org/directions?engine=osrm_car&amp;route=42.4652%2C2.8657%3B42.5789%2C2.8450#map=12/42.5220/2.8417)</a> , it positions the start point on the border with Spain, I guess it's because that is the closest node to 42.464852,2.865504 that is known in the OSM file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '17, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/7998acb6628483825d62dc4f11055d2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="06pboivin06&#39;s gravatar image" />
<p><span>06pboivin06</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="06pboivin06 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54102" class="comments-container">
&#10;</div>
<div id="comment-tools-54102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54102-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54121"></span>

<div id="answer-container-54121" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54121-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you are right Thibaut, it must be a snapping problem. I tried different origin coordinates progressing further and further inside France and when I reach enough inside France I get the same response as the Demo server. So the France OSM file must be missing a part of the French motorway and it snaps on the minor French road it finds closest. In fact, I get the same problem close to Italy border. In the center of France no such issues. Maybe I should try a to create a file resulting from merge of France plus the countries bordering France.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '17, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/7998acb6628483825d62dc4f11055d2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="06pboivin06&#39;s gravatar image" />
<p><span>06pboivin06</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="06pboivin06 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54121" class="comments-container">
<span id="54132"></span>
<div id="comment-54132" class="comment">
<div id="post-54132-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, you can merge different countries but maybe the easiest way for you should be to download europe-latest.pbf and to use osmosis (giving an extent covering France + surrounding area) to re-create a new PBF.</p>
<p>Or, if your server has enough RAM and perfs, you can try to compute osrm files on entire Europe (if needed, of course...). Just for information, for entire Europe, works fine with 40Gb RAM, 512Gb on SSD.</p>
</div>
<div id="comment-54132-info" class="comment-info">
<span class="comment-age">(18 Jan '17, 09:21)</span> <span class="comment-user userinfo">ThibPhil</span>
</div>
</div>
</div>
<div id="comment-tools-54121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54121-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>


+++
type = "question"
title = "How to work with osrm."
description = '''Hi, I try out how to work with osrm.  Lets say I do have two different points (one in Aachen and one in Brussel). I can ask for the map with: http://map.project-osrm.org/?hl=de&amp;amp;loc=50.776279,6.084859&amp;amp;loc=50.841579,4.366734&amp;amp;z=10&amp;amp;center=50.894572,4.945387&amp;amp;alt=0&amp;amp;df=0&amp;amp;re=0&amp;am...'''
date = "2015-02-27T10:48:00Z"
lastmod = "2015-03-02T10:46:00Z"
weight = 41407
keywords = [ "osrm", "json", "nominatim", "router", "distance" ]
aliases = [ "/questions/41407" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to work with osrm.](/questions/41407/how-to-work-with-osrm)

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
<span id="post-41407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41407-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I try out how to work with osrm.</p>
<p>Lets say I do have two different points (one in Aachen and one in Brussel).</p>
<p>I can ask for the map with: <a href="http://map.project-osrm.org/?hl=de&amp;loc=50.776279,6.084859&amp;loc=50.841579,4.366734&amp;z=10&amp;center=50.894572,4.945387&amp;alt=0&amp;df=0&amp;re=0&amp;ly=763558683">http://map.project-osrm.org/?hl=de&amp;loc=50.776279,6.084859&amp;loc=50.841579,4.366734&amp;z=10&amp;center=50.894572,4.945387&amp;alt=0&amp;df=0&amp;re=0&amp;ly=763558683</a></p>
<p>Now I want to trace that route and count the distance. <a href="http://router.project-osrm.org/viaroute?loc=50.776279,6.084859&amp;loc=50.841579,4.366734">http://router.project-osrm.org/viaroute?loc=50.776279,6.084859&amp;loc=50.841579,4.366734</a></p>
<p>I receive this one:</p>
<pre><code>{&quot;hint_data&quot;:{&quot;locations&quot;:[&quot;9HUWANgJugEdgiQAAAAAABoAAAAAAAAAAAAAAP____8AAAAA18gGA_vYXAAAABEA&quot;,&quot;t8gWBP_____HvRQANwAAAEgAAAAiAAAACAAAAHCp3AMAAAAA68cHA46hQgACABEA&quot;],&quot;checksum&quot;:1423277062},&quot;route_name&quot;:[&quot;&quot;,&quot;&quot;],&quot;via_indices&quot;:[0,1055],&quot;via_points&quot;:[[50.776279,6.084859],[50.841579,4.366734]],&quot;found_alternative&quot;:false,&quot;route_summary&quot;:{&quot;end_point&quot;:&quot;Avenue des Arts - Kunstlaan&quot;,&quot;start_point&quot;:&quot;Büchel&quot;,&quot;total_time&quot;:5160,&quot;total_distance&quot;:142783},&quot;route_geometry&quot;:&quot;klcz_BunkrJeAwJmLiN_FaOwNuU_FaIwHaLmDuFeJ}N{PpHuDdBmOgAuCUcLOaEzl@c@jGeDnl@iAxL_@`E[hDcArK}@tGa@fCcEjWoErT_AvEwA~GsIlb@aDhNeBfIuAlIgApG_AjDyBrDiGbH_F`G{KdNyKzNyFpU{@nDyBpHwP`h@wFxMwOxZeMjPwBxC_A~QcB~D_F~F_FrDeEnCsCtBqBtBg^~[qYhf@gAhBeF~I}JvQ{f@v|@{Wpe@cCjEuBtDgDfGkAvBqCzE_p@jjAgD`GiSd^{FfK_DvFcAhBaBrCgItNmDfGwDzGiAnByAfCaMtTmKdR_DtFuA~BsBzDyJrQmChEsCvEsJpO_NlRqMhOyRlOuU`MsOvEmOnBcHr@qWqAiOuA{MaC_Z}IeW{OcRmOsWeXqM}O}T{`@ko@c}A}Og\\oWic@uOmSaV{V}VoQwZePg[{Ju_@cIic@_EmdA_@wqAeAel@gAwu@oDaf@gEop@wKaOaDeRyEqDw@yz@_TeZkG{b@wGg[s@}]?cFCg@dHPtc@b@he@~@ff@lBjR|ChNvF|KnQzTtIxOfEjMhBnPTpG@nFKzFi@lKyE|f@}h@rsCo`@`~BaK`{@oLteAqFpm@mG~y@{HvvAoBlg@wAdg@e@rp@}@jg@It}@x@h}B\\ze@r@bvDKjd@W`iAeCx{A_GfdBcGhbAiEdk@{LjvAyP`sA}RbnAoXnuAo^n_Byd@xbBse@|uAui@zwAqG|Ngq@`uAsh@hz@cE~FoRpZeIfM_f@lo@ku@h{@_WlXeTlUimAnnAus@rs@ulAjnA}InJuzCd|C_k@bm@u}Cv}CmQbQ}xDb`EydF~fFabDrdDmoBrpBol@ts@sm@lx@sg@zw@on@bmAwHbRsRjb@cx@lkBkcBvnFqMnb@aqEr|N{s@h|Bsg@z_Bw`@reAkf@vhAqvAjlCaYfc@{Vz\\km@|x@gv@hy@wtAxlAos@pk@kuAn_AwaBffAw`@nUuyBztAy{BrzA_eA~u@_mArcAgmAvfA}nCdqCk_CtrCgjC`_DgdAbhAqzAn|Aa}@`|@a]xYmmBzeBcM~Jq~AryAk|@j{@izBj~BkpBj|Bc{FlnHy|BzrCs|BvnCwgAdmA}vBjsBscHfwG_`@~]m{@`y@uT|S{qAhnAy|AnzAsRvRuX`\\gP`TyUd[iWz_@m\\di@uVpc@gSz^gc@z{@y\\n{@mf@luAqUzw@{HzY_XtdAgYdwAi^ljBkcCjsMeFnXevAhuHqCpLmHz[{Jj`@eHtVgItW_Tpj@{f@rnAgm@tuAyUnh@sHtOyO~Y_Sj[gMlO_MzMiLrKof@|^eu@di@}KbIac@zY}Z`SitAtu@{hBt}@gnDxiBqlGdjEeMvJ{bAfu@_VhTuVpX}_@lf@mNnSuYlg@cNzU{[`u@kV|s@wmAl{DeJlYqdAlfDcQzq@aS~aAoLhr@gJ~w@ghA`~KiSzpC{SdrDoTniDiGbjAeFrs@kEn`@kFxYmHja@iGlWuJd\\{Pdh@oHjQshB|aF_U`s@eKdf@kHbg@_`@`jE{BhZsTprCcVfgCkRjxAaIfb@aLzi@w{GdsUouBlnHgi@pbBmRpe@ab@vaAyrCvqF{jBlqDmJjR}pAvhCcEnIaIpPydCfcF}`An_C}k@baBqWpy@gKr_@wL`f@uIzb@mHbc@aHhg@eFtb@{Fhn@sCbb@_Dhl@wBtq@s@xm@Ctx@bAxcAXtO`EbvA|GtcBzI|tAhH~~@`P`fB`Jvy@vNpdAvQ`mAxOr`A|`@dtBrOdq@be@`kBlpBzuGb[|cAlf@x_BnbBpoFzkAbyDdkB`eGb{@|pCzm@ryBpOnl@xWjhAlZ~wA~Oxx@xDxShV`yAhSpyApOdqArJbz@rX|~CzMltBdC`f@bEd{@hGv_CfA`r@bCtaCAj`BgA~aB}D|xB_S|xGiUf_HiGnoBkh@pqOs[h|JoArj@w[rmJsuAbsb@{Chy@eHzsAwExy@{JdxAgLvqA}L~mAkLndAiu@ztFyv@`wFq{@n{GqRffByRpoB{ZtbEiGz{@mWrlEsO~lDqRnlEe\\t_Iqa@txIo]|eGg]zbFck@x}Gkb@rjEco@r|Fif@x{Dw`@blDok@tbEgcCj`RmiAz}Ie`CpuQq_DrbVud@zzCyk@reD_^|iBy_@|hB}}@xcEkg@d|Bq`AdkEqlGffYmxHro]gOvq@_i@|`CwsB~iJcnApvFuOrr@aqAz_GoU`iA{^drBkS|mAyNb_AqOxgA{]rpC{OvpA}UhnBer@ryFsOloA_T`dBgSraBs]|uCsnAxdKqcAzkIeRf|Ac{@thHgEn^oQn{AcI`s@kMvhAmmAvqK}jAp~JqvChyVgoAppKa[bbDkOjkBaKpzAuH~sA{Drv@qDtz@eD``AyCrdA}CvzA}AbfAoAxoBm@zpBlDpi_@`BbmMvCphXvBxePp@`lHrAx|Jz@hyH`BtgOVbuA?th@|AvlDxCbiBjCtmArF~tApJhmB`E`p@rNvjBhPvhBle@`wEp_AraJ|RlkB|t@xdH`f@zuEh{@xjIfMvqAxKrvApKndBzEf`AlkAr~Uv\\z~GreBjy]r`A~xRtRnyD`Zj`GxV~bFrKr|Brp@rmMzTpfFjMjpBlFrhAjEpt@dDbv@lCpg@xY|~Fl_@llHxNjtBnNzfBbMzqArUnzB|d@z_DpRhiArg@tqCzn@peDplKzzi@|k@~uCv^hbBvi@|uBzj@hrBd}Al_Fp}A||Evc@psAvU~s@fjGzmRdn@xrBx^lfAlnBh`Gl_C|jHhQzj@tn@jsBz`@jtAn~@zrDd^fdBh]nlBjLjq@rTvxAz[jiCrWrmCpK|wA|IvyA`HhuA~FjwAbKpdDbI|aDfR|dIpKv}CtCzn@~I~eB`D`h@jIhhApQ|qBfPh{AtR~{A`Vr}ApAfIbCrOhFb\\`Pd{@pJde@hCdMhOtq@rQzx@nV~~@|Vl_AtWn}@rYv|@~q@nnB~v@tkBnz@~gB|{@`aBf_AndBnQnZhwCdaFzfC|qEviAf~Bbj@nnAnYjr@pr@vnBzi@nfBho@tbCv^lfBdUznAf]`wBjYncCbLrjAvJvlAtQhhDjFjaBtApu@z@rv@b@~y@Ej~@i@vgAq@xc@y@tb@iDtoAsBrk@kC|i@qB``@{IbvAiL|rAiKzaAeLj_AmBjOcJ|q@{Ltw@qMvs@_Rp~@iTbcAeQbt@eY`eAsPrj@mj@tcBq~@hcCycAfgCyLjYypBv_F{f@bpA_ChG}Opb@{_@~gAs[paA{Qtm@uRzr@gRpu@wPfu@mNnr@cLxn@oJ`k@_N|_AqEz^oKjaAuJ|eAwFpw@}FnbA{Dr~@}Bnw@kBhcAw@hmAVteAdAhrAlCxlAjGnlBvI|kB|Vb_FjRb{D`Jp|B~GnaC~ChbBnAdbA`Al`A^pbAFtaAO~zAu@~tAaCznBgD`cBaEpuAsHtxBwUjpFuTpsEwSzrEqJpyB{K~oBmP``EaC|f@eG`lAwv@`xOkQ~zEuRbzEaPfjFoG~aCgEh~BgIl~FwHj`GsJj_GyKhaGgMf_GmN`}FkGl~BgHhdCeY|{Iy[`vIuKhnCkL~kCaZtwG}u@fsP_PhrDcMd|D}D|jAqB`dAcB~eAkA`jASp^ObbAh@pdAv@j~@|Arz@vA|o@bC|k@vB|k@tC|k@nL`pBtKbmAxSzqBnHrk@~N|cAvPzbAnRpaAfSn`ArYxpAx[~nA`]lmAd^zjAnJpZtHtUfnApoDvpA`lDzcDlwIj]l`AnJ`[zq@xtB`t@toCtYdnAvV`nA~t@pcEjq@pdEhgA~yGlfBp{KvYdfBzYjeBz[`eBx\\bdBbSh~@~Sz}@fT~|@xTd|@~a@h}Avb@`|AhgAjvDjhAxxDtc@h{Anf@~xA|m@raBrWvn@dXtm@xg@pgAfk@pgAnl@ddAze@zx@vv@lfAjvBrkCndD|_EjfPl`Sz~InxKnlBf`CjM`PheAnqA`J~KjN`QxMhOnhAbsA|kCnbDpMxOzL|Nze@dn@zTb]pQzZpIbSnJnRd[tt@jQdl@tmBziHxpBhsHrOfh@nYty@hRre@rSpc@`e@t{@vy@ltAfxBhqDhV|b@bXbi@d]vx@|Qjk@zQbn@t`@zzAf{AvtFb]jnAfm@rwB`i@v}Ah[dt@~S~`@lXre@`_@ph@`V`Ztm@fl@lp@ng@jlBhpAx[xTx}BrdBff@za@z\\t\\jUlXfY|Zv_@jh@zXhd@fVxd@|Nr\\lTlk@tJz\\|_@`sAhYplAbJp]db@tlBbUpy@r`@jfAlZnr@hZne@rWn_@jWv[pNtO|YrWf]|Wv[fR|XlNlPbGlb@lNh]`Jxb@hKvs@rQb\\jL|]pPzNxHr[lR`RdNxd@dc@jtBt}BffDhyDpPxQhw@h`A~Qj\\xIfOlm@n~@xQxZxOh^lSlm@vO~i@pVnkAlh@h{CnIz~@pAt]x@z]Hdm@iBl_AqApWkBza@iUnjD}P`~CsS`qDsb@~bGaEji@oDff@uApUad@jrGm[vlEgPf_Cci@leHquAl|O{w@bsIwEtg@eZfvCu~@llKmD|b@coAbdN_b@hiFmRjyCwLp|B_OjkDkBxe@sLv_DmEtrAuJr{DyHzaFsBv}CcB~zDk@xdECr{DcBtj\\HpnPJ`nK_@dhHYbz^E`jMxAr_A`CtrBb@tg@dFnnCtIxoCxHlgBhF`eAtHvrAtNlxBdDdc@|Rv_C|e@ftElk@~lE|D`Wv]xaCnDpVht@daFfQjhAjDpVb[psBpf@zcDdk@rcD~AzHrX~tAxhC~pLz]fcBrU`rAxzAtfH`_@r`BdRdu@x^fpAlc@~{Afu@`aCff@pbBrJb[xGlT`a@~kA`k@rgBl]|_Aj`@ppA|Ohn@fKn[dGfVdH~ZvWziAfPzt@vBhJbDlMpPjl@d_@njBxJ`]nOzYtUneAnpAdpJ|Glj@nIp]v_@tpAdZn{@hKpTbFbJlJtZpElNnFvOpUhq@p[f~@|Vpv@xLf[~Rjl@nIpWbBlExClI~t@zsBfC`HkB`CyA`DcAxDk@jEQfH`@dHrAhG|BzEcAbIaFrf@}@tIoUzlBg@pQcA`IiKxx@t@~HgEr[qBhOiGrf@uYj_C}AbMsGph@i@`EiLh_AaA|HcMvbAqGdh@{Fbe@sGxh@mBpOwA~Ke@|DgDnXeF~a@eAdIeAxImBrOgAnIjEtC`Cx@tn@`SrD`Bxc@vRx[|N|FrFxYfMrGlDxDxBfIiAhc@jPnCbApDvAln@jYbH|IrQ~TrCkUmDkGkNmSeh@uW&quot;,&quot;status_message&quot;:&quot;Found route between points&quot;,&quot;status&quot;:0}</code></pre>
<p>I thought that I could forward this information to <a href="http://nominatim.openstreetmap.org/search/format=json">http://nominatim.openstreetmap.org/search/format=json</a> and then the above mentioned file. It just does not work. Any idea how I could do it right?</p>
<p>Thanks for your advice</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '15, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/2e4706b690bf4e8533fca09391851d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karten-Newbie&#39;s gravatar image" />
<p><span>Karten-Newbie</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karten-Newbie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '15, 12:20</strong> </span></p>
</div>
</div>
<div id="comments-container-41407" class="comments-container">
<span id="41410"></span>
<div id="comment-41410" class="comment">
<div id="post-41410-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Why do you want to pass the OSRM output to Nominatim? What result are you expecting? Nominatim is a geocoder, it is just able to convert single addresses to geographic locations and vice-versa. It won't understand route instructions.</p>
<p>Regarding your other questions: 5160 does indeed correspond to the required time in seconds and 142783 corresponds to the distance in meters.</p>
</div>
<div id="comment-41410-info" class="comment-info">
<span class="comment-age">(27 Feb '15, 11:55)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="41411"></span>
<div id="comment-41411" class="comment">
<div id="post-41411-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your advice ...</p>
<p>I've deleted the two questions because I realized how dumb they are :-(</p>
<p>What I'm looking for is a tool which receives the route from osrm-website and "answers" with a file in a format which I could analyze in a a way like.</p>
<ul>
<li>100m, xx sec, Street, Germany</li>
<li>34567m, xy sec, Highway, Germany</li>
<li>23235m, zz sec, Highway, Belgium</li>
</ul>
<p>I thought that nominatim could provide that answer, when I "give" that file to it.</p>
<p>I guess it is a dumb idea. It would be really kind if you give me a hint which tool or way might be the right one. I promise I will try to read and understand the manual of that tool, before I ask again. ;-)</p>
</div>
<div id="comment-41411-info" class="comment-info">
<span class="comment-age">(27 Feb '15, 12:27)</span> <span class="comment-user userinfo">Karten-Newbie</span>
</div>
</div>
<span id="41412"></span>
<div id="comment-41412" class="comment">
<div id="post-41412-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't worry, we all learn something new every day :) But unfortunately I'm not aware of such a tool.</p>
</div>
<div id="comment-41412-info" class="comment-info">
<span class="comment-age">(27 Feb '15, 12:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41407" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41407-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="41446"></span>

<div id="answer-container-41446" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41446-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks to google I found the explanation why I could not read the json-file.</p>
<p><a href="http://router.project-osrm.org/viaroute?compression=false?loc=50.776279,6.084859&amp;loc=50.841579,4.366734">http://router.project-osrm.org/viaroute?compression=false?loc=50.776279,6.084859&amp;loc=50.841579,4.366734</a></p>
<p>The <strong>?compression=false</strong> makes the difference!</p>
<p>Now I could use the points and get with nomination the answer in which country the point is. But there is another problem for me:</p>
<p>I do not know which distance I have! How could I get the distance for these waypoints?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '15, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/2e4706b690bf4e8533fca09391851d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karten-Newbie&#39;s gravatar image" />
<p><span>Karten-Newbie</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karten-Newbie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41446" class="comments-container">
<span id="41448"></span>
<div id="comment-41448" class="comment">
<div id="post-41448-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that without ?compression=false, the polyline is in Google polyline format. You can decode this into lat/lon pairs with a Google polyline decoding library - one exists in most popular languages.</p>
</div>
<div id="comment-41448-info" class="comment-info">
<span class="comment-age">(02 Mar '15, 10:46)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41446-form-container" class="comment-form-container">
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

</div>

</div>


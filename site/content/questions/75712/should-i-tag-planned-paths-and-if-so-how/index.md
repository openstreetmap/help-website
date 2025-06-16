+++
type = "question"
title = "Should I tag planned paths? and if so how?"
description = '''there are two paths coming, I don&#x27;t know the date, they are not built yet. so I won&#x27;t add them. but if I were to add them as proposed or planned or something, I see roads some places are tagged as proposed. but this is a walk and bike path.'''
date = "2020-07-15T07:52:00Z"
lastmod = "2020-07-18T09:30:00Z"
weight = 75712
keywords = [ "path", "bike", "proposed", "cycle" ]
aliases = [ "/questions/75712" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Should I tag planned paths? and if so how?](/questions/75712/should-i-tag-planned-paths-and-if-so-how)

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
<span id="post-75712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75712-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>there are two paths coming, I don't know the date, they are not built yet. so I won't add them. but if I were to add them as proposed or planned or something, I see roads some places are tagged as proposed. but this is a walk and bike path.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-bike" rel="tag" title="see questions tagged &#39;bike&#39;">bike</span> <span class="post-tag tag-link-proposed" rel="tag" title="see questions tagged &#39;proposed&#39;">proposed</span> <span class="post-tag tag-link-cycle" rel="tag" title="see questions tagged &#39;cycle&#39;">cycle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '20, 07:52</strong></p>
<img src="https://secure.gravatar.com/avatar/36fe123bbb61e49a67eae244eddcca16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtbboy1993&#39;s gravatar image" />
<p><span>mtbboy1993</span><br />
<span class="score" title="40 reputation points">40</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtbboy1993 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75712" class="comments-container">
&#10;</div>
<div id="comment-tools-75712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75712-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="75741"></span>

<div id="answer-container-75741" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75741-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to <a href="https://wiki.openstreetmap.org/wiki/Lifecycle_prefix">lifecycle prefix</a> planned and proposed paths should be tagged as <code>highway=proposed</code> + <code>proposed=*</code>. For your case, a path for walking and cycling, I would use <code>highway=proposed</code> + <code>proposed=path</code>. There is no need for any access tags since proposed paths are not used for routing.</p>
<p>If the path is already in construction then use <code>highway=construction</code> + <code>construction=*</code> instead. For your case this would be <code>highway=construction</code> + <code>construction=path</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '20, 07:23</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-75741" class="comments-container">
&#10;</div>
<div id="comment-tools-75741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75741-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75721"></span>

<div id="answer-container-75721" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75721-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's one i have mapped</p>
<p><img src="/upfiles/New_Path_RQJQyQl.JPG" alt="alt text" /></p>
<p>I could have also added a proposed tag, but it is an actual path now and the local authority have confirmed it. It isn't open yet. One problem is surveying something when you should not be there, or copying it from a copyrighted plan, which isn't allowed of course. Letting people know what is planned is, i think a good idea. Edit I guess new path could be at different stages, proposed, planned, under construction with a barrier fence before finally being opened as a designated path for for example foot and or/or cycles or horses.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '20, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jul '20, 14:38</strong> </span></p>
</div>
</div>
<div id="comments-container-75721" class="comments-container">
<span id="75739"></span>
<div id="comment-75739" class="comment">
<div id="post-75739-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>the path has been planned for years, and now it's confirmed it will come, but no date set. but I have seen the plan drawings. there is no path built yet. but the money is there, it will cost 50 million Nok <a href="https://www.smaalenene.no/lokale-nyheter/punger-ut-50-millioner-til-gangvei-her/s/1-87-7189782">https://www.smaalenene.no/lokale-nyheter/punger-ut-50-millioner-til-gangvei-her/s/1-87-7189782</a> <a href="https://viken.no/tjenester/vei-og-kollektiv/fylkesvei/veiprosjekter/veiprosjektartikler/fv-128-slitu-sekkelsten.22187.aspx">https://viken.no/tjenester/vei-og-kollektiv/fylkesvei/veiprosjekter/veiprosjektartikler/fv-128-slitu-sekkelsten.22187.aspx</a></p>
</div>
<div id="comment-75739-info" class="comment-info">
<span class="comment-age">(16 Jul '20, 05:42)</span> <span class="comment-user userinfo">mtbboy1993</span>
</div>
</div>
<span id="75740"></span>
<div id="comment-75740" class="comment">
<div id="post-75740-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>there is a path that is under construction at a different location, that one has the drainage carpet and gravel already laid, no asphalt yet, and is a dead end. how should I tag it? it's planned to connect to a bridge that already is, the path will go around an apartment building that is planned. sign and swing gate is set up. I tagged it as a closed road, is that correct? <a href="https://www.openstreetmap.org/way/720561813">https://www.openstreetmap.org/way/720561813</a></p>
</div>
<div id="comment-75740-info" class="comment-info">
<span class="comment-age">(16 Jul '20, 05:48)</span> <span class="comment-user userinfo">mtbboy1993</span>
</div>
</div>
<span id="75744"></span>
<div id="comment-75744" class="comment">
<div id="post-75744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>where did you get that system from?, I don't have this.</p>
</div>
<div id="comment-75744-info" class="comment-info">
<span class="comment-age">(16 Jul '20, 09:34)</span> <span class="comment-user userinfo">mtbboy1993</span>
</div>
</div>
<span id="75749"></span>
<div id="comment-75749" class="comment not_top_scorer">
<div id="post-75749-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The second path example looks OK to me. In the last comment what system are you speaking of?</p>
</div>
<div id="comment-75749-info" class="comment-info">
<span class="comment-age">(16 Jul '20, 18:38)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="75757"></span>
<div id="comment-75757" class="comment">
<div id="post-75757-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If a path is mapped from a plan, and that plan is based on a copyrighted source we should NOT copy from it. If path position can be estimated from a remote survey and/or bing or other OSM supplied source then it should not be a problem.</p>
</div>
<div id="comment-75757-info" class="comment-info">
<span class="comment-age">(17 Jul '20, 06:36)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="75773"></span>
<div id="comment-75773" class="comment not_top_scorer">
<div id="post-75773-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I meant the window thing wit the blue stuff and all. what key do you press to get that? is that desktop software or is this in OSM website? sure looks to be the website.</p>
</div>
<div id="comment-75773-info" class="comment-info">
<span class="comment-age">(18 Jul '20, 09:18)</span> <span class="comment-user userinfo">mtbboy1993</span>
</div>
</div>
<span id="75774"></span>
<div id="comment-75774" class="comment">
<div id="post-75774-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>mtbboy1993 The jpeg i attached was a window snip of the Potlatch2 editor with a new path selected and ready to edit. The side panel shows the tags i used at the time.</p>
</div>
<div id="comment-75774-info" class="comment-info">
<span class="comment-age">(18 Jul '20, 09:24)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="75775"></span>
<div id="comment-75775" class="comment not_top_scorer">
<div id="post-75775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I walked this path a couple of months ago and according to the local press work had finished on it ( A14 road project ) BUT the contractors are still working and it's now locked off at the underpass of the A14 which is to the north of my pic. ( i checked on the 17072020</p>
</div>
<div id="comment-75775-info" class="comment-info">
<span class="comment-age">(18 Jul '20, 09:30)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-75721" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-75721-form-container" class="comment-form-container">
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


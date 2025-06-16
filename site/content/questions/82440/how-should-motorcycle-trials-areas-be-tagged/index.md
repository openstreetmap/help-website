+++
type = "question"
title = "How should motorcycle trials areas be tagged?"
description = '''These are designated areas where cross-country (i.e. off trail) access by motorcycles is permitted. I searched OSM wiki, forums, and help and didn&#x27;t see anything specific to this topic. I&#x27;d be happy to have a reference to exiting documentation if there is some. My first guess was to use an area with...'''
date = "2021-11-01T15:06:00Z"
lastmod = "2021-11-01T19:50:00Z"
weight = 82440
keywords = [ "motorcycle", "area" ]
aliases = [ "/questions/82440" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How should motorcycle trials areas be tagged?](/questions/82440/how-should-motorcycle-trials-areas-be-tagged)

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
<span id="post-82440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82440-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>These are designated areas where cross-country (i.e. off trail) access by motorcycles is permitted. I searched OSM wiki, forums, and help and didn't see anything specific to this topic. I'd be happy to have a reference to exiting documentation if there is some.</p>
<p>My first guess was to use an area with leisure=park and motorcycle=yes, but is there a better way to indicate the nature of these areas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-motorcycle" rel="tag" title="see questions tagged &#39;motorcycle&#39;">motorcycle</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '21, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/684423178235ce4cdb2620edbe9f1035?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="b1tw153&#39;s gravatar image" />
<p><span>b1tw153</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="b1tw153 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82440" class="comments-container">
&#10;</div>
<div id="comment-tools-82440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82440-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="82446"></span>

<div id="answer-container-82446" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82446-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="b1tw153 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please don't use <code>leisure=park</code>: this will generally be taken to mean people can go for a stroll, walk the dog, stop for a picnic etc.</p>
<ul>
<li>If there are apparent trails in the area used by riders then they can be marked with regular highway tags, with appropriate access tags (e.g. motorcycle=customers).</li>
<li>If it's used for competitive sports such as Motocross then leisure=track sport=motocross. See this <a href="https://www.rogershillraceway.com/">location</a> for an example.</li>
<li>If it's just a generic area where people go where they will then I dont know if we have any specific usage. The general approach would be to use a <code>leisure</code> tag, perhaps something like offroad_driving (which would cover both 4wd vehicles and trail bikes) with further tags for additional precision.</li>
</ul>
<p>I've had a quick look for 4 wheel drive off-road experience locations in the UK (such as <a href="https://mudmayhem.co.uk/en/venues/4x4-off-roading/dorset/oTown-146719">these</a>), but although they are quite common, they appear to be unmapped. I note that a related driving activity skid pans do not appear to be mapped much (2 that <a href="https://taginfo.openstreetmap.org/tags/name=Skid%20pan">I can find</a>).</p>
<p>Obviously a shortage of real petrolheads in OSM (I once worked for a small firm where I was the only person without this obsession : company days were 4wd off-road, karting &amp; the firm sponsored a colleague who raced homologated Honda ....)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '21, 17:38</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-82446" class="comments-container">
&#10;</div>
<div id="comment-tools-82446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82446-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82445"></span>

<div id="answer-container-82445" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82445-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think leisure=park fits. If motorcycles can freely use any part of the area (not just specific ways), that seems to rule out "typical" park-like activities such as strolling around enjoying the fresh air. An access tag such as motorcycle=yes shouldn't be used to completely change the meaning of the main tag.</p>
<p>It sounds more like a dedicated sports facility than a park. Is it similar to <a href="https://wiki.openstreetmap.org/wiki/Tag:sport%3Dmotocross">https://wiki.openstreetmap.org/wiki/Tag:sport%3Dmotocross</a> ?</p>
<p>An example might help (e.g. a location where we can see background imagery, or the website of such a facility).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '21, 17:16</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-82445" class="comments-container">
&#10;</div>
<div id="comment-tools-82445" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82445-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82447"></span>

<div id="answer-container-82447" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82447-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for the quick replies. I'm happy to change the tags to something more appropriate than leisure=park if it's clear what the tags should be.</p>
<p>Maybe an example will help. The areas in question are designated in the Cleveland National Forest Motor Vehicle Use Map. Here's how the map depicts these areas.</p>
<p><img src="/upfiles/Screen_Shot_2021-11-01_at_11.46.19_AM.png" alt="alt text" /></p>
<p>The USFS map legend makes it clear that the Trials Areas are for motorcycle use only even though some trails (e.g. 901) are also option to ATVs, and other trails (e.g. 903) are open to any street-legal motor vehicle.</p>
<p>Here's a link to one of the areas off the 912A route: <a href="https://www.openstreetmap.org/way/998197106">Trials Area</a>. If you look at the aerial imagery, you can see that this is not a motocross track. It's just a rock outcropping that has been designated as an open riding area.</p>
<p>For reference, <a href="https://en.wikipedia.org/wiki/Motorcycle_trials">motorcycle trials</a> is a distinct sport from motocross. So I wouldn't think that leisure=track or sport=motocross would be appropriate here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '21, 19:00</strong></p>
<img src="https://secure.gravatar.com/avatar/684423178235ce4cdb2620edbe9f1035?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="b1tw153&#39;s gravatar image" />
<p><span>b1tw153</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="b1tw153 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-82447" class="comments-container">
<span id="82449"></span>
<div id="comment-82449" class="comment">
<div id="post-82449-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I suspected as much, but wanted to cover the principal bases. I believe BMX riders have similar areas, and as I pointed out off road 4wd vehicles too, so a generic off-road terrain area tag for leisure would work. Another analogy is leisure=skatepark. A last option which would be visualised, but which I personally dont like, is leisure=sports_centre + a sport tag. Given the wikipedia entry motorcycle_trials may be OK for the latter, but does not yet exist. The tagging mailing list is the usual place for further discussion at this point.</p>
</div>
<div id="comment-82449-info" class="comment-info">
<span class="comment-age">(01 Nov '21, 19:50)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82447-form-container" class="comment-form-container">
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


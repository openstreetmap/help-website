+++
type = "question"
title = "Solar Panels on Houses"
description = '''I would like to start adding solar panels in my neighborhood. Many houses around me have simple photovoltaic panels on the roof of their houses. These aren&#x27;t power plants, just personal power generators. What is the best practice to tagging solar panels on building&#x27;s roofs? I was thinking to draw th...'''
date = "2018-10-09T03:32:00Z"
lastmod = "2019-04-30T08:03:00Z"
weight = 66234
keywords = [ "house", "tagging", "bestpractice", "solar" ]
aliases = [ "/questions/66234" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Solar Panels on Houses](/questions/66234/solar-panels-on-houses)

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
<span id="post-66234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66234-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-66234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to start adding solar panels in my neighborhood. Many houses around me have simple photovoltaic panels on the roof of their houses. These aren't power plants, just personal power generators.</p>
<p>What is the best practice to tagging solar panels on building's roofs?</p>
<p>I was thinking to draw the outline of the solar panels and tag it as a generator.</p>
<p><img src="/upfiles/Adding_Home_Solar_Panels.png" alt="Here&#39;s a picture of what I&#39;m talking about." /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span> <span class="post-tag tag-link-solar" rel="tag" title="see questions tagged &#39;solar&#39;">solar</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Oct '18, 03:32</strong></p>
<img src="https://secure.gravatar.com/avatar/0e871659158cd1d3869f97d4e028ad17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kayla%20Colflesh&#39;s gravatar image" />
<p><span>Kayla Colflesh</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kayla Colflesh has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '18, 03:33</strong> </span></p>
</div>
</div>
<div id="comments-container-66234" class="comments-container">
&#10;</div>
<div id="comment-tools-66234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66234-form-container" class="comment-form-container">
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

<span id="66241"></span>

<div id="answer-container-66241" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66241-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-66241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kayla Colflesh has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sounds fine. Additionally you can add <code>generator:place=roof</code>.</p>
<pre><code>power=generator
generator:source=solar
generator:place=roof</code></pre>
<p>If you know whether these solar panels are used for producing electricity or hot water you can also either add <code>generator:method=photovoltaic</code> or <code>generator:method=thermal</code>. However as far as I know there is no real visible distinction between those two types, so better don't add this tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '18, 08:25</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-66241" class="comments-container">
<span id="68985"></span>
<div id="comment-68985" class="comment">
<div id="post-68985-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Some of us have changed over from <code>generator:place=roof</code> to the more conventional <code>location=roof</code>. More info on this wiki page: <a href="https://wiki.openstreetmap.org/wiki/Renewable_energy_in_the_United_Kingdom/Rooftop_Solar_PV">https://wiki.openstreetmap.org/wiki/Renewable_energy_in_the_United_Kingdom/Rooftop_Solar_PV</a></p>
</div>
<div id="comment-68985-info" class="comment-info">
<span class="comment-age">(27 Apr '19, 15:29)</span> <span class="comment-user userinfo">mcld</span>
</div>
</div>
<span id="69008"></span>
<div id="comment-69008" class="comment">
<div id="post-69008-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> In most cases I think it's possible to tell them apart. Thermal installations are usually smaller, and darker on imagery. They may also be older and therefore detectable by comparing imagery layers. With good imagery or a ground survey one may detect piping connecting to the internal water system. Solar PV are usually larger arrays of fixed size modules, modern ones being recognisable by a pale surround in imagery. Some examples in my recent blog post: <a href="https://sk53-osm.blogspot.com/2019/03/mapping-roof-top-solar-panels.html.">https://sk53-osm.blogspot.com/2019/03/mapping-roof-top-solar-panels.html.</a> I have since collected many more ground level images of Solar PV &amp; will be posting those soon.</p>
</div>
<div id="comment-69008-info" class="comment-info">
<span class="comment-age">(29 Apr '19, 16:59)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="69015"></span>
<div id="comment-69015" class="comment">
<div id="post-69015-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> Thanks for your explanations :)</p>
</div>
<div id="comment-69015-info" class="comment-info">
<span class="comment-age">(30 Apr '19, 08:03)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66241-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68984"></span>

<div id="answer-container-68984" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68984-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't you think it's personnal / private data ? I wonder if we should map these photovoltaic generators. I would love to but notre sûre if it's a good idea ...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '19, 15:22</strong></p>
<img src="https://secure.gravatar.com/avatar/41fbeaf2b79a70fc8e8985ee61ef0563?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mawy33&#39;s gravatar image" />
<p><span>mawy33</span><br />
<span class="score" title="11 reputation points">11</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mawy33 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68984" class="comments-container">
<span id="68986"></span>
<div id="comment-68986" class="comment">
<div id="post-68986-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If the info is being added from aerial imagery or from what is visible in surveys on the public street, then it must be just as non-personal as the outline of a building, surely?</p>
</div>
<div id="comment-68986-info" class="comment-info">
<span class="comment-age">(27 Apr '19, 15:31)</span> <span class="comment-user userinfo">mcld</span>
</div>
</div>
<span id="68991"></span>
<div id="comment-68991" class="comment">
<div id="post-68991-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi scai, is not there some thickness visible measurement on those panels. The termal ones are thicker due to the structure inside. A local survey would show it clearly.</p>
</div>
<div id="comment-68991-info" class="comment-info">
<span class="comment-age">(28 Apr '19, 14:52)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-68984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68984-form-container" class="comment-form-container">
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


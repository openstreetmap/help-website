+++
type = "question"
title = "OSM-Inspector, View Multipolygon, touching-inner-rings: are these errors or what is it that osm-inspector wants to tell us?"
description = '''I use osm-inspector not only to verify my own work but to correct that of other contributors if they are within my areas of interest. I far as I understand the Multipolygon instructions touching-inner-rings are allowed in OSM in a multipolygon contruction: See https://wiki.openstreetmap.org/wiki/Rela...'''
date = "2012-04-29T10:50:00Z"
lastmod = "2012-05-03T06:43:00Z"
weight = 12416
keywords = [ "touching-inner-rings", "osminspector", "multipolygon" ]
aliases = [ "/questions/12416" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM-Inspector, View Multipolygon, touching-inner-rings: are these errors or what is it that osm-inspector wants to tell us?](/questions/12416/osm-inspector-view-multipolygon-touching-inner-rings-are-these-errors-or-what-is-it-that-osm-inspector-wants-to-tell-us)

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
<span id="post-12416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12416-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use osm-inspector not only to verify my own work but to correct that of other contributors if they are within my areas of interest.</p>
<p>I far as I understand the Multipolygon instructions touching-inner-rings are allowed in OSM in a multipolygon contruction: See <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Touching_inner_rings">https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Touching_inner_rings</a></p>
<p>However the osm-inspector displays touching-inner-rings with the comment <code>[broken/lost image here]</code></p>
<p>Are these then errors and if not what is the osmi trying to tell me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-touching-inner-rings" rel="tag" title="see questions tagged &#39;touching-inner-rings&#39;">touching-inner-rings</span> <span class="post-tag tag-link-osminspector" rel="tag" title="see questions tagged &#39;osminspector&#39;">osminspector</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '12, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/cd4569f9fa1aac11eb6b19d6de309ea6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcp&#39;s gravatar image" />
<p><span>dcp</span><br />
<span class="score" title="721 reputation points">721</span><span title="37 badges"><span class="badge1">●</span><span class="badgecount">37</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Sep '15, 06:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-12416" class="comments-container">
&#10;</div>
<div id="comment-tools-12416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12416-form-container" class="comment-form-container">
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

<span id="12417"></span>

<div id="answer-container-12417" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12417-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Touching inner rings are a violation of the OGC "Simple Features" specification and therefore some programs that process OSM data might have a problem with that, and discard the polygon that has touching inner rings.</p>
<p>The standard OSM rendering process that is based on an osm2pgsql import of OSM data into a PostGIS database has no problems with touching inner rings. You can switch off the "touching inner rings" layer in OSMI if you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '12, 11:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Apr '12, 10:57</strong> </span></p>
</div>
</div>
<div id="comments-container-12417" class="comments-container">
<span id="12424"></span>
<div id="comment-12424" class="comment">
<div id="post-12424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank-you Frederik for the prompt reply. I know I can switch it off but that is not what disturbs me.</p>
<p>I understand now that the <em>errormsg</em> is not an error at all and it begs the question <strong>Why is it flaged?</strong>. Isn't this <em>errormsg</em> redundant, i.e. <strong>what purpose does it serve?</strong></p>
<p>If the <em>errormsg</em> "touching-inner-rings" is irrelevant, <strong>how many other OSMI-*errormsg</strong>* are also irrelevant?</p>
</div>
<div id="comment-12424-info" class="comment-info">
<span class="comment-age">(29 Apr '12, 14:03)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
<span id="12451"></span>
<div id="comment-12451" class="comment">
<div id="post-12451-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The OSM Inspector doesn't only show errors. It shows different "views" of the OSM data. It is your job to interpret those views and decide what to fix and how to fix it. The field called "errormsg" is a bit of a misnomer, just think of it as "description" or so.</p>
</div>
<div id="comment-12451-info" class="comment-info">
<span class="comment-age">(30 Apr '12, 10:52)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-12417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12417-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12473"></span>

<div id="answer-container-12473" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12473-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In my opinion, dcp correctly concludes that a "touching inner rings" case is not an error (I would avoid "redundant", not enough strong). Even refering to "some programs ... might have a problem ..." is confusing if we accept the often used OSM statement "we are not tagging for renderers...". Most programs will today easily handle the referd "touching inner rings" case (and much more complicated that apears in OSM area classes).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '12, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-12473" class="comments-container">
<span id="12517"></span>
<div id="comment-12517" class="comment">
<div id="post-12517-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I like your point: "we are not tagging for the renderers".</p>
<p>I would still like to know how many other errormsg flags are also irrelevant as I have not only been falsely "correcting for OSMI" but I have also contacted others contributers citing OSMI and erroneously pointing out their errors.</p>
<p>This is not encouraging!</p>
</div>
<div id="comment-12517-info" class="comment-info">
<span class="comment-age">(03 May '12, 06:43)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
</div>
<div id="comment-tools-12473" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12473-form-container" class="comment-form-container">
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


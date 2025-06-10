+++
type = "question"
title = "Adding name tags in &quot;unknown&quot; languages"
description = '''I&#x27;ve recently started mapping in Russia&#x27;s North Caucasus. Alongside Russian, there are hundreds of small languages spoken, many of them also being a second official language in some areas.  One example is the Abasa language. It has 45.000 speakers and is an official language in Abazinsky District. I...'''
date = "2014-10-28T10:30:00Z"
lastmod = "2014-10-28T13:37:00Z"
weight = 38039
keywords = [ "name", "localization" ]
aliases = [ "/questions/38039" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Adding name tags in "unknown" languages](/questions/38039/adding-name-tags-in-unknown-languages)

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
<span id="post-38039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38039-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've recently started mapping in Russia's North Caucasus. Alongside Russian, there are hundreds of small languages spoken, many of them also being a second official language in some areas.</p>
<p>One example is the Abasa language. It has 45.000 speakers and is an official language in Abazinsky District. I now want to add Abasa names in this district. However, when I try to add name tags in the language (in OSM's iD editor), I cannot select it from the list of languages. The language is not in the list. Can I still add a name in Abasa?</p>
<p>This is just an example, there are many other small languages that don't appear as a choice in OSM's web editor.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-localization" rel="tag" title="see questions tagged &#39;localization&#39;">localization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '14, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/9b1b4e90f4146bc02ab2da5df7df202d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maturi0n&#39;s gravatar image" />
<p><span>Maturi0n</span><br />
<span class="score" title="44 reputation points">44</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maturi0n has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Oct '14, 10:33</strong> </span></p>
</div>
</div>
<div id="comments-container-38039" class="comments-container">
&#10;</div>
<div id="comment-tools-38039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38039-form-container" class="comment-form-container">
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

<span id="38040"></span>

<div id="answer-container-38040" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38040-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-38040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM allows you to add any properties to objects; we call that "tags". For example, a commercial building would receive the tag <code>building=commercial</code>. Some of these tags are available as presets in the editors but not all of them are. (There's over 53,000 distinct keys, that's the bit to the left of the equal sign, in the database. You wouldn't want an editor that shows them all in a drop-down!)</p>
<p>ID allows the adding of custom tags. Click the "+" button under "all tags", and enter "name:xx" as the key, and the name in language xx as the value. ("xx" here stands for the ISO language code of the language in question.)</p>
<p>Please, however, refrain from adding translations as names. For example, the "Pont Neuf" in Paris is <em>not</em> called the "New Bridge" in English, so it should not have a "name:en=New Bridge" tag. Only use the name tag when something really has an independent name in another language, never for mere translations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '14, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-38040" class="comments-container">
<span id="38048"></span>
<div id="comment-38048" class="comment">
<div id="post-38048-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Most common languages are included in the ISO 639-1 two-letter codes. Some less widely spoken languages will only be in the ISO 639-3 three letter codes. For these, see <a href="http://en.wikipedia.org/wiki/List_of_ISO_639-3_codes">http://en.wikipedia.org/wiki/List_of_ISO_639-3_codes</a> Looks like the code for Abasa (aka Abaza) is abq. <a href="http://en.wikipedia.org/wiki/Abaza_language">http://en.wikipedia.org/wiki/Abaza_language</a></p>
</div>
<div id="comment-38048-info" class="comment-info">
<span class="comment-age">(28 Oct '14, 13:37)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-38040" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38040-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38042"></span>

<div id="answer-container-38042" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38042-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi MaturiOn, remember the basic rule of OSM tag what’s there. So if there’s a road- or name sign alongside the road in a bilingual area, you’re allowed to use that name and tag it accordingly. Take a look here 2 names on one shield <a href="https://www.google.nl/maps/@53.0308013,5.692169,3a,90y,102.69h,76.7t/data=!3m4!1e1!3m2!1sGtbNDRSZwYg_BkFfmTBM_g!2e0">https://www.google.nl/maps/@53.0308013,5.692169,3a,90y,102.69h,76.7t/data=!3m4!1e1!3m2!1sGtbNDRSZwYg_BkFfmTBM_g!2e0</a> And the community written as Sneek is also known as Snits, the area has Frisk as language and they have their own Wiki pages <a href="http://fy.wikipedia.org/wiki/Haadside">http://fy.wikipedia.org/wiki/Haadside</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '14, 11:56</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-38042" class="comments-container">
&#10;</div>
<div id="comment-tools-38042" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38042-form-container" class="comment-form-container">
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


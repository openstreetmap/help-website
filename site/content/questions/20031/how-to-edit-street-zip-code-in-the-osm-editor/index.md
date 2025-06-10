+++
type = "question"
title = "How to edit street zip code in the OSM editor"
description = '''Is there a way to add a zip code to streets using the OSM editor?'''
date = "2013-02-18T20:15:00Z"
lastmod = "2013-04-17T14:33:00Z"
weight = 20031
keywords = [ "editing", "osm" ]
aliases = [ "/questions/20031" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to edit street zip code in the OSM editor](/questions/20031/how-to-edit-street-zip-code-in-the-osm-editor)

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
<span id="post-20031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to add a zip code to streets using the OSM editor?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '13, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/dc06a3de85eb8aa3a8331e85c1390a79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gabriel_casado&#39;s gravatar image" />
<p><span>gabriel_casado</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gabriel_casado has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20031" class="comments-container">
<span id="20034"></span>
<div id="comment-20034" class="comment">
<div id="post-20034-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>similar question <a href="https://help.openstreetmap.org/questions/6896/zip-codes-and-associated-areas">https://help.openstreetmap.org/questions/6896/zip-codes-and-associated-areas</a> if you search these questions you will find more info .. try zip code or post code</p>
</div>
<div id="comment-20034-info" class="comment-info">
<span class="comment-age">(18 Feb '13, 21:19)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-20031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20031-form-container" class="comment-form-container">
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

<span id="21624"></span>

<div id="answer-container-21624" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21624-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the online editor Potlatch many POIs have an Address tab (usually third from left) which enables you to input address information. One of the fields is "Postcode:" which is also used for Zip Codes. This populates the <code>addr:postcode</code> tag.</p>
<p>If this option is not available then you can switch to Advanced Edit mode (option of bottom of POI panel) and directly add the <code>addr:postcode</code> tag and its value.</p>
<p>The Java editor JOSM has a preset for adding address information under its <code>Presets|Annotation</code> menu</p>
<p>Note that post code is not only British English, the OSM standard, but corresponds better than Zip Code with the name in other languages.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '13, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-21624" class="comments-container">
&#10;</div>
<div id="comment-tools-21624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21624-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20035"></span>

<div id="answer-container-20035" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20035-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="http://wiki.openstreetmap.org/wiki/Key:addr">http://wiki.openstreetmap.org/wiki/Key:addr</a> and <a href="http://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema#Tags">http://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema#Tags</a> for the tags that are in use (at least in germany, but applicable worldwide)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '13, 21:40</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Feb '13, 21:43</strong> </span></p>
</div>
</div>
<div id="comments-container-20035" class="comments-container">
&#10;</div>
<div id="comment-tools-20035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20035-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20039"></span>

<div id="answer-container-20039" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20039-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="http://wiki.openstreetmap.org/wiki/Key:postal_code">postal_code=*</a> to associate a street with a zip code. But <a href="http://wiki.openstreetmap.org/wiki/Key:addr">individual addresses</a> are preferred, as gormo already pointed out.</p>
<p>/al</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '13, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5501080a7333d6383d6c545f076eaeba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_al&#39;s gravatar image" />
<p><span>_al</span><br />
<span class="score" title="860 reputation points">860</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_al has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-20039" class="comments-container">
&#10;</div>
<div id="comment-tools-20039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20039-form-container" class="comment-form-container">
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


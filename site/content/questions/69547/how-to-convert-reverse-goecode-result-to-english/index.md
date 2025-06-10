+++
type = "question"
title = "how to convert reverse goecode result to english ?"
description = '''My reverse geocode result contains some of sinhalese language. I want to get rid of that and want completely English result to be dispalyed. how should that be done?'''
date = "2019-06-10T10:58:00Z"
lastmod = "2019-06-10T11:58:00Z"
weight = 69547
keywords = [ "reversegeocoding", "nodejs" ]
aliases = [ "/questions/69547" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to convert reverse goecode result to english ?](/questions/69547/how-to-convert-reverse-goecode-result-to-english)

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
<span id="post-69547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69547-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My reverse geocode result contains some of sinhalese language. I want to get rid of that and want completely English result to be dispalyed. how should that be done?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nodejs" rel="tag" title="see questions tagged &#39;nodejs&#39;">nodejs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jun '19, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f56e873c0a39225fe081ca6565f8632e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="charuUmesh&#39;s gravatar image" />
<p><span>charuUmesh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="charuUmesh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jun '19, 10:59</strong> </span></p>
</div>
</div>
<div id="comments-container-69547" class="comments-container">
&#10;</div>
<div id="comment-tools-69547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69547-form-container" class="comment-form-container">
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

<span id="69549"></span>

<div id="answer-container-69549" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69549-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Add &amp;accept-language=en to the API request URL.</p>
<p>By default Nominatim returns the value of the <code>name</code> tag, e.g. for <a href="https://www.openstreetmap.org/relation/5337946">https://www.openstreetmap.org/relation/5337946</a> that is මාතර දිස්ත්‍රික්කය. If you set &amp;accept-language=en then Nominatim first looks at the <code>name:en</code> tag.</p>
<p><a href="https://nominatim.openstreetmap.org/reverse.php?format=json&amp;lat=5.973857676873632&amp;lon=80.54088463153965">https://nominatim.openstreetmap.org/reverse.php?format=json&amp;lat=5.973857676873632&amp;lon=80.54088463153965</a></p>
<p><code>"address": { "suburb": "Welegoda", "state_district": "මාතර දිස්ත්‍රික්කය", "state": "දකුණු පළාත", "postcode": "81050", "country": "ශ්‍රී ලංකාව இலங்கை", "country_code": "lk" },</code></p>
<p><a href="https://nominatim.openstreetmap.org/reverse.php?format=json&amp;lat=5.973857676873632&amp;lon=80.54088463153965&amp;accept-language=en">https://nominatim.openstreetmap.org/reverse.php?format=json&amp;lat=5.973857676873632&amp;lon=80.54088463153965&amp;accept-language=en</a></p>
<p><code>"address": { "suburb": "Welegoda", "state_district": "Matara District", "state": "Southern Province", "postcode": "81050", "country": "Sri Lanka", "country_code": "lk" },</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jun '19, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-69549" class="comments-container">
&#10;</div>
<div id="comment-tools-69549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69549-form-container" class="comment-form-container">
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


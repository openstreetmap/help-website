+++
type = "question"
title = "How would I go about finding all objects with the &#x27;fixme&#x27; key within an area?"
description = '''This is specific application of my question on searching for keys and any key values (as opposed to just names) from a map. I though I would ask it both ways. Maybe someone has a good workflow for looking for things to do (e.g., &#x27;fixme&#x27;) within an area. Either from the View or Potlatch 1/2 would be ...'''
date = "2011-02-10T19:32:00Z"
lastmod = "2011-02-10T21:59:00Z"
weight = 2903
keywords = [ "search", "key", "fixup" ]
aliases = [ "/questions/2903" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How would I go about finding all objects with the 'fixme' key within an area?](/questions/2903/how-would-i-go-about-finding-all-objects-with-the-fixme-key-within-an-area)

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
<span id="post-2903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2903-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is specific application of my question on searching for keys and any key values (as opposed to just names) from a map. I though I would ask it both ways. Maybe someone has a good workflow for looking for things to do (e.g., 'fixme') within an area.</p>
<p>Either from the View or Potlatch 1/2 would be fine.</p>
<p>I realize I could use XAPI, but that method leaves a few too many hoops jump through: I have to calculate the "box" query parameter and then open the result in JOSM, which I currently don't use.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span> <span class="post-tag tag-link-fixup" rel="tag" title="see questions tagged &#39;fixup&#39;">fixup</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '11, 19:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '11, 06:47</strong> </span></p>
</div>
</div>
<div id="comments-container-2903" class="comments-container">
&#10;</div>
<div id="comment-tools-2903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2903-form-container" class="comment-form-container">
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

<span id="2906"></span>

<div id="answer-container-2906" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2906-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try the <a href="http://tools.geofabrik.de/osmi/">OSM Inspector</a> - a third party tool that shows all kinds of problem reports about OSM data. One of these views shows various tagging problems (likely misspelled tags, empty values etc), and also includes highlighting of all FIXME objects. Here's a permaling for the <a href="http://tools.geofabrik.de/osmi/?view=tagging&amp;lon=-82.43335&amp;lat=28.00283&amp;zoom=12&amp;overlays=fixmes_on_nodes,fixmes_on_ways">Tampa, Florida area</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '11, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '11, 21:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span></p>
</div>
</div>
<div id="comments-container-2906" class="comments-container">
<span id="2918"></span>
<div id="comment-2918" class="comment">
<div id="post-2918-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks great, thanks. Does it not look for lower case "fixme"? I see a few FIXME objects, but no fixme (and I know there are some).</p>
</div>
<div id="comment-2918-info" class="comment-info">
<span class="comment-age">(10 Feb '11, 21:59)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-2906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2906-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2907"></span>

<div id="answer-container-2907" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2907-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An alternative to OSM Inspector is <a href="http://keepright.ipax.at/">Keep Right</a>.</p>
<p>To be honest it does not let you search for any key or any values, but there is a FIXME preset together with a lot of other checks. Those error checks will probably keep you busy a looong time before you have corrected all of them in your area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '11, 20:46</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-2907" class="comments-container">
&#10;</div>
<div id="comment-tools-2907" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2907-form-container" class="comment-form-container">
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


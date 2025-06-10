+++
type = "question"
title = "How can i download old points of interest data from openstreetmap?"
description = '''I am looking for a way to download points of interest data for London from 2007. Is there a way to access archived data? is this available with someone who might have downloaded this data back in 2006/07/08 ? '''
date = "2018-02-05T20:47:00Z"
lastmod = "2018-02-05T22:45:00Z"
weight = 61969
keywords = [ "download", "historic", "export", "poi" ]
aliases = [ "/questions/61969" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can i download old points of interest data from openstreetmap?](/questions/61969/how-can-i-download-old-points-of-interest-data-from-openstreetmap)

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
<span id="post-61969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61969-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for a way to download points of interest data for London from 2007. Is there a way to access archived data? is this available with someone who might have downloaded this data back in 2006/07/08 ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-historic" rel="tag" title="see questions tagged &#39;historic&#39;">historic</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '18, 20:47</strong></p>
<img src="https://secure.gravatar.com/avatar/138c8c4a42bde49fb02554314454127f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djohn&#39;s gravatar image" />
<p><span>djohn</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djohn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Feb '18, 21:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-61969" class="comments-container">
&#10;</div>
<div id="comment-tools-61969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61969-form-container" class="comment-form-container">
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

<span id="61973"></span>

<div id="answer-container-61973" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61973-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using a "history" file will get you there but you will not see the data that was removed during the license change. A slightly more complete approach is using one of the very old "planet files" from <a href="http://planet.openstreetmap.org/cc-by-sa/">http://planet.openstreetmap.org/cc-by-sa/</a> and processing that. These files will have an older data format and you'll have to download version 0.35 of Osmosis to process them.</p>
<p>However, whatever way you choose, this will <em>not</em> give you any indicator on how many POIs there were in London at the time - just how many POIs OSM knew about! So if you intend to compute something like "the number of pubs in London has changed so-and-so over the last 10 years" then forget OSM as a data source. OSM's coverage of POIs in London in 2007 was patchy at best - counting, just to give an example, about 900 hotel/restaurant/pub POIs compared to today's 21,000.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '18, 22:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-61973" class="comments-container">
&#10;</div>
<div id="comment-tools-61973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61973-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61972"></span>

<div id="answer-container-61972" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61972-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use osmium-tool along with a full history file (<code>*.osh.pbf</code>) of UK (country extracts are available from Geofabrik) to make a normal non-history OSM file "snapshot" at certain timestamp. Osmium-tool can also clip it to London area and filter POI you want (e.g. <code>shop=*</code>, <code>amenity=*</code>) so you could load it in JOSM, for instance - or whatever can read .osm or .pbf files.</p>
<p>(Sorry I have no time to explain each step, but the above way will certainly work. ;-) )</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '18, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/b68bcf9f1c4a7921aeee1bb35b0e2784?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RicoElectrico&#39;s gravatar image" />
<p><span>RicoElectrico</span><br />
<span class="score" title="371 reputation points">371</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RicoElectrico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61972" class="comments-container">
&#10;</div>
<div id="comment-tools-61972" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61972-form-container" class="comment-form-container">
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


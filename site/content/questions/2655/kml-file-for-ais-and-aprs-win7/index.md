+++
type = "question"
title = "KML-file for AIS and APRS (Win7)"
description = '''How can I get a KML-file i.e. for AIS (Automatic Identification System) or APRS (Amateur Packet Radio System) ? Thanks in advance for your answer. Horst, DK9XH'''
date = "2011-02-01T13:28:00Z"
lastmod = "2015-03-12T08:51:00Z"
weight = 2655
keywords = [ "kml", "aprs", "ais" ]
aliases = [ "/questions/2655" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [KML-file for AIS and APRS (Win7)](/questions/2655/kml-file-for-ais-and-aprs-win7)

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
<span id="post-2655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2655-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I get a KML-file i.e. for AIS (Automatic Identification System) or APRS (Amateur Packet Radio System) ?</p>
<p>Thanks in advance for your answer.</p>
<p>Horst, DK9XH</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-aprs" rel="tag" title="see questions tagged &#39;aprs&#39;">aprs</span> <span class="post-tag tag-link-ais" rel="tag" title="see questions tagged &#39;ais&#39;">ais</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '11, 13:28</strong></p>
<img src="https://secure.gravatar.com/avatar/abb2a7ea3783ba759b783db7d36bd8c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Horst&#39;s gravatar image" />
<p><span>Horst</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Horst has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Feb '11, 22:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-2655" class="comments-container">
<span id="2659"></span>
<div id="comment-2659" class="comment">
<div id="post-2659-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not familiar with using KML files together with AIS and APRS, but I know that the gpsbabel command has options for KML. Maybe something like this: (untested)</p>
<p>gpsbabel -i gpx -o kml -f myinfile.gpx -F myoutfile.kml</p>
<p>There are some further options to gpsbabel specified in the manual</p>
<p>What kind of information is it you would like to export from OSM to AIS and APRS?</p>
<p>73 de gnurk</p>
</div>
<div id="comment-2659-info" class="comment-info">
<span class="comment-age">(01 Feb '11, 15:11)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
</div>
<div id="comment-tools-2655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2655-form-container" class="comment-form-container">
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

<span id="41652"></span>

<div id="answer-container-41652" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41652-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can request OSM on <a href="http://overpass-turbo.eu/">overpass-turbo</a> and export the data as KML.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '15, 08:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-41652" class="comments-container">
&#10;</div>
<div id="comment-tools-41652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41652-form-container" class="comment-form-container">
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


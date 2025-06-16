+++
type = "question"
title = "Overpass query with CSV export"
description = '''I have currently the following query: http://overpass-api.de/api/interpreter?data=(node%22highway%22;way(bn);%3E;);(.;rel(bn););(.;rel(bw););._;out; I would like to retrieve the data in an csv output format. I found out that I need to add this to the query data=[out:format]... Works like a charm for...'''
date = "2015-03-30T13:56:00Z"
lastmod = "2015-03-30T14:05:00Z"
weight = 42020
keywords = [ "overpassapi", "csv" ]
aliases = [ "/questions/42020" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass query with CSV export](/questions/42020/overpass-query-with-csv-export)

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
<span id="post-42020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42020-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have currently the following query: <a href="http://overpass-api.de/api/interpreter?data=(node">http://overpass-api.de/api/interpreter?data=(node</a><a href="49.49941925,10.899506193259619,49.5385736,10.972935156740382">%22highway%22</a>;way(bn);%3E;);(.<em>;rel(bn););(.</em>;rel(bw););._;out;</p>
<p>I would like to retrieve the data in an csv output format. I found out that I need to add this to the query data=[out:format]... Works like a charm for JSON but not for CSV. What am I doing wrong?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '15, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/36e485e2bc86e1d7e70d8515a253aeda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Linda&#39;s gravatar image" />
<p><span>Linda</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Linda has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42020" class="comments-container">
&#10;</div>
<div id="comment-tools-42020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42020-form-container" class="comment-form-container">
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

<span id="42021"></span>

<div id="answer-container-42021" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42021-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>[out:csv] alone will not work. You need to specify exactly, which fields should be included in the response. Please check out the documentation on the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Output_Format_.28out.29">wiki page</a> as pointed out earlier today. Also, you can test your query in <a href="http://overpass-turbo.eu">http://overpass-turbo.eu</a> , which may be more convenient.</p>
<p>Can you elaborate a bit more, what you're trying to do?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '15, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Mar '15, 14:10</strong> </span></p>
</div>
</div>
<div id="comments-container-42021" class="comments-container">
&#10;</div>
<div id="comment-tools-42021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42021-form-container" class="comment-form-container">
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


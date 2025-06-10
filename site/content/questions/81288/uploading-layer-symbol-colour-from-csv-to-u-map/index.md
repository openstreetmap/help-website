+++
type = "question"
title = "Uploading layer, symbol, colour from CSV to u-map"
description = '''I have a list of stuff in a spreadsheet that I want to send periodically to u-map. I can get different symbols for different types of POI by splitting the data into several chunks and sending each group to a different layer, but that&#x27;s a fuiter. Can I specify layers, colours symbols in the CSV?'''
date = "2021-08-12T15:05:00Z"
lastmod = "2021-08-19T13:04:00Z"
weight = 81288
keywords = [ "csv", "u-map", "upload" ]
aliases = [ "/questions/81288" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Uploading layer, symbol, colour from CSV to u-map](/questions/81288/uploading-layer-symbol-colour-from-csv-to-u-map)

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
<span id="post-81288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81288-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a list of stuff in a spreadsheet that I want to send periodically to u-map. I can get different symbols for different types of POI by splitting the data into several chunks and sending each group to a different layer, but that's a fuiter. Can I specify layers, colours symbols in the CSV?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-u-map" rel="tag" title="see questions tagged &#39;u-map&#39;">u-map</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '21, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/bcf52aade252d57aa782ee61b38197f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David_J_Edge&#39;s gravatar image" />
<p><span>David_J_Edge</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David_J_Edge has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81288" class="comments-container">
&#10;</div>
<div id="comment-tools-81288" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81288-form-container" class="comment-form-container">
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

<span id="81296"></span>

<div id="answer-container-81296" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81296-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think umap can interpret the csv as you would like.</p>
<p>But there are various import/export functions, with gpx, kml and umap own format (based on geojson). Maybe you can convert your csv to one of these format, I know that the kml export keep the styling options of the object, so I guess the import function should do as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '21, 16:41</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-81296" class="comments-container">
<span id="81322"></span>
<div id="comment-81322" class="comment">
<div id="post-81322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks both</p>
<p>My U-Map now has two layers; "uploaded" w layerhich is always replaced and "manual" where I add items directly to a map. What I need to develop then is either a painless way of parsing the spreadsheet to kml and ideally decrypting the kml of the "manual" back into the spreadsheet. I'm wondering if there is some tool that I can use to replace the spreadsheet and edit my tabular data (manual edits) and just spit it out as geojson, or whatever. I can't believe I am the only person who has wanted to produce a spatial representation of a table of data overlayed on a map.</p>
</div>
<div id="comment-81322-info" class="comment-info">
<span class="comment-age">(16 Aug '21, 11:07)</span> <span class="comment-user userinfo">David_J_Edge</span>
</div>
</div>
<span id="81366"></span>
<div id="comment-81366" class="comment">
<div id="post-81366-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess QGis could fit your bill, there a tabular edit mode. But it's not so easy to master.</p>
<p>Otherwise, depending your exact needs, you could get rid of your spreadsheet altogether, and let your user edit the data directly. In UMap it is not easy, but there are other software, I think mainly of <a href="https://gitlab.com/Seballot/gogocarto">GogoCarto</a> which is made for collaborative editing of geographical data, with validation, admin rights, and so on. Really easy to use for the basic user.</p>
</div>
<div id="comment-81366-info" class="comment-info">
<span class="comment-age">(19 Aug '21, 13:04)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-81296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81296-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81299"></span>

<div id="answer-container-81299" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81299-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think you can split a file between layers. But according to the help texts in the edit sidebar you should be able to change the icon by supplying parameters from the file into the symbol URL. If you try to edit the icon of a node there is a possibility to add a URL instead of choosing a icon. The help text says you can use something like <a href="http://myserver.org/images/%7Bname%7D.png"><code>http://myserver.org/images/{name}.png</code></a> there. I've never tried this.</p>
<p>There is an open <a href="https://github.com/umap-project/umap/issues/858">Github issue</a> requesting a parameter for the color.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '21, 21:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-81299" class="comments-container">
&#10;</div>
<div id="comment-tools-81299" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81299-form-container" class="comment-form-container">
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


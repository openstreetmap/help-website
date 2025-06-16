+++
type = "question"
title = "JOSM: Resuming interrupted upload of .osm file"
description = '''Upload of my .osm file was interrupted (reason unknown) in JOSM and only some nodes from that file were uploaded. Changeset was closed and instance of JOSM finished. What is the easiest way to resume the original upload? I preffer ammending to the data that were already uploaded to making a revert a...'''
date = "2012-03-10T14:44:00Z"
lastmod = "2012-12-19T14:37:00Z"
weight = 11096
keywords = [ "josm", "revert", "upload", ".osm" ]
aliases = [ "/questions/11096" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM: Resuming interrupted upload of .osm file](/questions/11096/josm-resuming-interrupted-upload-of-osm-file)

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
<span id="post-11096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11096-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Upload of my .osm file was interrupted (reason unknown) in JOSM and only some nodes from that file were uploaded. Changeset was closed and instance of JOSM finished. What is the easiest way to resume the original upload? I preffer ammending to the data that were already uploaded to making a revert and a whole new upload again.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '12, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-11096" class="comments-container">
&#10;</div>
<div id="comment-tools-11096" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11096-form-container" class="comment-form-container">
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

<span id="11106"></span>

<div id="answer-container-11106" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11106-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It depends. First of all check the list of your <a href="https://www.openstreetmap.org/user/Kozuch/edits">edits</a> to see what really got uploaded. In the default setting, an upload in JOSM is <strong>all or nothing</strong>, i.e. either the upload is complete or the changeset is empty. If, like you say, the upload is partial, this means you uploaded in chunked mode. Now there are 2 possibilities:</p>
<p>Either JOSM got the server response from the last successfully uploaded chunk, or it missed this response. In the first case, everything is fine and you can just try to upload again. In the second case you have a problem:</p>
<p>There will be a number of objects in your dataset that are already uploaded, but JOSM does not know this and will try to upload them again. If all these objects are new, the upload will succeed and create lots of duplicates. If one of the objects is modified or deleted, the server will refuse the upload due to version mismatch. Now, what you can do is <em>File &gt; Update data</em>.</p>
<p>Afterwards, you may have plenty of duplicates in your dataset. Validator helps to find and clean these up. When everything is in order, you can proceed with the upload.</p>
<p>Some tips:</p>
<ul>
<li>Don't use chunked upload, unless you have a good reason. This way you avoid partial upload mess.</li>
<li>Save often. If you have saved the state just before the upload, you can always revert and try again.</li>
<li>If everything fails, use <em>File &gt; Upload selection</em> to get at least some parts of your work on the server.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '12, 23:14</strong></p>
<img src="https://secure.gravatar.com/avatar/766400faa78a96dce84422cdb20779d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bastik&#39;s gravatar image" />
<p><span>bastik</span><br />
<span class="score" title="651 reputation points">651</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bastik has 5 accepted answers">41%</span></p>
</div>
</div>
<div id="comments-container-11106" class="comments-container">
<span id="11397"></span>
<div id="comment-11397" class="comment">
<div id="post-11397-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The file had 12000 nodes, JOSM was not able to complete it as a whole for several times...</p>
</div>
<div id="comment-11397-info" class="comment-info">
<span class="comment-age">(21 Mar '12, 20:36)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
<span id="18591"></span>
<div id="comment-18591" class="comment">
<div id="post-18591-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In JOSM, you can upload data in smaller chunks, you can determine chunk size in the advanced tab in the upload dialog(below the comment box. for slower connection you can use chunk size of 50, for good connections 1000. this way this way if you get stuck in the middle, it will takes less time afterwards as the previous chunks will be already uploaded</p>
</div>
<div id="comment-18591-info" class="comment-info">
<span class="comment-age">(19 Dec '12, 09:41)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
<span id="18608"></span>
<div id="comment-18608" class="comment">
<div id="post-18608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well after all, I realized JOSM upload works best for me with super small chunks, that means splitting any upload to pieces of about 5 or 10 objects. While it may generate more load for the server, I have really not found another working solution here.</p>
</div>
<div id="comment-18608-info" class="comment-info">
<span class="comment-age">(19 Dec '12, 14:37)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
</div>
<div id="comment-tools-11106" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11106-form-container" class="comment-form-container">
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


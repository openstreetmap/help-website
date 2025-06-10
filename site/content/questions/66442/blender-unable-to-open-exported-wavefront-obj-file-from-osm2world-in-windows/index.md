+++
type = "question"
title = "Blender unable to open exported wavefront obj-file from OSM2World in Windows"
description = '''There is a problem with exported wavefront OBJ-file from OSM2World in windows, that Blender shows an error and is unable to open the obj file. But it works good in Linux! Are there any suggestion or idea what could be the reason and perhaps any solution? '''
date = "2018-10-24T15:14:00Z"
lastmod = "2018-11-08T15:16:00Z"
weight = 66442
keywords = [ "osm2world" ]
aliases = [ "/questions/66442" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Blender unable to open exported wavefront obj-file from OSM2World in Windows](/questions/66442/blender-unable-to-open-exported-wavefront-obj-file-from-osm2world-in-windows)

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
<span id="post-66442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66442-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a problem with exported wavefront OBJ-file from OSM2World in windows, that Blender shows an error and is unable to open the obj file. But it works good in Linux! Are there any suggestion or idea what could be the reason and perhaps any solution?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2world" rel="tag" title="see questions tagged &#39;osm2world&#39;">osm2world</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '18, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/fef602ecf8e90f6593c6103096a980ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NGS92&#39;s gravatar image" />
<p><span>NGS92</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NGS92 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '18, 15:15</strong> </span></p>
</div>
</div>
<div id="comments-container-66442" class="comments-container">
<span id="66449"></span>
<div id="comment-66449" class="comment">
<div id="post-66449-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just guessing, but one thing that's different between the operating systems is file paths, so that could be a source of issues (e.g. because Blender cannot find the textures used by the model). But to properly diagnose the issue, additional information would be helpful. For example: Does Blender display any text in the error message? If so, what does it say?</p>
</div>
<div id="comment-66449-info" class="comment-info">
<span class="comment-age">(24 Oct '18, 21:28)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="66451"></span>
<div id="comment-66451" class="comment">
<div id="post-66451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><img src="https://help.openstreetmap.org/upfiles/error.png" alt="alt text" /></p>
</div>
<div id="comment-66451-info" class="comment-info">
<span class="comment-age">(24 Oct '18, 21:43)</span> <span class="comment-user userinfo">NGS92</span>
</div>
</div>
<span id="66474"></span>
<div id="comment-66474" class="comment">
<div id="post-66474-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the screenshot! It looks as if the import fails due to a number that uses a comma instead of a dot. This is relatively common programming issue, and I'll probably be able to find the bug responsible for it. But if you could provide the problematic obj and obj.mtl files (upload them somewhere, or <a href="http://osm2world.org/contact/">send me a mail</a>), that could speed things up! :)</p>
</div>
<div id="comment-66474-info" class="comment-info">
<span class="comment-age">(25 Oct '18, 22:52)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="66727"></span>
<div id="comment-66727" class="comment">
<div id="post-66727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I sent you the files via email (osm@tobias-knerr.de) on 26.10.2018 .</p>
</div>
<div id="comment-66727-info" class="comment-info">
<span class="comment-age">(08 Nov '18, 15:16)</span> <span class="comment-user userinfo">NGS92</span>
</div>
</div>
</div>
<div id="comment-tools-66442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66442-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


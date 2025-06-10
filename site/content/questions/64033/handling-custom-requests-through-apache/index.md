+++
type = "question"
title = "Handling custom requests through Apache"
description = '''I have an OSM tile server running on Ubuntu 16.04 LTS by going through the guide on the OSM website. I&#x27;m now trying to handle custom requests and use render_list to pre-render some tiles and send a single .mbtile file when the rendering is finished.  My plan right now is to make a custom Apache modu...'''
date = "2018-06-05T19:46:00Z"
lastmod = "2018-06-05T19:46:00Z"
weight = 64033
keywords = [ "apache", "render_list", "renderd", "mod_tile" ]
aliases = [ "/questions/64033" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Handling custom requests through Apache](/questions/64033/handling-custom-requests-through-apache)

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
<span id="post-64033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64033-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an OSM tile server running on Ubuntu 16.04 LTS by going through the guide on the OSM website. I'm now trying to handle custom requests and use render_list to pre-render some tiles and send a single .mbtile file when the rendering is finished.</p>
<p>My plan right now is to make a custom Apache module to handle these requests after installing mod_tile/renderd on the same Apache server. I had two questions if anyone can help:</p>
<ol>
<li>Is this a good way to go about this?</li>
<li>I've started looking into creating custom Apache modules. Could someone give a high level explanation of how mod_tile is hooked into Apache and knows to specifically handle only tile requests?</li>
</ol>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-render_list" rel="tag" title="see questions tagged &#39;render_list&#39;">render_list</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '18, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/7594614ba848fdde8ac9feb3d91253f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coderunner&#39;s gravatar image" />
<p><span>coderunner</span><br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coderunner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64033" class="comments-container">
&#10;</div>
<div id="comment-tools-64033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64033-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


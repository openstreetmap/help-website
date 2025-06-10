+++
type = "question"
title = "xapi returns two different roads for a bounding box on a specific road"
description = '''Hi all, I am trying to get the roadname for a specifi road. For this I use an xapi query with the bounding box set as small as just a point on a road (as retrieved from google maps). http://open.mapquestapi.com/xapi/api/0.6/way[highway=*][bbox=5.405231,51.466303,5.405231,51.466303] While the boundin...'''
date = "2013-05-05T01:22:00Z"
lastmod = "2013-05-06T07:43:00Z"
weight = 22102
keywords = [ "node", "xapi", "way" ]
aliases = [ "/questions/22102" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [xapi returns two different roads for a bounding box on a specific road](/questions/22102/xapi-returns-two-different-roads-for-a-bounding-box-on-a-specific-road)

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
<span id="post-22102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22102-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am trying to get the roadname for a specifi road. For this I use an xapi query with the bounding box set as small as just a point on a road (as retrieved from google maps). <a href="http://open.mapquestapi.com/xapi/api/0.6/way%5Bhighway=*%5D%5Bbbox=5.405231,51.466303,5.405231,51.466303%5D">http://open.mapquestapi.com/xapi/api/0.6/way[highway=*][bbox=5.405231,51.466303,5.405231,51.466303]</a></p>
<p>While the bounding box is on a road called N2 the result is also containing a road called A2 which is next to it.</p>
<p>Can anybody tell me what I am doing wrong here?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 May '13, 01:22</strong></p>
<img src="https://secure.gravatar.com/avatar/9da543a4155e2c5e408b566ace90025f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JLambregs&#39;s gravatar image" />
<p><span>JLambregs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JLambregs has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22102" class="comments-container">
<span id="22120"></span>
<div id="comment-22120" class="comment">
<div id="post-22120-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>you even have a third way ... a cycleway!</p>
<p>Maybe that the mapquest API is rounding the coordinates so a bigger bbox is the result?</p>
<p>Have you tried do that query at <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">http://wiki.openstreetmap.org/wiki/Overpass_API</a> ?</p>
</div>
<div id="comment-22120-info" class="comment-info">
<span class="comment-age">(05 May '13, 18:32)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="22125"></span>
<div id="comment-22125" class="comment">
<div id="post-22125-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please note also that the Mapquest API got stuck with old data from even before the license change. Maybe this is also an old and already busted bug.</p>
</div>
<div id="comment-22125-info" class="comment-info">
<span class="comment-age">(06 May '13, 07:43)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-22102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22102-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


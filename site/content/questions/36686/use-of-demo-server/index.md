+++
type = "question"
title = "Use of demo server"
description = '''I currently have the OSRM daemon running locally. I am not permitted to access this server via the Internet. I am running a demo PHP page that takes two points and returns a travel time. The php is called like this: traveltimes.php?start=26.4945,-81.8479&amp;amp;dest=26.1535,-81.8706 When I change the S...'''
date = "2014-09-08T20:08:00Z"
lastmod = "2014-09-08T20:08:00Z"
weight = 36686
keywords = [ "demo", "private_server", "osrm", "viaroute" ]
aliases = [ "/questions/36686" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Use of demo server](/questions/36686/use-of-demo-server)

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
<span id="post-36686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36686-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I currently have the OSRM daemon running locally. I am not permitted to access this server via the Internet. I am running a demo PHP page that takes two points and returns a travel time. The php is called like this: traveltimes.php?start=26.4945,-81.8479&amp;dest=26.1535,-81.8706</p>
<p>When I change the Server address and also the call to the demo address it returns a [FAILED] message. I need to be able to use my test script while travelling. What am I doing wrong?</p>
<pre><code>$ServerAddress=&quot;http://router.project-osrm.org:5000&quot;;
$url = &quot;http://router.project-osrm.org:5000/viaroute?loc=&quot;.$args[&#39;start&#39;].&quot;&amp;loc=&quot;.$args[&#39;dest&#39;];</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-demo" rel="tag" title="see questions tagged &#39;demo&#39;">demo</span> <span class="post-tag tag-link-private_server" rel="tag" title="see questions tagged &#39;private_server&#39;">private_server</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-viaroute" rel="tag" title="see questions tagged &#39;viaroute&#39;">viaroute</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '14, 20:08</strong></p>
<img src="https://secure.gravatar.com/avatar/79f57a1acef90f11c6d02bad9b3ec5aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anamealreadyinuse&#39;s gravatar image" />
<p><span>anamealready...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anamealreadyinuse has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '14, 21:14</strong> </span></p>
</div>
</div>
<div id="comments-container-36686" class="comments-container">
&#10;</div>
<div id="comment-tools-36686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36686-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


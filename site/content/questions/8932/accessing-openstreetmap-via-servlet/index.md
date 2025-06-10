+++
type = "question"
title = "accessing openstreetmap via servlet"
description = '''Hi All, I am using OSM for my application which is hosted on tomcat. Application is accessible only via https as a result of it http calls made to get tile on open e.g. :- http://tile.openstreetmap.org/3/2/1.png would fail. Since security violation ... I thought of creating a proxy via a servlet i h...'''
date = "2011-11-11T16:35:00Z"
lastmod = "2011-11-11T17:03:00Z"
weight = 8932
keywords = [ "osm", "servlet", "proxy" ]
aliases = [ "/questions/8932" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [accessing openstreetmap via servlet](/questions/8932/accessing-openstreetmap-via-servlet)

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
<span id="post-8932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8932-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I am using OSM for my application which is hosted on tomcat. Application is accessible only via https as a result of it http calls made to get tile on open e.g. :- <a href="http://tile.openstreetmap.org/3/2/1.png">http://tile.openstreetmap.org/3/2/1.png</a> would fail. Since security violation ...</p>
<p>I thought of creating a proxy via a servlet i have shown code below used in doGet ...this wont work</p>
<p>URL url = new URL("http://tile.openstreetmap.org/3/2/1.png"); BufferedImage bimg = ImageIO.read(url); response.setContentType("image/png"); OutputStream outputStream = response.getOutputStream(); ImageIO.write(bimg, "png", outputStream); outputStream.close();</p>
<p>error i get is - Caused by: java.net.SocketException: Software caused connection abort: recv failed</p>
<p>Can anyone tell me what could be an issue? I have used the same code above pointing to different site to get an image and it works just fine....</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-servlet" rel="tag" title="see questions tagged &#39;servlet&#39;">servlet</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '11, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/238a6eddc9b015e8ede9b864ecf0be3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mayank&#39;s gravatar image" />
<p><span>Mayank</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mayank has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8932" class="comments-container">
<span id="8933"></span>
<div id="comment-8933" class="comment">
<div id="post-8933-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What useragent would osm see your servlet proxy using? I don't know whether it is going to be the problem, but I think some are blocked. It might help someone who knows more about the technical aspects to answer, though.</p>
</div>
<div id="comment-8933-info" class="comment-info">
<span class="comment-age">(11 Nov '11, 16:43)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="8934"></span>
<div id="comment-8934" class="comment">
<div id="post-8934-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>actually i am not passing useragent ... let me try that and will keep u posted</p>
</div>
<div id="comment-8934-info" class="comment-info">
<span class="comment-age">(11 Nov '11, 16:48)</span> <span class="comment-user userinfo">Mayank</span>
</div>
</div>
<span id="8935"></span>
<div id="comment-8935" class="comment">
<div id="post-8935-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i happen to come across this link <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">http://wiki.openstreetmap.org/wiki/Tile_usage_policy</a></p>
<p>i tried using Alternative tile server from <a href="http://tile.openstreetmap.org/3/2/1.png">http://tile.openstreetmap.org/3/2/1.png</a> to <a href="http://a.tile.openstreetmap.org/3/2/1.png">http://a.tile.openstreetmap.org/3/2/1.png</a> and the code works... i am not sure what is going on....</p>
<p>why are the same restrictions not applied to <a href="http://a.tile">http://a.tile</a>..... as that of <a href="http://tile">http://tile</a>...</p>
<p>Any advice?</p>
</div>
<div id="comment-8935-info" class="comment-info">
<span class="comment-age">(11 Nov '11, 17:03)</span> <span class="comment-user userinfo">Mayank</span>
</div>
</div>
</div>
<div id="comment-tools-8932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8932-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


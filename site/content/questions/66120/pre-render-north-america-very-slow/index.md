+++
type = "question"
title = "pre render north america very slow"
description = '''I&#x27;m trying to pre-render the whole of North America from zoom level 6 to 18 using the below command /usr/bin/perl ./render_list_geo.pl -l 28 -n 16 -z 6 -Z 18 -x -168.8 -X -50.8 -y 23.6 -Y 71.8 -m default As per my calculations it should take around 2.8 TB disk space. The postgresql DB is on SSD driv...'''
date = "2018-10-02T07:47:00Z"
lastmod = "2018-10-12T07:49:00Z"
weight = 66120
keywords = [ "renderd", "osm", "mod_tile" ]
aliases = [ "/questions/66120" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pre render north america very slow](/questions/66120/pre-render-north-america-very-slow)

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
<span id="post-66120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66120-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to pre-render the whole of North America from zoom level 6 to 18 using the below command</p>
<p>/usr/bin/perl ./render_list_geo.pl -l 28 -n 16 -z 6 -Z 18 -x -168.8 -X -50.8 -y 23.6 -Y 71.8 -m default</p>
<p>As per my calculations it should take around 2.8 TB disk space. The postgresql DB is on SSD drives while the tiles are being stored on SAS drives. When I had imported the OSM DB, it took only 61 hours for a planet import so I think drives are quite fast.</p>
<p>The pace of pre rendering is around 40 GB per day. At this pace it will take months for the pre rendering to finish. Please suggest how it can be made faster.</p>
<p>I am not sure whats the bottleneck because the server has fast drives and has 64 GB RAM and 32 cpu cores. The disk IOs are mostly un-utilized.</p>
<p>Pre rendering from zoom 6 to 15 is finished and right now its pre rendering zoom 16. Its the pace of pre rendering that worries me.</p>
<p><a href="http://tools.geofabrik.de/calc/#type=geofabrik_standard&amp;bbox=-168.8,23.6,-50.8,71.8&amp;grid=1">http://tools.geofabrik.de/calc/#type=geofabrik_standard&amp;bbox=-168.8,23.6,-50.8,71.8&amp;grid=1</a></p>
<p>If I pre rendered the above area from zoom 6 to zoom 18 then how long would it normally take. Please forgive me if I've asked any stupid question because this is the first time I'm configuring this server and have little knowledge of it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '18, 07:47</strong></p>
<img src="https://secure.gravatar.com/avatar/df8704d2a10bf36fc9c5b79301fbd118?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="augustusj&#39;s gravatar image" />
<p><span>augustusj</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="augustusj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '18, 12:18</strong> </span></p>
</div>
</div>
<div id="comments-container-66120" class="comments-container">
<span id="66167"></span>
<div id="comment-66167" class="comment">
<div id="post-66167-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please help me with this issue</p>
</div>
<div id="comment-66167-info" class="comment-info">
<span class="comment-age">(05 Oct '18, 06:12)</span> <span class="comment-user userinfo">augustusj</span>
</div>
</div>
<span id="66178"></span>
<div id="comment-66178" class="comment">
<div id="post-66178-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Cross-posted here: <a href="https://forum.openstreetmap.org/viewtopic.php?id=63980">https://forum.openstreetmap.org/viewtopic.php?id=63980</a></p>
</div>
<div id="comment-66178-info" class="comment-info">
<span class="comment-age">(05 Oct '18, 17:39)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="66202"></span>
<div id="comment-66202" class="comment">
<div id="post-66202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes. I'm eager to get a response but nothing yet</p>
</div>
<div id="comment-66202-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 05:29)</span> <span class="comment-user userinfo">augustusj</span>
</div>
</div>
<span id="66306"></span>
<div id="comment-66306" class="comment">
<div id="post-66306-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If nobody has a solution for you and this problem is important enough to invest some money you could consider getting professional help, for example by contacting one of the companies listed at <a href="https://switch2osm.org/providers/">https://switch2osm.org/providers/</a></p>
</div>
<div id="comment-66306-info" class="comment-info">
<span class="comment-age">(12 Oct '18, 07:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66120-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


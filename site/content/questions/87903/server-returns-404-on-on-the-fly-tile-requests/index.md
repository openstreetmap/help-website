+++
type = "question"
title = "Server returns 404 on &quot;on the fly&quot; tile requests"
description = '''Built server following Switch2OSM docs for Ubuntu 22.04 Server sitting on Hyper-V Windows 2012 r2 1.8 4core 78 gig memory 2tb WD black SSD NVMe connected through 16X PCI Lane card. Full server is dedicated to OSM. Nothing else is running on it. Processor response is typically 5% Issue Successfully i...'''
date = "2023-10-13T23:36:00Z"
lastmod = "2023-10-14T21:41:00Z"
weight = 87903
keywords = [ "maptiles", "renderd", "404" ]
aliases = [ "/questions/87903" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Server returns 404 on "on the fly" tile requests](/questions/87903/server-returns-404-on-on-the-fly-tile-requests)

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
<span id="post-87903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87903-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Built server following Switch2OSM docs for Ubuntu 22.04 Server sitting on Hyper-V Windows 2012 r2 1.8 4core 78 gig memory 2tb WD black SSD NVMe connected through 16X PCI Lane card. Full server is dedicated to OSM. Nothing else is running on it. Processor response is typically 5%</p>
<p>Issue Successfully installed and pre-renderd zoom levels 0-12. When requesting those map tiles, everything works correctly. However when we request, higher zoom levels that are not pre-renderd, we constantly get 404 not found errors. Any help would be greatly appreciated.</p>
<pre><code>Oct 13 00:42:37 maps-live renderd[743]: START TILE s2o 17 23376-23383 49224-49231, age 37.16 days
Oct 13 00:42:37 maps-live renderd[743]: Rendering projected coordinates 17 23376 49224 -&gt; -12890340.450019|4984917.236649 -12887894.465114|4987363.221554 to a 8 x 8 tile
Oct 13 00:42:37 maps-live renderd[743]: Data is available now on 1 fds
Oct 13 00:42:37 maps-live renderd[743]: Got incoming connection, fd 11, number 0, total conns 1, total slots 6
Oct 13 00:42:37 maps-live renderd[743]: Data is available now on 1 fds
Oct 13 00:42:37 maps-live renderd[743]: Got incoming request with protocol version 2
Oct 13 00:42:37 maps-live renderd[743]: Got command Dirty fd(11) xml(s2o), z(17), x(23377), y(49223), mime(image/png), options()
Oct 13 00:42:37 maps-live renderd[743]: Sending NotDone response(4)
Oct 13 00:42:37 maps-live renderd[743]: Sending render cmd(4 s2o 17/23377/49223) with protocol version 2 to fd 11
Oct 13 00:42:37 maps-live renderd[743]: Data is available now on 1 fds
Oct 13 00:42:37 maps-live renderd[743]: Failed to read cmd on fd 11
Oct 13 00:42:37 maps-live renderd[743]: Connection 0, fd 11 closed, now 0 left, total slots 6
Oct 13 00:42:37 maps-live renderd[743]: START TILE s2o 17 23376-23383 49216-49223, age 37.16 days
Oct 13 00:42:37 maps-live renderd[743]: Rendering projected coordinates 17 23376 49216 -&gt; -12890340.450019|4987363.221554 -12887894.465114|4989809.206459 to a 8 x 8 tile
Oct 13 00:42:37 maps-live renderd[743]: DONE TILE s2o 16 11688-11695 24608-24615 in 3.445 seconds
Oct 13 00:42:37 maps-live renderd[743]: Creating and writing a metatile to /var/cache/renderd/tiles/s2o/16/0/38/208/162/128.meta
Oct 13 00:42:38 maps-live renderd[743]: DONE TILE s2o 17 23376-23383 49224-49231 in 1.523 seconds
Oct 13 00:42:38 maps-live renderd[743]: Creating and writing a metatile to /var/cache/renderd/tiles/s2o/17/0/92/176/84/8.meta
Oct 13 00:42:39 maps-live renderd[743]: DONE TILE s2o 17 23376-23383 49216-49223 in 1.761 seconds
Oct 13 00:42:39 maps-live renderd[743]: Creating and writing a metatile to /var/cache/renderd/tiles/s2o/17/0/92/176/84/0.meta
Oct 13 00:42:45 maps-live hv_kvp_daemon[2161]: sh: 1: /usr/libexec/hypervkvpd/hv_get_dns_info: not found
Oct 13 00:42:45 maps-live hv_kvp_daemon[2163]: sh: 1: /usr/libexec/hypervkvpd/hv_get_dhcp_info: not found
Oct 13 00:42:45 maps-live hv_kvp_daemon[2171]: sh: 1: /usr/libexec/hypervkvpd/hv_get_dns_info: not found
Oct 13 00:42:45 maps-live hv_kvp_daemon[2173]: sh: 1: /usr/libexec/hypervkvpd/hv_get_dhcp_info: not found
Oct 13 00:42:45 maps-live systemd[1]: Starting Download data for packages that failed at package install time...
Oct 13 00:42:46 maps-live systemd[1]: update-notifier-download.service: Deactivated successfully.
Oct 13 00:42:46 maps-live systemd[1]: Finished Download data for packages that failed at package install time.
Oct 13 00:42:47 maps-live dbus-daemon[730]: [system] Activating via systemd: service name=&#39;org.freedesktop.timedate1&#39; unit=&#39;dbus-org.freedesktop.timedate1.service&#39; requested by &#39;:1.11&#39; (uid=0 pid=748 comm=&quot;/usr/lib/snapd/snapd &quot; label=&quot;unconfined&quot;)
Oct 13 00:42:47 maps-live systemd[1]: Starting Time &amp; Date Service...
Oct 13 00:42:47 maps-live dbus-daemon[730]: [system] Successfully activated service &#39;org.freedesktop.timedate1&#39;-v wont come out of saved state
Oct 13 00:42:47 maps-live systemd[1]: Started Time &amp; Date Service.
Oct 13 00:42:53 maps-live snapd[748]: storehelpers.go:773: cannot refresh: snap has no updates available: &quot;core20&quot;, &quot;lxd&quot;, &quot;snapd&quot;
Oct 13 00:42:55 maps-live hv_kvp_daemon[2186]: sh: 1: /usr/libexec/hypervkvpd/hv_get_dns_info: not found
Oct 13 00:42:55 maps-live hv_kvp_daemon[2188]: sh: 1: /usr/libexec/hypervkvpd/hv_get_dhcp_info: not found
Oct 13 00:42:55 maps-live hv_kvp_daemon[2196]: sh: 1: /usr/libexec/hypervkvpd/hv_get_dns_info: not found
Oct 13 00:42:55 maps-live hv_kvp_daemon[2198]: sh: 1: /usr/libexec/hypervkvpd/hv_get_dhcp_info: not found
Oct 13 00:42:57 maps-live renderd[743]: DONE TILE s2o 3 0-7 0-7 in 235.340 seconds
Oct 13 00:42:57 maps-live renderd[743]: Creating and writing a metatile to /var/cache/renderd/tiles/s2o/3/0/0/0/0/0.meta</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maptiles" rel="tag" title="see questions tagged &#39;maptiles&#39;">maptiles</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-404" rel="tag" title="see questions tagged &#39;404&#39;">404</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '23, 23:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0df9f75be4430d9814261a32c5ac07d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jagjaeger&#39;s gravatar image" />
<p><span>Jagjaeger</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jagjaeger has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-87903" class="comments-container">
&#10;</div>
<div id="comment-tools-87903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87903-form-container" class="comment-form-container">
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

<span id="87905"></span>

<div id="answer-container-87905" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87905-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think we resolved the issue. Ended up making adjustments to the renderd.conf in conf.available and coping it over to conf.enabled. I think the biggest issue was the ModTileMaxLoadMissing. Changing it 30 seems to give it enough time. We noticed that the 404 was getting thrown about every 5 seconds which was inline for the default setting of 5.</p>
<p>Thank you everyone for the help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '23, 21:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0df9f75be4430d9814261a32c5ac07d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jagjaeger&#39;s gravatar image" />
<p><span>Jagjaeger</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jagjaeger has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-87905" class="comments-container">
&#10;</div>
<div id="comment-tools-87905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87905-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87904"></span>

<div id="answer-container-87904" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87904-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've seen "Sending NotDone response" when:</p>
<ul>
<li>renderd.conf was misconfigured (in my example I had TILEDIR pointing to somewhere that did not exist)</li>
<li>renderd had died, perhaps out of memory</li>
<li>renderd was unhappy because proj4 was missing</li>
</ul>
<p>Of those, if you've pre-rendered tiles successfully it's unlikely to be the first or the last, so I'd restart renderd and apache2 and see if that fixes it. If it does, watch for out of memory issues or log entries suggesting that renderd has died for some reason.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '23, 23:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-87904" class="comments-container">
&#10;</div>
<div id="comment-tools-87904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87904-form-container" class="comment-form-container">
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


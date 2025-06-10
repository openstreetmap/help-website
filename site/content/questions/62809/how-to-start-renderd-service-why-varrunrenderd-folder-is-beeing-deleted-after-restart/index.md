+++
type = "question"
title = "How to start Renderd service? Why &quot;/var/run/renderd&quot; folder is beeing deleted after restart?"
description = '''Hello, I am trying to create my own OSM server. I am using Ubuntu 16.04.4 LTS running on a VirtualBox as guest system. I am doing the setup with the nice tutorial on switch2osm.org site for Ubuntu 16.04.2. I did all the steps there. I am having issues with renderd service. One of them is that after ...'''
date = "2018-03-24T17:24:00Z"
lastmod = "2018-03-25T22:48:00Z"
weight = 62809
keywords = [ "renderd" ]
aliases = [ "/questions/62809" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to start Renderd service? Why "/var/run/renderd" folder is beeing deleted after restart?](/questions/62809/how-to-start-renderd-service-why-varrunrenderd-folder-is-beeing-deleted-after-restart)

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
<span id="post-62809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62809-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am trying to create my own OSM server. I am using Ubuntu 16.04.4 LTS running on a VirtualBox as guest system. I am doing the setup with the nice tutorial on switch2osm.org site for Ubuntu 16.04.2. I did all the steps there.</p>
<p>I am having issues with <strong>renderd</strong> service. One of them is that after each server restart this folder is beeing deleted by unknown reasons.</p>
<p>If I run below command after server restart</p>
<pre><code>journalctl -b0 _PID=1 | grep Failed</code></pre>
<p>it shows following output:</p>
<pre><code>Mar 24 16:11:22 huawei-VirtualBox systemd[1]: Failed to start Renderd.
Mar 24 16:11:22 huawei-VirtualBox systemd[1]: renderd.service: Failed with result &#39;exit-code&#39;.</code></pre>
<p>When I check <code>/var/run/renderd</code> it does not exist anymore.</p>
<p>Then again I repeat following commands:</p>
<pre><code>sudo mkdir /var/run/renderd
sudo chown huawei /var/run/renderd</code></pre>
<p>and folder is there again. Just in case I am reloading apache with:</p>
<pre><code>sudo service apache2 reload</code></pre>
<p>Then comes my second problem.</p>
<p>If I run the service in the foreground it looks like starting ok - below is an extract after execution (in fact there are about 82 warning for "unable to find face-name" - I have no idea whether this is a problem).</p>
<pre><code>...
renderd[5539]: Loading parameterization function for 
renderd[5539]: Starting stats thread
...
Mapnik LOG&gt; 2018-03-24 16:51:03: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2018-03-24 16:51:03: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
renderd[5539]: Using web mercator projection settings
renderd[5539]: Using web mercator projection settings</code></pre>
<p>After ctrl+c I am starting the service with:</p>
<pre><code>huawei@huawei-VirtualBox:~$ sudo /etc/init.d/renderd start
#</code></pre>
<p>According to the manual it should return “[ ok ] Starting renderd (via systemctl): renderd.service.”, but this does not happen and only # stays. When I type exit following appears:</p>
<pre><code>[....] Starting renderd (via systemctl): renderd.serviceJob for renderd.service failed because the control process exited with error code. See &quot;systemctl status renderd.service&quot; and &quot;journalctl -xe&quot; for details.
 failed!</code></pre>
<p>Then if I run again</p>
<pre><code>journalctl -b0 _PID=1 | grep Failed</code></pre>
<p>it shows the same error message as in the beginning of my question.</p>
<pre><code>Mar 24 17:01:52 huawei-VirtualBox systemd[1]: Failed to start Renderd.
Mar 24 17:01:52 huawei-VirtualBox systemd[1]: renderd.service: Failed with result &#39;exit-code&#39;.</code></pre>
<p>Interesting is that the time above is the time of executing Exit and not the time of service start attempt.</p>
<p>One other thing that can put some light on my problem. When I try to set server to pre-render tiles with</p>
<pre><code>render_list -m default -a -z 0 -Z 10</code></pre>
<p>following error output is received (the command is taken from another tutorial):</p>
<pre><code>debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
Rendering client
Starting 1 rendering threads
Rendering all tiles from zoom 0 to zoom 10
Rendering all tiles for zoom 0 from (0, 0) to (0, 0)
Rendering all tiles for zoom 1 from (0, 0) to (1, 1)
Rendering all tiles for zoom 2 from (0, 0) to (3, 3)
Rendering all tiles for zoom 3 from (0, 0) to (7, 7)
Rendering all tiles for zoom 4 from (0, 0) to (15, 15)
Rendering all tiles for zoom 5 from (0, 0) to (31, 31)
Rendering all tiles for zoom 6 from (0, 0) to (63, 63)
socket connect failed for: /var/run/renderd/renderd.sock</code></pre>
<p>Folder "/var/run/renderd" and file "renderd.sock" exist.</p>
<p>What could be wrong with my configuration and where I could possibly search for the problem? I would be very happy for some thoughts and suggestions. Thank you in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '18, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb979091bc877382f06444606bb7906?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="idenchev&#39;s gravatar image" />
<p><span>idenchev</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="idenchev has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-62809" class="comments-container">
&#10;</div>
<div id="comment-tools-62809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62809-form-container" class="comment-form-container">
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

<span id="62817"></span>

<div id="answer-container-62817" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62817-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>The author of question is answering himself. I was not able to find a solution to my problem when using the OSM server installation guide in <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">switch2osm</a> site.</p>
<p>Then I found another description for building OSM server on following link: <a href="https://ircama.github.io/osm-carto-tutorials/tile-server-ubuntu/">ircama.github.io/osm-carto-tutorials</a>. It is much more detailed, the steps and settings are more and the approach is some kind different, but the result is successfully comissioned OSM server without any truobles. It is a really great description. It is pity that the author name is not mentioned, so that to congratulate him/her with name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '18, 22:17</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb979091bc877382f06444606bb7906?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="idenchev&#39;s gravatar image" />
<p><span>idenchev</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="idenchev has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '18, 22:18</strong> </span></p>
</div>
</div>
<div id="comments-container-62817" class="comments-container">
<span id="62818"></span>
<div id="comment-62818" class="comment">
<div id="post-62818-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've accepted your answer on your behalf - hope you don't mind.</p>
<p>One question though - what, actually, was the solution to the problem? What fixed (presumably) the access rights that allowed /var/run/renderd to be created?</p>
</div>
<div id="comment-62818-info" class="comment-info">
<span class="comment-age">(25 Mar '18, 22:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62817-form-container" class="comment-form-container">
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


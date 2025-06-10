+++
type = "question"
title = "How Can i Speed up the tiles loading in the map"
description = '''Hi from last couple weeks, i am learning OSM , i have setup own tiles , they all good. I am using rendering  Ref : https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site   render_list -n 1 -s /var/run/renderd/renderd.sock -z 0 -Z 20 -m ajt -a  now I have cou...'''
date = "2018-06-18T17:13:00Z"
lastmod = "2018-06-18T17:13:00Z"
weight = 64241
keywords = [ "rendering" ]
aliases = [ "/questions/64241" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How Can i Speed up the tiles loading in the map](/questions/64241/how-can-i-speed-up-the-tiles-loading-in-the-map)

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
<span id="post-64241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64241-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi from last couple weeks, i am learning OSM , i have setup own tiles , they all good. I am using rendering</p>
<pre><code>Ref : https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site
&#10; render_list -n 1 -s /var/run/renderd/renderd.sock -z 0 -Z 20 -m ajt  -a</code></pre>
<p>now I have couple of question . Initially our services will be only for particular country , later on we will exend that to few other countries. we will provide TRacking solution for a particular country only and we are expecting lot of vechiles so the reqeust will be very high.</p>
<p>I wanted to know how can I speed up the loading of maps ( one country ) ? basically i am trying to understand if i can avoid postgress with every times user try to load a map.</p>
<p>if i Render all tiles betwen 0 to 25 for a country before hand, will it make the map loading faster ? if Render before hand by using "--z 0 -Z 20 " will it still require to use postgres when servering map ?</p>
<p>(we will use the map in Dekstop and Mobile for tracking solution.)</p>
<p>I have lot of space to hold tiles ( so no worris about that) , just trying to see how can i avoid on demand rendering with postgress also if i can serve tiles from a static place i.e web server.</p>
<p>Additional Note, if i Look at this one</p>
<blockquote>
<p><a href="https://wiki.openstreetmap.org/wiki/Creating_your_own_tiles">https://wiki.openstreetmap.org/wiki/Creating_your_own_tiles</a></p>
</blockquote>
<p>section "Creating tiles using Mapnik and generate_tiles.py"</p>
<pre><code>When everything works, use generate_tiles.py to create 1000s of tiles in a special hierarchy of folders
Copy/move tiles into your webserver&#39;s document root.</code></pre>
<p>does it mean, i will not require postgress or further rendering at all ? if yes it should be fast to load right ?</p>
<p>Please let me know.</p>
<p>Thanks for the help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '18, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jun '18, 18:57</strong> </span></p>
</div>
</div>
<div id="comments-container-64241" class="comments-container">
&#10;</div>
<div id="comment-tools-64241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64241-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


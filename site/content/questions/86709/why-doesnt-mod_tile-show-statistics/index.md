+++
type = "question"
title = "Why doesn&#x27;t mod_tile show statistics"
description = '''Server is installed and tiles seem to render and display as expected. But http://server/mod_tile shows the directory contents instead of the statistics page. Munin is also installed and shows various stats, but mod_tile graphs are empty. The stats_file defined in /etc/renderd.conf is as expected: -r...'''
date = "2023-02-16T15:45:00Z"
lastmod = "2023-02-21T20:12:00Z"
weight = 86709
keywords = [ "stats", "mod_tile" ]
aliases = [ "/questions/86709" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why doesn't mod_tile show statistics](/questions/86709/why-doesnt-mod_tile-show-statistics)

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
<span id="post-86709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86709-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Server is installed and tiles seem to render and display as expected. But <a href="http://server/mod_tile">http://server/mod_tile</a> shows the directory contents instead of the statistics page. Munin is also installed and shows various stats, but mod_tile graphs are empty. The stats_file defined in /etc/renderd.conf is as expected: -rw-r--r-- 1 osm nogroup 1152 16. Feb 15:44 /run/renderd/renderd.stats and contains stats as expected. I have run out of ideas - help appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stats" rel="tag" title="see questions tagged &#39;stats&#39;">stats</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '23, 15:45</strong></p>
<img src="https://secure.gravatar.com/avatar/d6d95189d57bd84e76b3f1d0c9c410ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markwe&#39;s gravatar image" />
<p><span>markwe</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markwe has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86709" class="comments-container">
<span id="86725"></span>
<div id="comment-86725" class="comment">
<div id="post-86725-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Munin reads data from "/run/renderd/renderd.stats", which works.</p>
<p>My recollection is that there was (more than 7 years ago) mod_tile had a provision for a site you could browse to and view statistics. Even back then that never worked for me for reasons unrelated to the software. However, munin works, and if you want use something else you can look at munin's plugins and read from /run/renderd/renderd.stats in the same way.</p>
<p>When the big "package mod_tile properly for Debian" was done, various mod_tile enhancements were gathered together from various places, and it was then maintained properly for the first time in years. I think that it was at this stage that the "basic site you could browse statistics" went away. I did have a brief look at it back then, but it wasn't obvious to me what would be needed to fix it, and given that the statistics were available and munin can read them, there was no point in worrying about it.</p>
<p>What are you actually trying to do, and what (if any) set of instructions are you following that do not work?</p>
</div>
<div id="comment-86725-info" class="comment-info">
<span class="comment-age">(18 Feb '23, 12:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="86728"></span>
<div id="comment-86728" class="comment">
<div id="post-86728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just trying to get the basic stats for mod_tile as per documentation on wiki.openstreetmap.org: <a href="http://your.server/mod_tile">http://your.server/mod_tile</a> The reason my munin is not working is now obvious. All the mod_tile plugin scripts collect the data per: data="wget -q <a href="http://localhost/mod_tile">http://localhost/mod_tile</a> -O -" Munin shows the renderd stats fine, as this comes from /run/renderd/renderd.stats. So with munin, renderd status are fine. Mod_tile stats are empty charts.</p>
</div>
<div id="comment-86728-info" class="comment-info">
<span class="comment-age">(18 Feb '23, 20:54)</span> <span class="comment-user userinfo">markwe</span>
</div>
</div>
<span id="86729"></span>
<div id="comment-86729" class="comment">
<div id="post-86729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had no idea that e.g. "mod_tile_fresh" still did that underneath :)</p>
<p>If you do a "wget -q <a href="http://localhost/mod_tile">http://localhost/mod_tile</a> -O -" from the shell, what actually happens? Do you get an Apache error code, and if so, what?</p>
</div>
<div id="comment-86729-info" class="comment-info">
<span class="comment-age">(18 Feb '23, 21:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="86733"></span>
<div id="comment-86733" class="comment">
<div id="post-86733-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I get the directory listing (index) of /var/cache/renderd/tiles (tile_dir from /etc/renderd.conf). But my expectation is:<br />
<a href="https://tile.openstreetmap.de/mod_tile">https://tile.openstreetmap.de/mod_tile</a></p>
</div>
<div id="comment-86733-info" class="comment-info">
<span class="comment-age">(19 Feb '23, 04:48)</span> <span class="comment-user userinfo">markwe</span>
</div>
</div>
<span id="86766"></span>
<div id="comment-86766" class="comment">
<div id="post-86766-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>I get the directory listing (index)</p>
</blockquote>
<p>That sounds like an apache config error. If you follow the apache bits of <a href="https://switch2osm.org/serving-tiles/">https://switch2osm.org/serving-tiles/</a> you won't get that - I followed those instructions and I get <a href="http://map.atownsend.org.uk/mod_tile">http://map.atownsend.org.uk/mod_tile</a> .</p>
</div>
<div id="comment-86766-info" class="comment-info">
<span class="comment-age">(21 Feb '23, 14:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="86770"></span>
<div id="comment-86770" class="comment not_top_scorer">
<div id="post-86770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep. I combed through the apache configs and there were some left over directives which were conflicting. Works like a charm now, including munin. Thanks for the pointers !</p>
</div>
<div id="comment-86770-info" class="comment-info">
<span class="comment-age">(21 Feb '23, 20:12)</span> <span class="comment-user userinfo">markwe</span>
</div>
</div>
</div>
<div id="comment-tools-86709" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-86709-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


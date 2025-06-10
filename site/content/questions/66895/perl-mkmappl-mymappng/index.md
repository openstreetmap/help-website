+++
type = "question"
title = "perl mkmap.pl &gt; mymap.png"
description = '''Hi Like the following manual https://wiki.openstreetmap.org/wiki/DE:Bigmap I downloaded a mkmap.pl file. With perl mkmap.pl &amp;gt; mymap.png I tried to create a png file. During the download sometimes appears: http://tile.openstreetmap.org/11/1097/729.png... 500 Status read failed: Eine vorhandene Ver...'''
date = "2018-11-23T22:38:00Z"
lastmod = "2018-11-23T22:38:00Z"
weight = 66895
keywords = [ "download", "png", "perl" ]
aliases = [ "/questions/66895" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [perl mkmap.pl \> mymap.png](/questions/66895/perl-mkmappl-mymappng)

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
<span id="post-66895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66895-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>Like the following manual <a href="https://wiki.openstreetmap.org/wiki/DE:Bigmap">https://wiki.openstreetmap.org/wiki/DE:Bigmap</a> I downloaded a mkmap.pl file. With perl mkmap.pl &gt; mymap.png I tried to create a png file.</p>
<p>During the download sometimes appears: <a href="http://tile.openstreetmap.org/11/1097/729.png...">http://tile.openstreetmap.org/11/1097/729.png...</a> 500 Status read failed: Eine vorhandene Verbindung wurde vom Remotehost geschlossen.</p>
<p>Sometrimes appears: <a href="http://tile.openstreetmap.org/11/1095/745.png...">http://tile.openstreetmap.org/11/1095/745.png...</a> 500 Can't connect to tile.openstreetmap.org:80 (Invalid argument)</p>
<p>Mostly appears: <a href="http://tile.openstreetmap.org/11/1096/748.png...">http://tile.openstreetmap.org/11/1096/748.png...</a> 200 OK</p>
<p>After about 1 hour appears: &lt;html&gt;&lt;head&gt; &lt;meta http-equiv="cache-control" content="no-cache"&gt; &lt;meta http-equiv="pragma" content="no-cache"&gt; &lt;meta http-equiv="refresh" content="0;url=/ui/dboard"&gt; &lt;/head&gt;&lt;/html&gt; not found: Invalid argument at C:/Perl64/lib/GD/Image.pm line 64.</p>
<p>At the end, normally the png-file is empty. Once I had a png File (93MB) but with many white squares.</p>
<p>What do I wrong?</p>
<p>Thanks and best regards!</p>
<p>my mkmap.pl file contains:</p>
<h1 id="usrbinperl">!/usr/bin/perl</h1>
<h1 id="generated-from-httpopenstreetmap.gryph.debigmap.cgi">generated from <a href="http://openstreetmap.gryph.de/bigmap.cgi/">http://openstreetmap.gryph.de/bigmap.cgi/</a></h1>
<h1 id="permalink-for-this-map-httpopenstreetmap.gryph.debigmap.cgixmin1066xmax1121ymin715ymax751zoom11scale256baseurlhttp3a2f2ftile.openstreetmap.org2f21z2f21x2f21y.png">permalink for this map: <a href="http://openstreetmap.gryph.de/bigmap.cgi?xmin=1066&amp;xmax=1121&amp;ymin=715&amp;ymax=751&amp;zoom=11&amp;scale=256&amp;baseurl=http%3A%2F%2Ftile.openstreetmap.org%2F%21z%2F%21x%2F%21y.png">http://openstreetmap.gryph.de/bigmap.cgi?xmin=1066&amp;xmax=1121&amp;ymin=715&amp;ymax=751&amp;zoom=11&amp;scale=256&amp;baseurl=http%3A%2F%2Ftile.openstreetmap.org%2F%21z%2F%21x%2F%21y.png</a></h1>
<h1 id="section"></h1>
<p>use strict; use LWP; use GD;</p>
<p>my $img = GD::Image-&gt;new(14336, 9472, 1); my $white = $img-&gt;colorAllocate(248,248,248); $img-&gt;filledRectangle(0,0,14336,9472,$white); my $ua = LWP::UserAgent-&gt;new(); $ua-&gt;env_proxy; for (my $x=0;$x&lt;56;$x++) { for (my $y=0;$y&lt;37;$y++) { my $xx = $x + 1066; my $yy = $y + 715; foreach my $base(split(/\|/, "http://tile.openstreetmap.org/11/!x/!y.png")) { my $url = $base; $url =~ s/!x/$xx/g; $url =~ s/!y/$yy/g; print STDERR "$url... "; my $resp = $ua-&gt;get($url); print STDERR $resp-&gt;status_line; print STDERR "\n"; next unless $resp-&gt;is_success; my $tile = GD::Image-&gt;new($resp-&gt;content); next if ($tile-&gt;width == 1); if ($base =~ /seamark/) { my $black=$tile-&gt;colorClosest(0,0,0); $tile-&gt;transparent($black); } $img-&gt;copy($tile, $x<em>256,$y</em>256,0,0,256,256); } } } binmode STDOUT; print $img-&gt;png();</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-png" rel="tag" title="see questions tagged &#39;png&#39;">png</span> <span class="post-tag tag-link-perl" rel="tag" title="see questions tagged &#39;perl&#39;">perl</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '18, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/cd7137960bbf5929c3784a3f67aa17b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="test99&#39;s gravatar image" />
<p><span>test99</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="test99 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66895" class="comments-container">
&#10;</div>
<div id="comment-tools-66895" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66895-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


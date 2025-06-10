+++
type = "question"
title = "The requested URL /osm/0/0/0.png was not found on this server"
description = '''Just installed OSM on Ubuntu 18.04 using the rather excellent guide published by the switch2osm folks. Everything works up to and including the initial manual test of rendered. When I try to go to the web page at http://yourserveripaddress/osm/0/0/0.png (yes, using the server&#x27;s IP address) I get the...'''
date = "2019-09-18T07:24:00Z"
lastmod = "2023-03-20T10:59:00Z"
weight = 70827
keywords = [ "osm", "tileserver" ]
aliases = [ "/questions/70827" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [The requested URL /osm/0/0/0.png was not found on this server](/questions/70827/the-requested-url-osm000png-was-not-found-on-this-server)

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
<span id="post-70827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70827-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Just installed OSM on Ubuntu 18.04 using the rather excellent guide published by the switch2osm folks.</p>
<p>Everything works up to and including the initial manual test of rendered.</p>
<p>When I try to go to the web page at <a href="http://yourserveripaddress/osm/0/0/0.png">http://yourserveripaddress/osm/0/0/0.png</a> (yes, using the server's IP address) I get the following error;</p>
<p>The requested URL /osm/0/0/0.png was not found on this server</p>
<p>I've reviewed all of the steps and confess I am a bit confused, not that that is particularly unusual. I tend to get grumpy when I follow a recipe and I burn the cake... so to speak.</p>
<p>Any help would be most helpful.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '19, 07:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a285ddf311b5f7382fd8001ac7460d65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amu306&#39;s gravatar image" />
<p><span>amu306</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amu306 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70827" class="comments-container">
&#10;</div>
<div id="comment-tools-70827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70827-form-container" class="comment-form-container">
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

<span id="70828"></span>

<div id="answer-container-70828" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70828-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Which instructions did you follow exactly - these: <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> ? In that case (slightly non-intuitively perhaps) your tiles will be under /hot/ not under /osm/.</p>
<p>In any case double-check that you have made the necessary changes to the Apache config as documented, and if things still don't work let us see what appears in your /var/log/apache2/error.log when you make this request.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '19, 07:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70828" class="comments-container">
<span id="70830"></span>
<div id="comment-70830" class="comment">
<div id="post-70830-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I followed <a href="https://www.linuxbabe.com/linux-server/openstreetmap-tile-server-ubuntu-16-04">https://www.linuxbabe.com/linux-server/openstreetmap-tile-server-ubuntu-16-04</a> this article to setup tile server on ubuntu 18.04 . All is set up perfectly but the image was not found</p>
</div>
<div id="comment-70830-info" class="comment-info">
<span class="comment-age">(18 Sep '19, 09:24)</span> <span class="comment-user userinfo">amu306</span>
</div>
</div>
<span id="70831"></span>
<div id="comment-70831" class="comment">
<div id="post-70831-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Are you sure you used this guide. Because up there you said that you followed a switch2osm guide which is different. And the guide you have just quoted says "Then in your web browser address bar, type your-server-ip/osm_tiles/0/0/0.png" - but you apparently expected that "/osm/0/0/0.png" works. Where did you get that from? It appears that you might have burnt your cake by using a random mix of recipes!</p>
</div>
<div id="comment-70831-info" class="comment-info">
<span class="comment-age">(18 Sep '19, 09:43)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="70835"></span>
<div id="comment-70835" class="comment">
<div id="post-70835-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>this is what can be seen while rendering sudo -u tharakk renderd -f -c /usr/local/etc/renderd.conf</p>
<p>renderd[31905]: Rendering daemon started renderd[31905]: Initiating reqyest_queue renderd[31905]: Parsing section renderd renderd[31905]: Parsing render section 0 renderd[31905]: Parsing section mapnik renderd[31905]: Parsing section default renderd[31905]: Parsing section style2 renderd[31905]: config renderd: unix socketname=/var/run/renderd/renderd.sock renderd[31905]: config renderd: num_threads=4 renderd[31905]: config renderd: num_slaves=0 renderd[31905]: config renderd: tile_dir=/var/lib/mod_tile renderd[31905]: config renderd: stats_file=/var/run/renderd/renderd.stats renderd[31905]: config mapnik: plugins_dir=/usr/local/lib/mapnik/input renderd[31905]: config mapnik: font_dir=/usr/share/fonts/truetype/ttf-dejavu renderd[31905]: config mapnik: font_dir_recurse=1 renderd[31905]: config renderd(0): Active renderd[31905]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock renderd[31905]: config renderd(0): num_threads=4</p>
<p>========================</p>
</div>
<div id="comment-70835-info" class="comment-info">
<span class="comment-age">(18 Sep '19, 13:18)</span> <span class="comment-user userinfo">amu306</span>
</div>
</div>
<span id="70836"></span>
<div id="comment-70836" class="comment">
<div id="post-70836-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Before you posted this you posted a link to your server IP which I will not repeat assuming you removed it on purpose. But that link proves that your mod_tile is working and that you have actually configured a /osm/ tile layer; however mod_tile immediately returns a 404 error for any tiles requested. Likely this is either because mod_tile cannot contact the renderd server - could be a freak local networking or security issue e.g. SELinux - or that mod_tile does contact the server but then gets an error message back. Check the /var/log/apache2/error.log for further info.</p>
</div>
<div id="comment-70836-info" class="comment-info">
<span class="comment-age">(18 Sep '19, 14:00)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70828-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86953"></span>

<div id="answer-container-86953" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86953-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In my case, the 404 error occurred because the apache2 configuration was wrong. I put localhost in the apache2 settings. I checked /var/log/apache2/error.log for errors. When I changed localhost to IP, it worked fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '23, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/6d504dc9ccb917e9f8662151f3b738a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kharma77&#39;s gravatar image" />
<p><span>kharma77</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kharma77 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86953" class="comments-container">
&#10;</div>
<div id="comment-tools-86953" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86953-form-container" class="comment-form-container">
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


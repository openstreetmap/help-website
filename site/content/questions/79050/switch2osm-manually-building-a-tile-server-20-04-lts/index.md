+++
type = "question"
title = "switch2osm manually-building-a-tile-server-20-04-lts"
description = '''I&#x27;m following the guide. Reached the point of installing carto. after what appears to be a successful install, I isssue carto -v which returns: /usr/lib/nodejs/carto/lib/carto/tree/reference.js:19  if (mapnik_reference.version.hasOwnProperty(version)) {  ^  TypeError: Cannot read property &#x27;hasOwnPro...'''
date = "2021-02-27T11:47:00Z"
lastmod = "2021-02-27T15:35:00Z"
weight = 79050
keywords = [ "sudo", "carto", "ubunto", "switch2osm" ]
aliases = [ "/questions/79050" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [switch2osm manually-building-a-tile-server-20-04-lts](/questions/79050/switch2osm-manually-building-a-tile-server-20-04-lts)

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
<span id="post-79050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79050-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm following the guide. Reached the point of installing carto. after what appears to be a successful install, I isssue carto -v which returns:</p>
<pre><code>/usr/lib/nodejs/carto/lib/carto/tree/reference.js:19
    if (mapnik_reference.version.hasOwnProperty(version)) {
                             ^
&#10;TypeError: Cannot read property &#39;hasOwnProperty&#39; of undefined
    at Object.ref.setVersion (/usr/lib/nodejs/carto/lib/carto/tree/reference.js:19:34)
    at /usr/lib/nodejs/carto/lib/carto/tree/reference.js:209:5
    at Object.&lt;anonymous&gt; (/usr/lib/nodejs/carto/lib/carto/tree/reference.js:213:3)
    at Module._compile (internal/modules/cjs/loader.js:778:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:789:10)
    at Module.load (internal/modules/cjs/loader.js:653:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:593:12)
    at Function.Module._load (internal/modules/cjs/loader.js:585:3)
    at Module.require (internal/modules/cjs/loader.js:692:17)
    at require (internal/modules/cjs/helpers.js:25:18)</code></pre>
<p>However if I invoke carto using sudo, it works fine. I can get by using sudo carto to convert project.mml to mapnik.xml. I'm just wondering what I did wrong!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sudo" rel="tag" title="see questions tagged &#39;sudo&#39;">sudo</span> <span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-ubunto" rel="tag" title="see questions tagged &#39;ubunto&#39;">ubunto</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '21, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/ec180fe051c382b214977ae4a8bf85e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G3YAC&#39;s gravatar image" />
<p><span>G3YAC</span><br />
<span class="score" title="516 reputation points">516</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="G3YAC has 2 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '21, 12:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-79050" class="comments-container">
&#10;</div>
<div id="comment-tools-79050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79050-form-container" class="comment-form-container">
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

<span id="79054"></span>

<div id="answer-container-79054" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79054-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm guessing here, but if something works when run from root but not from a regular user I'm guessing that you did something from root that shouldn't have been done from root?</p>
<p>I'd start by checking project.mml and the rest of the OSM Carto style that you cloned from github.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '21, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-79054" class="comments-container">
<span id="79057"></span>
<div id="comment-79057" class="comment">
<div id="post-79057-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>THANKS - It fails with carto -v which is before I try to use project.xml</p>
<p>There's nothing obvious earlier in the chain of setup operations.</p>
</div>
<div id="comment-79057-info" class="comment-info">
<span class="comment-age">(27 Feb '21, 14:10)</span> <span class="comment-user userinfo">G3YAC</span>
</div>
</div>
<span id="79059"></span>
<div id="comment-79059" class="comment">
<div id="post-79059-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good point. Was there anything different to <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a> that you did early on that might cause it? It's not something silly like "disk full" is it? The relevant lines:</p>
<pre><code>sudo apt install npm
sudo npm install -g carto
carto -v</code></pre>
<p>just use Ubuntu's standard npm, and were working just fine the last time I tested it (a couple of months ago)</p>
</div>
<div id="comment-79059-info" class="comment-info">
<span class="comment-age">(27 Feb '21, 14:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="79061"></span>
<div id="comment-79061" class="comment">
<div id="post-79061-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The error message points to a too-old version of carto. Type the command <code>which carto</code> as root and as non-root user; my hunch is that you might have installed a new version of carto with "npm install carto" as well as an older version from the Ubuntu distribution with "apt install carto" and that when root you run the correct version and when not root you run the too-old version.</p>
</div>
<div id="comment-79061-info" class="comment-info">
<span class="comment-age">(27 Feb '21, 15:12)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="79063"></span>
<div id="comment-79063" class="comment">
<div id="post-79063-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think it is something silly - but not disc full. I found that there was a directory oddity: ~/src/openstreetmap-carto/openstreetmap.carto.</p>
<p>I must have done something stupid when copy/pasting. I just repeated the instructions from 'install mod tile and rendered'. Carto then returned version number as expected without needing sudo. It also processes project.mml to mapnik.xml without sudo but with lots of warnings about style/...not matching layer selector. I'll see what happens next but it is tempting to wipe the VM I'm using and have a fresh start. Thanks for your help.</p>
</div>
<div id="comment-79063-info" class="comment-info">
<span class="comment-age">(27 Feb '21, 15:35)</span> <span class="comment-user userinfo">G3YAC</span>
</div>
</div>
</div>
<div id="comment-tools-79054" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79054-form-container" class="comment-form-container">
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


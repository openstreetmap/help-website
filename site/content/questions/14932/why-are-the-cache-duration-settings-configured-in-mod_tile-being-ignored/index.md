+++
type = "question"
title = "Why are the cache duration settings configured in mod_tile being ignored?"
description = '''Hello, I`m running a tile server on Ubuntu 12.04LTS according to the documentation of switch2osm.org using the openstreetmap ppa from kakrueger.  The geo-data doesn`t need to be update more than once in a month so I`ve set the caching times in mod_tile to one month - every cache duration setting I f...'''
date = "2012-08-09T20:15:00Z"
lastmod = "2012-08-10T22:06:00Z"
weight = 14932
keywords = [ "renderd", "cache", "mod_tile", "ubuntu", "switch2osm" ]
aliases = [ "/questions/14932" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why are the cache duration settings configured in mod_tile being ignored?](/questions/14932/why-are-the-cache-duration-settings-configured-in-mod_tile-being-ignored)

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
<span id="post-14932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14932-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I`m running a tile server on Ubuntu 12.04LTS according to the documentation of switch2osm.org using the openstreetmap ppa from kakrueger.</p>
<p>The geo-data doesn`t need to be update more than once in a month so I`ve set the caching times in mod_tile to one month - every cache duration setting I found in tileserver_site. When analyzing the tile requests with firebug the correct cache duration settings appear in the header.</p>
<p>However, three days after the tiles are being pre-rendered they are considered to be outdated and rendered again on-the-fly when being requested by a client! So my cache duration settings in the config-file tileserver_site seem to be ignored.</p>
<p>Now my questions:</p>
<p><strong>How to enforce longer caching times? Where do I have to configure these settings to take effect? Does renderd ignore the mod_tile settings?</strong> What I do is: - touch the planet_import_complete after data-import with osm2pgsql - pre-render important and slow-rendered zoom-levels with render_list (Have to note that render_list tells me that it is missing the timestamp file:</p>
<pre><code>Planet timestamp file (/var/lib/mod_tile//planet-import-complete) is missing</code></pre>
<p>but after googling around this seems to be a bug, isn`t it?)</p>
<p>I would be really glad if there is someone out there to help me or give me a hint...</p>
<p>EDIT: As there are many comments I think it`s not a bad idea to summarize them:</p>
<p>The answer of Frederik Ramm was the key: My timestamp file had a wrong name. I had</p>
<p>planet_import_complete</p>
<p>in the right folder. But the name must be</p>
<p>planet-import-complete</p>
<p>After correcting the file name of the timestamp-file render_list was reporting a correct message indicating the last update of the timestamp.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-cache" rel="tag" title="see questions tagged &#39;cache&#39;">cache</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '12, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/cfb323a8b79422753c14105f98941ec5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSMDeveloperBK&#39;s gravatar image" />
<p><span>OSMDeveloperBK</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSMDeveloperBK has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '12, 22:24</strong> </span></p>
</div>
</div>
<div id="comments-container-14932" class="comments-container">
&#10;</div>
<div id="comment-tools-14932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14932-form-container" class="comment-form-container">
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

<span id="14933"></span>

<div id="answer-container-14933" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14933-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-14933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="OSMDeveloperBK has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you see is consistent with the error message. When no planet-import-complete file is found, mod_tile will assume the planet file is three days old, and any tile older than three days will be re-rendered.</p>
<p>If this is indeed a bug then you better get yourself a mod_tile version that doesn't have the bug. Are you really sure that you have your planet-import-complete file in the right location? It must either be in /var/lib/mod_tile or in /var/lib/mod_tile/whatever-your-stylename-is.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '12, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '12, 08:33</strong> </span></p>
</div>
</div>
<div id="comments-container-14933" class="comments-container">
<span id="14936"></span>
<div id="comment-14936" class="comment">
<div id="post-14936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, as I wrote in my question, there is the Planet timestamp in the location you mentioned and I`m always touching it after the data-import. But is the directory mentioned in the error message really existing? /var/lib/mod_tile//planet-import-complete</p>
<p>I mean the double slash before planet-import-complete This may indicate that the name of the Whatever-your-stylename-is that you mentioned in your answer is not set but expected? Where do I set that stylename? In the osm.xml or where? By the way, I`m using the German style created in a bachelor thesis you were responsible for.</p>
</div>
<div id="comment-14936-info" class="comment-info">
<span class="comment-age">(10 Aug '12, 08:37)</span> <span class="comment-user userinfo">OSMDeveloperBK</span>
</div>
</div>
<span id="14937"></span>
<div id="comment-14937" class="comment">
<div id="post-14937-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know if the file really exists on your computer. Enter the command</p>
<p><code>[ -f /var/lib/mod_tile//planet-import-complete ] || echo "oh no, the file does not exist"</code></p>
<p>to check. The double slash should not be a problem. - You say you're always touching the file after data import but by that you mean once a month, or are you updating more frequently? If the file exists, then any tile older than the file timestamp will be re-rendered. So if you update your database every day but are happy to have old tiles lying around, then it would not be good to touch the file after each update....</p>
</div>
<div id="comment-14937-info" class="comment-info">
<span class="comment-age">(10 Aug '12, 08:43)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="14938"></span>
<div id="comment-14938" class="comment not_top_scorer">
<div id="post-14938-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah that means I should touch it before running render_list to prerender tiles? And what is whith the cache duration settings of mod-tile? Are they done relative to the timestamp? The file exists and everybody (especially www-data) has full access to it though your command seems to be incomplete.</p>
</div>
<div id="comment-14938-info" class="comment-info">
<span class="comment-age">(10 Aug '12, 08:56)</span> <span class="comment-user userinfo">OSMDeveloperBK</span>
</div>
</div>
<span id="14939"></span>
<div id="comment-14939" class="comment">
<div id="post-14939-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>render_list does not look at the planet-import-complete file, it just renders whatever you tell it. Only mod_tile looks at that timestamp file. The cache duration settings are there to control how long the browser is told to keep the tile, they have nothing to do with how often the tile is rendered.</p>
</div>
<div id="comment-14939-info" class="comment-info">
<span class="comment-age">(10 Aug '12, 09:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="14941"></span>
<div id="comment-14941" class="comment not_top_scorer">
<div id="post-14941-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Now I<code>ve checked my experimental map server installation inside a VM where the standard mapnik style is used and there render_list doesn</code>t say that the timestamp file is missing. So I think in my case the style name is set to an empty string and so it cannot be found. (I think that because of the double slash in the path name of the error message) Where do I have to set the style name? Is it set during the import with osm2pgsql or within renderd.conf or the style-File or where?</p>
</div>
<div id="comment-14941-info" class="comment-info">
<span class="comment-age">(10 Aug '12, 09:50)</span> <span class="comment-user userinfo">OSMDeveloperBK</span>
</div>
</div>
<span id="14942"></span>
<div id="comment-14942" class="comment">
<div id="post-14942-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Usually the name is in your Apache configuration where you have the AddTileConfig directive. The first parameter is the web path, and the second is the style name.</p>
</div>
<div id="comment-14942-info" class="comment-info">
<span class="comment-age">(10 Aug '12, 09:57)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="14943"></span>
<div id="comment-14943" class="comment not_top_scorer">
<div id="post-14943-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, in my config file AddTileConfig is commented out and instead the following is used:</p>
<p>LoadTileConfigFile /etc/renderd.conf</p>
<p>But in renderd.conf there is no option/section for the stylename.</p>
</div>
<div id="comment-14943-info" class="comment-info">
<span class="comment-age">(10 Aug '12, 10:09)</span> <span class="comment-user userinfo">OSMDeveloperBK</span>
</div>
</div>
<span id="14960"></span>
<div id="comment-14960" class="comment">
<div id="post-14960-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Frederik, you were absolutely right: The timestamp file was missing on my system. I had planet_import_complete instead of the required planet-import-complete. Now render_list is not missing the timestamp anymore. In three days I should know it exactly. Thank you very much for this hint! BTW I faced a strange issue when configuring the german map style, but I don<code>t know where to report this bug (?). I</code>ve already described it here: <a href="http://forum.openstreetmap.org/viewtopic.php?pid=253552#p253552">http://forum.openstreetmap.org/viewtopic.php?pid=253552#p253552</a></p>
</div>
<div id="comment-14960-info" class="comment-info">
<span class="comment-age">(10 Aug '12, 22:06)</span> <span class="comment-user userinfo">OSMDeveloperBK</span>
</div>
</div>
</div>
<div id="comment-tools-14933" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-14933-form-container" class="comment-form-container">
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


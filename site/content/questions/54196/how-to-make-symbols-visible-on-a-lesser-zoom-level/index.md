+++
type = "question"
title = "How to make symbols visible on a lesser zoom level"
description = '''Hi! Basically I followed instructions from here:  http://openstreetmapserverwindows.blogspot.com.eg/2015/11/osmopenstreetmap-tile-server.html to set up our own OSM server on Windows Server 2012 64-bit. I edited generate_tiles.py and generated some tiles for Tuam town in Ireland to test this. I notic...'''
date = "2017-01-20T16:38:00Z"
lastmod = "2017-01-20T23:01:00Z"
weight = 54196
keywords = [ "symbols", "rendering", "tileserver" ]
aliases = [ "/questions/54196" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to make symbols visible on a lesser zoom level](/questions/54196/how-to-make-symbols-visible-on-a-lesser-zoom-level)

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
<span id="post-54196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54196-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>Basically I followed instructions from here: <span></span><a href="http://openstreetmapserverwindows.blogspot.com.eg/2015/11/osmopenstreetmap-tile-server.html">http://openstreetmapserverwindows.blogspot.com.eg/2015/11/osmopenstreetmap-tile-server.html</a> to set up our own OSM server on Windows Server 2012 64-bit.</p>
<p>I edited generate_tiles.py and generated some tiles for Tuam town in Ireland to test this. I noticed that there are not many symbols included on zoom level 16, but much on zoom level 17 , below: notice this is the same crossroad:<br />
<img src="/upfiles/21191.png" alt="alt text" /> <img src="/upfiles/42383.png" alt="alt text" /></p>
<p>However we don't want to generate zoom level 17, because it takes an awful long time to generate so many small tiles even for a small town and we accually don't need such high zoom level. Instead we want to have ALL symbols to be included on zoom level 16 or even earlier. How to achieve this?</p>
<p>Thanks :-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-symbols" rel="tag" title="see questions tagged &#39;symbols&#39;">symbols</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jan '17, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f98ed179efe75af596090a497cefeb90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koles500&#39;s gravatar image" />
<p><span>Koles500</span><br />
<span class="score" title="68 reputation points">68</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koles500 has no accepted answers">0%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jan '17, 22:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</img>
</div>
</div>
<div id="comments-container-54196" class="comments-container">
<span id="54206"></span>
<div id="comment-54206" class="comment">
<div id="post-54206-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you both very much for responses, I will be working on this intensively in next days. Right now I want to add that I found newer build for Windows: <a href="https://dl.dropboxusercontent.com/u/63393258/osm2pgsql_testRelease.zip">https://dl.dropboxusercontent.com/u/63393258/osm2pgsql_testRelease.zip</a> linked on this page: <a href="http://awcull.com/2015/09/30/postgis-osm2pgsql-windows.html">http://awcull.com/2015/09/30/postgis-osm2pgsql-windows.html</a> However I am not sure if this is the newest build. How can I check this or where can I download newest build for Windows 64-bit? I am now running osm2pgsql for whole Europe in slim mode and I'm curious if this will work...</p>
</div>
<div id="comment-54206-info" class="comment-info">
<span class="comment-age">(20 Jan '17, 21:18)</span> <span class="comment-user userinfo">Koles500</span>
</div>
</div>
</div>
<div id="comment-tools-54196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54196-form-container" class="comment-form-container">
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

<span id="54204"></span>

<div id="answer-container-54204" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54204-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-54204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would not recommend rendering zoom 16 with all the icons of zoom 17, as the style is carefully crafted to display as much information as possible while keeping clarity. But if you really want to, you should check <a href="https://github.com/gravitystorm/openstreetmap-carto">openstreetmap-carto</a>, the commonly used style, that you would have to modify.</p>
<p>My first advice would be to run a Linux VM in HyperV (or other virtualization), it's free and easy to set up. Then you will a much more common setup and you will be able to find a lot more help !</p>
<p>For exemple you could follow this kind of tutorial (there are many) : <a href="https://www.linuxbabe.com/linux-server/openstreetmap-tile-server-ubuntu-16-04">openstreetmap-tile-server-ubuntu-16-04</a> Or the "official" <a href="https://switch2osm.org">switch2osm.org</a>.</p>
<p>With this kind of setup, tiles will be rendered on demand. Except if you force a render, as in the last step, in the first link they only pre-render down to zoom level 10. Then you can cheaply host a renderer that goes down to zoom 20 ! This way tiles are only calculated when someone needs them, and you can choose to store them or not.</p>
<p>There are probably ways to do the same thing with Windows, but I didn't find it quickly.</p>
<p>Sorry as I don't really answer to the question asked. But I really think it will be easier with Linux to find documentation.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '17, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-54204" class="comments-container">
<span id="54213"></span>
<div id="comment-54213" class="comment">
<div id="post-54213-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Regardless of OS, I'd definitely suggest working with a CartoCSS style definition rather than a raw mapnik one - it'll be much easier to understand. Some of the stuff at <a href="https://ircama.github.io/osm-carto-tutorials/">https://ircama.github.io/osm-carto-tutorials/</a> (which does include Windows examples) may be useful. Note that TileMill that's mentioned there isn't supported by the absolute latest "OSM Standard" style, but it'll work out of the box with a "fairly recent" one (one much newer than the style you are currently using).</p>
</div>
<div id="comment-54213-info" class="comment-info">
<span class="comment-age">(20 Jan '17, 23:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54204" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54204-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54202"></span>

<div id="answer-container-54202" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54202-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, note that the map style you are using from SVN is about four years old. Since then, all style development has happened in github.com/gravitystorm/openstreetmap-carto - so don't be surprised if your maps look very different from what you see on openstreetmap.org. However, switching to the newest style would also require newer version of Mapnik and osm2pgsql than referenced in the blog article so maybe youre safer to stay with what you have.</p>
<p>You can change the zoom level at which icons are displayed by modifying the right map style file. For example, the file <code>inc/layer-amenity-points.xml.inc</code> controls when amenities are shown. In there, you will for example see a section like this</p>
<pre><code>&lt;Rule&gt;
   &amp;maxscale_zoom17;
   &lt;Filter&gt;[amenity]=&#39;fast_food&#39;&lt;/Filter&gt;
   &lt;PointSymbolizer file=&quot;&amp;symbols;/fast_food.png&quot; placement=&quot;interior&quot;/&gt;
&lt;/Rule&gt;</code></pre>
<p>Change to <code>&amp;maxscale_zoom16;</code> and you're done - for fast food joints. You can of course do a search and replace too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '17, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jan '17, 20:13</strong> </span></p>
</div>
</div>
<div id="comments-container-54202" class="comments-container">
&#10;</div>
<div id="comment-tools-54202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54202-form-container" class="comment-form-container">
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


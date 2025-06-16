+++
type = "question"
title = "How to install MKGMAP?"
description = '''I have downloaded it, unzipped it and downloaded and installed the required Java platform but when I click on the file &quot;mkgmap&quot;, an executable jar file, nothing happens. Can someone tell what I am doing wrong?'''
date = "2010-12-14T21:50:00Z"
lastmod = "2013-04-15T15:06:00Z"
weight = 1809
keywords = [ "download", "map", "garmin" ]
aliases = [ "/questions/1809" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to install MKGMAP?](/questions/1809/how-to-install-mkgmap)

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
<span id="post-1809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1809-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have downloaded it, unzipped it and downloaded and installed the required Java platform but when I click on the file "mkgmap", an executable jar file, nothing happens.</p>
<p>Can someone tell what I am doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '10, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/5628aa29417d4023bd222cda5a55fad7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="discus277&#39;s gravatar image" />
<p><span>discus277</span><br />
<span class="score" title="299 reputation points">299</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="discus277 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1809" class="comments-container">
&#10;</div>
<div id="comment-tools-1809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1809-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="1810"></span>

<div id="answer-container-1810" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1810-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-1810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mkgmap is a command line program, and doesn't need installing as such. You just have to unzip it, then use Java to run it. Exactly how to do this will depend on what operating system you are using. Something like this from a command line will probably work (running it from the folder you unzipped Mkgmap into):</p>
<pre><code>java -jar  mkgmap.jar</code></pre>
<p>This command won't actually do anything, except output details of how to use Mkgmap. To actually generate a Garmin map, you will have to specify an input file, and probably some other options, depending on what you want to do. eg something like this will generate a map, with routing enabled, and a tdb file for Mapsource:</p>
<pre><code>java -ea -jar mkgmap.jar --tdbfile --route data.osm</code></pre>
<p>There is more details of how to use Mkgmap, and all of the available options, on the <a href="https://wiki.openstreetmap.org/wiki/Mkgmap">Mkgmap wiki page</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '10, 22:11</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-1810" class="comments-container">
&#10;</div>
<div id="comment-tools-1810" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1810-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2440"></span>

<div id="answer-container-2440" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2440-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As an example I'll describe what I do - hope it helps! This is on a Windows 7 PC and the paths to things not in the local directory will obviously be different in your case.</p>
<p>(if you haven't already) you'll need to download OSM data for the area that you're interested in. That will typically be as a .osm.bz2 file or a .pbf file. The ".osm" file format is XML (text based) and files in that format are large; with a .osm.bz2 download you'd unzip it with "bunzip2" (which if you haven't already installed you'll need to). The .pbf file format is a binary version of the same data and takes up less space than .osm. Newer versions only (since some time last year) of the mkgmap tools support .pbf format.</p>
<p>In my case (I'm interested in Great Britain) I download great_britain.osm.bz2 from Geofabrik here: <a href="http://download.geofabrik.de/osm/europe/">http://download.geofabrik.de/osm/europe/</a> I notice that there are some .pbfs available there for the US that might be suitable for you; also have a look on Cloudmade's site.</p>
<p>I'll then run "splitter" on it. If you haven't got that already it's available from the same place as mkgmap. This is run from the same directory as the (bunzipped) great_britain.osm:</p>
<pre><code>java -Xmx2000m -jar c:\\Doc\\eclipse\\workspace_lenovo\\splitter\\dist\\splitter.jar great_britain.osm --max-nodes=800000</code></pre>
<p>The "2000m" above is the amount of memory to allocate. I find that that vaue works on a Windows machine with 4Gb RAM; you might want to try a smaller number. The next argument is just the full path to "splitter.jar". The max-nodes setting is half the default; I found that I had to use that (to create twice as many tiles as would otherwise be needed) for routing to work.</p>
<p>"splitter" creates lots of .osm.gz files (44 in my case). The next thing that I do is run mkgmap:</p>
<pre><code>java -Xmx2000M -jar c:/Doc/eclipse/workspace_lenovo/mkgmap/dist/mkgmap.jar --style-file=C:\\Users\\SomeoneElse\\Downloads\\mkgmap-r1733\\resources\\styles\\default  --remove-short-arcs --levels=&quot;0=24, 1=22, 2=21, 3=19, 4=18, 5=16&quot; --location-autofill=3 --route --gmapsupp *.osm.gz</code></pre>
<p>The style file is part of the mkgmap download. I'd just use the default style to start with. The other arguments are ones that work for me. The final one "*.osm.gz" assumes that there aren't any other .osm.gz files in the current directory other than the ones that splitter has created. The "gmapsupp" argument says "please create a big file made up of all the small ones so I can put it straight on my GPS without messing about".</p>
<p>That creates lots of numbered .img files and these three important ones: gmapsupp.img (the actual map, large) and osmmap.tdb and osmmap.img (the map overview file, small)</p>
<p>Plug the Garmin into your PC and on the garmin go into setup, Interface, and select USB Mass Storage. Copy these three files to the "Garmin" directory on there (which should be visible on your PC). When copied disconnect and press the Garmin "off" button, that'll restart it not in mass storage mode and you should be able to see your new maps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '11, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '12, 13:01</strong> </span></p>
</div>
</div>
<div id="comments-container-2440" class="comments-container">
&#10;</div>
<div id="comment-tools-2440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2440-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21545"></span>

<div id="answer-container-21545" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21545-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I typed "java -jar mkgmap.jar" in the command line, while being in the mkgmap-folder (Windows command prompt), and I get the typical 'mkgmao is not recognized (etc)" answer. What am I doing wrong? Where should the commands be typed in, which command line?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '13, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0b62a9f5308f050deac73b7b9a2cdb37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MichelBruggeman&#39;s gravatar image" />
<p><span>MichelBruggeman</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MichelBruggeman has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '13, 15:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-21545" class="comments-container">
&#10;</div>
<div id="comment-tools-21545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21545-form-container" class="comment-form-container">
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


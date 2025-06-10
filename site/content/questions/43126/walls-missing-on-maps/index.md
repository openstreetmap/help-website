+++
type = "question"
title = "walls missing on maps"
description = '''I am fairly new to this, so try and be patient with me, I am joined openstreetmap and slowly getting used to how to add things to the database, and I am now trying to produce my own maps, I am using  Osmosis, Splitter and Mkgmap, the final output is okay, paths, roads etc etc, but I am a keen walker...'''
date = "2015-05-20T12:15:00Z"
lastmod = "2015-05-26T18:40:00Z"
weight = 43126
keywords = [ "mkgmap", "walls", "garmin" ]
aliases = [ "/questions/43126" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [walls missing on maps](/questions/43126/walls-missing-on-maps)

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
<span id="post-43126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43126-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am fairly new to this, so try and be patient with me, I am joined openstreetmap and slowly getting used to how to add things to the database, and I am now trying to produce my own maps, I am using</p>
<p>Osmosis, Splitter and Mkgmap, the final output is okay, paths, roads etc etc, but I am a keen walker and I would like to see walls on my maps, what switches do i need to use to make this happen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-walls" rel="tag" title="see questions tagged &#39;walls&#39;">walls</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '15, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/1a48846e2865ba49198e0fb8e4064358?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rossendale%20Gary&#39;s gravatar image" />
<p><span>Rossendale Gary</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rossendale Gary has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '15, 12:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-43126" class="comments-container">
&#10;</div>
<div id="comment-tools-43126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43126-form-container" class="comment-form-container">
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

<span id="43127"></span>

<div id="answer-container-43127" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43127-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I use</p>
<pre><code>barrier=wall [0x29 resolution 20]
barrier=fence [0x29 resolution 20]
barrier=hedge [0x29 resolution 20]</code></pre>
<p>in the "lines" style file between the "highway" and "railway" definitions. It draws them as powerlines, but that works for me. I'm using the default TYP file.</p>
<p>Edit: Actually a quick scan of the UK <a href="http://taginfo.openstreetmap.org.uk/keys/barrier?filter=ways#values">taginfo</a> suggests some other values that ought to be considered (wire_fence being one obvious candidate). When I was trying to work out how to render various barriers on an OSM-carto web map (unrelated to Garmin maps) I did some thinking about some of the more esoteric values. See <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/style.lua#L270">here</a> for the results of that if you're interested, though the actual code won't be directly useful to mkgmap, and note that OSM-carto has default barrier rendering and mkgmap by default hasn't, so not all the taginfo values are covered here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '15, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '15, 12:38</strong> </span></p>
</div>
</div>
<div id="comments-container-43127" class="comments-container">
<span id="43128"></span>
<div id="comment-43128" class="comment">
<div id="post-43128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the quick response, I guess i need to figure out how to get and edit a TYP file..</p>
</div>
<div id="comment-43128-info" class="comment-info">
<span class="comment-age">(20 May '15, 12:55)</span> <span class="comment-user userinfo">Rossendale Gary</span>
</div>
</div>
<span id="43129"></span>
<div id="comment-43129" class="comment">
<div id="post-43129-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For info I've never bothered using a TYP file to change how things appear - you don't need to find one to add those lines to the style (though many people do use them to create nicely styled Garmin maps, of course).</p>
</div>
<div id="comment-43129-info" class="comment-info">
<span class="comment-age">(20 May '15, 12:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="43130"></span>
<div id="comment-43130" class="comment">
<div id="post-43130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so where do i add those lines to the style ?</p>
</div>
<div id="comment-43130-info" class="comment-info">
<span class="comment-age">(20 May '15, 12:59)</span> <span class="comment-user userinfo">Rossendale Gary</span>
</div>
</div>
<span id="43131"></span>
<div id="comment-43131" class="comment">
<div id="post-43131-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Below the "mkgap" folder you'll probably see "resources", and below that "styles", and in there (among others) "default". Take a copy of the "default" folder (or the folder for whatever style you're using). In there you'll see a file "lines". Open that with a text editor, and edit as suggested above. Then specify the path to the style file in your "mkgmap" command "--style-file=\path\to\your_new_style"</p>
</div>
<div id="comment-43131-info" class="comment-info">
<span class="comment-age">(20 May '15, 13:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="43183"></span>
<div id="comment-43183" class="comment">
<div id="post-43183-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As a walker, the outline of fields is in my mind more important than the actual barrier type. A nice to have is simply barrier=field_boundary as a filler until more detail can be added. Many boundaries have a bit of hedge, a bit of wooden fence, some wire fence, a level of detail that is hard to map and not the most important thing. we need.</p>
</div>
<div id="comment-43183-info" class="comment-info">
<span class="comment-age">(24 May '15, 13:30)</span> <span class="comment-user userinfo">trigpoint</span>
</div>
</div>
</div>
<div id="comment-tools-43127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43127-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43159"></span>

<div id="answer-container-43159" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43159-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you decide you want to style your own map further the TYPWiz editor is a useful resource.</p>
<p><a href="http://www.pinns.co.uk/osm/typwiz4.html">http://www.pinns.co.uk/osm/typwiz4.html</a></p>
<p>There is other useful information on this website.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '15, 21:04</strong></p>
<img src="https://secure.gravatar.com/avatar/2ecce75f34e449d0ced44bf7aa6d6e06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dud1&#39;s gravatar image" />
<p><span>dud1</span><br />
<span class="score" title="401 reputation points">401</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dud1 has 3 accepted answers">30%</span></p>
</div>
</div>
<div id="comments-container-43159" class="comments-container">
<span id="43171"></span>
<div id="comment-43171" class="comment">
<div id="post-43171-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>correct me if I am wrong, but unless the information is in the mkgmap style files, then no matter what it won't be viewed, is that correct?</p>
<p>I have downloaded typwiz3, is there a big difference between 3 and 4?</p>
</div>
<div id="comment-43171-info" class="comment-info">
<span class="comment-age">(23 May '15, 08:36)</span> <span class="comment-user userinfo">Rossendale Gary</span>
</div>
</div>
<span id="43234"></span>
<div id="comment-43234" class="comment">
<div id="post-43234-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>My knowledge of this subject is quite limited but as far as I am aware if it isn't in the stle file directory your using "--style-file=...." it wont be rendered. I have found the process, one of trial and error. One thing you may want to do is create a simple map file of your own (i.e. stored on your own computer) with the relevant features you want to render and use this when developing your own style and typ files. You can create such a local map file using JOSM. If you have your gps connected you can copy the new garmin map file over and use basecamp to view the rendering whilst the gps is connected.</p>
<p>Another website that has some helpful information is: <a href="http://www.cferrero.net/maps/guide_to_TYPs.html">http://www.cferrero.net/maps/guide_to_TYPs.html</a></p>
<p>I've only used typwiz3. It has enabled me to produce garmin maps with different rendering for fences, hedges and walls along with different type of stiles all of which are helpful for me when surveying and navigating.</p>
</div>
<div id="comment-43234-info" class="comment-info">
<span class="comment-age">(26 May '15, 18:40)</span> <span class="comment-user userinfo">dud1</span>
</div>
</div>
</div>
<div id="comment-tools-43159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43159-form-container" class="comment-form-container">
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


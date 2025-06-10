+++
type = "question"
title = "Importing PDF JOSM"
description = '''Is there any page/link explaining how to use this function in JOSM? appreciate your answers, thanks'''
date = "2010-11-30T00:56:00Z"
lastmod = "2017-06-19T22:34:00Z"
weight = 1677
keywords = [ "josm", "import", "plugin", "pdf" ]
aliases = [ "/questions/1677" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Importing PDF JOSM](/questions/1677/importing-pdf-josm)

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
<span id="post-1677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1677-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there any page/link explaining how to use this function in JOSM? appreciate your answers, thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-pdf" rel="tag" title="see questions tagged &#39;pdf&#39;">pdf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '10, 00:56</strong></p>
<img src="https://secure.gravatar.com/avatar/92efd2ad1ae2f8664e9cca5f4d17281b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beerforfree&#39;s gravatar image" />
<p><span>Beerforfree</span><br />
<span class="score" title="94 reputation points">94</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beerforfree has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>30 Nov '10, 11:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/bc6d0b055d631830f7891d3f89edb66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katpatuka&#39;s gravatar image" />
<p><span>katpatuka</span><br />
<span class="score" title="1041 reputation points"><span>1.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span></p>
</div>
</div>
<div id="comments-container-1677" class="comments-container">
&#10;</div>
<div id="comment-tools-1677" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1677-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="1937"></span>

<div id="answer-container-1937" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1937-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-1937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>pdfimport is very powerful tool, but requires some learning and experimenting to get to grips with. Also, unfortunately, as of now, it has virtually no documentation. Here's quick-ish guide:</p>
<p>First, you'll need a PDF that</p>
<ul>
<li>You're legally allowed to use in OpenStreetMap</li>
<li>Is in a known coordinate system</li>
<li>Preferably has coordinate grid with labels</li>
</ul>
<p>Also you might need to tweak your JOSM setup too. pdfimport tends to use a lot of RAM, and you can run out of memory with more complex PDFs. Arrange so that your system has several gigs of RAM, and launch JOSM with "Xmx" option, like this "java -Xmx1024M -jar josm-latest.jar". You can put that command in <code>.sh</code> or <code>.bat</code> file for convenience.</p>
<p>So, this is how you import PDF in separate layer in JOSM:</p>
<ul>
<li>Open the pdfimport plugin from "Tools - Import PDF file"</li>
<li>Optionally tweak some settings in "Import settings" groupbox. The options there deal with filtering imported PDF data. If there's lots of garbage vector data in PDF file (like, lines used for creating fill patterns), tinkering with these options can turn import process and subsequent operations from unbearably slow to reasonably quick</li>
<li>Press on "Load file" , select your PDF</li>
<li>Select correct projection</li>
<li>The hardest part: georeference PDF by specifying coordinates for two reference points. Here coordinate grid comes in handy. Say, for bottom left corner:</li>
<li>Select a point somewhere in bottom left part of PDF file that is <em>precisely</em> on intersection of horizontal and vertical coordinate lines (sorry, don't know the right lingo)</li>
<li>Press on "Take X and Y from sel..." to fill "PDF X and Y" fields</li>
<li>Read coordinates for this point from PDF, and put them in "East and North" boxes. The measurement units for these are in meters, but coordinate grid is sometimes labelled with km's so you may need to multiply the numbers by 1000. Here's an illustration of where numbers end up:</li>
</ul>
<p><img src="http://img530.imageshack.us/img530/9462/coords.png" alt="alt text" /></p>
<ul>
<li>With coordinates and coordinate system in place, you're good to go. If you press "Show target", JOSM will place viewport over the region where PDF data will end up, useful for checking that you didn't mix up the numbers and your data is not going to appear on the other side of globe...</li>
<li>Press "Place", this will load vector data from PDF file into a separate JOSM data layer</li>
</ul>
<p>What happens next? Most likely imported PDF data is noisy and dirty, and requires some cleaning and tagging before it's good to upload. The best way to do this is to work in separate layers--select some stuff in your PDF layer, copy it to OSM layer, then clean up tags, fix overlapping issues etc. Importer adds a bunch of tags to imported nodes and ways, these are handy for semi-automating the cleanup process. The "Search" function in "Selection" panel is your friend!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '10, 23:43</strong></p>
<img src="https://secure.gravatar.com/avatar/49a5be1c12519dc592e6d1aafd8026e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cuu508&#39;s gravatar image" />
<p><span>cuu508</span><br />
<span class="score" title="136 reputation points">136</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cuu508 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Dec '10, 00:03</strong> </span></p>
</div>
</div>
<div id="comments-container-1937" class="comments-container">
&#10;</div>
<div id="comment-tools-1937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1937-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1678"></span>

<div id="answer-container-1678" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1678-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you haven't done this yet, you have to download the plugin "pdfimport" You can do this by going to Edit - Preferences - Plugins then click on "Download List" on the bottom. After a restart of JOSM you can use the plugin by going to Tools - Import PDF File A new window opens where you can select different settings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '10, 06:27</strong></p>
<img src="https://secure.gravatar.com/avatar/6889fe77c40ce982689c8b523f9edc10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twist3r&#39;s gravatar image" />
<p><span>twist3r</span><br />
<span class="score" title="246 reputation points">246</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twist3r has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '10, 08:47</strong> </span></p>
</div>
</div>
<div id="comments-container-1678" class="comments-container">
&#10;</div>
<div id="comment-tools-1678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1678-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="30166"></span>

<div id="answer-container-30166" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30166-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Could you not use a map warper program and simply use the resulting co-ordinates to make it a background image?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '14, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/66001846f0632f073fa821d84341d7cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Azzitizz&#39;s gravatar image" />
<p><span>Azzitizz</span><br />
<span class="score" title="445 reputation points">445</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Azzitizz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30166" class="comments-container">
&#10;</div>
<div id="comment-tools-30166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30166-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56655"></span>

<div id="answer-container-56655" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56655-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So, I've installed pdfimport with the idea using a pdf as a guiding layer to fix osm data. Not quite sure if that's what you had in mind. But...</p>
<p>First problem: There is no "Tools - Import PDF file"</p>
<p>Is pdfimport maintained and up-to-date?</p>
<p>The pdf in question (5.5M): <a href="http://www.dot.state.mn.us/metro/projects/hwy100slp/pdf/projectmap.pdf">http://www.dot.state.mn.us/metro/projects/hwy100slp/pdf/projectmap.pdf</a></p>
<p>Permission to use granted at www.dot.state.mn.us/information/disclaimer.html section "Maps and related data".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '17, 03:15</strong></p>
<img src="https://secure.gravatar.com/avatar/b55060683074e39c1ba64a93572468ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rhardy&#39;s gravatar image" />
<p><span>rhardy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rhardy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56655" class="comments-container">
<span id="56683"></span>
<div id="comment-56683" class="comment">
<div id="post-56683-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Found at "Imagery - More - Import PDF file".</p>
<p>And it works. The PDF has no coordinate system, so I left the importer at the default, then found (approximately) matching nodes in the pdf and the osm data. It was about 4 meters off at the north end of the pdf, and 1 meter off at the south, which I took to be good enough.</p>
</div>
<div id="comment-56683-info" class="comment-info">
<span class="comment-age">(19 Jun '17, 22:34)</span> <span class="comment-user userinfo">rhardy</span>
</div>
</div>
</div>
<div id="comment-tools-56655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56655-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1679"></span>

<div id="answer-container-1679" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1679-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So far I came too. I tried last night to make some imports but it look like no overlap with OSM data is possible or at least I haven't been able to see both stuff together. On the other hand I came to the problem of how to geo-referencing it since I don't have the exact coordinates of both edges, so I tried first with aprox. coordinates</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '10, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/92efd2ad1ae2f8664e9cca5f4d17281b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beerforfree&#39;s gravatar image" />
<p><span>Beerforfree</span><br />
<span class="score" title="94 reputation points">94</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beerforfree has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1679" class="comments-container">
&#10;</div>
<div id="comment-tools-1679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1679-form-container" class="comment-form-container">
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


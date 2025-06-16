+++
type = "question"
title = "Problem: Creating a MultiPolygon with JOSM and convert it with osm2poly.pl"
description = '''Dear all, first of all I want to thank you in advance for even reading my post and any effort you will put into helping me. I highly appreciate your expertise and time you spend to help me. Now to the problem: I discovered OSM on Friday to solve a problem that I have. For a certain area, I want to e...'''
date = "2018-02-17T14:30:00Z"
lastmod = "2018-02-21T16:47:00Z"
weight = 62177
keywords = [ "josm", "osmconvert", ".osm", "multipolygon" ]
aliases = [ "/questions/62177" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problem: Creating a MultiPolygon with JOSM and convert it with osm2poly.pl](/questions/62177/problem-creating-a-multipolygon-with-josm-and-convert-it-with-osm2polypl)

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
<span id="post-62177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62177-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all,</p>
<p>first of all I want to thank you in advance for even reading my post and any effort you will put into helping me. I highly appreciate your expertise and time you spend to help me.</p>
<p>Now to the problem:</p>
<p>I discovered OSM on Friday to solve a problem that I have. For a certain area, I want to extract all the street names. Originally, I would just go to Google Maps and click on every street to get the street name, but I think that is very inefficient and I want to make it way easier. When it comes to coding etc, I am a total noob and I don't really know what I am doing.</p>
<p>So I stumbled upon this Question <a href="/questions/2980/how-do-i-list-all-the-streets-in-a-city-with-nominatim">here</a> to help my problem.</p>
<p>It is very useful, so far I installed Osmosis and got it running. The country that I want data from is Portugal. I managed to get the street names from a rectangle, however, the areas that I want are more complex like a mulitpolygon.</p>
<p>For that, I downloaded JOSM and its here where the first problem starts. I have no clue if I do it the right way, but I basically downloaded the GPS data from Lisbon. Actually I just needed the satellite map, but I had no idea how to get that on JOSM. Then I drew some nodes of my area and made it into a Multipolygon and saved it as an osm.file. I provide a link so you get the picutre:</p>
<p><img src="https://imgur.com/fdggYc6.jpg" title="Multipolygon" alt="alt text" /></p>
<p>Not sure if I am on the right track, but I downloaded Perl and installed it. In the Command line I put:</p>
<p>"perl PathToOSM2PolyScript PathToMultipolyFile"</p>
<p>The results were correct like the ones in the Question link that I posted, however here is the big problem: How do I get the results into a .poly file that can be read by Osmosis? This is where I am stuck.</p>
<p>Additionally, the last thing whats missing is then to filter the .osm file that contains all the data. I figured I can just open the .osm file with Excel and I get so much data, but how to I filter only for the street names?</p>
<p>I saw that in the Answer to the posted Question, the guy provided a line like this:</p>
<p>"sed -n 's/.*k="name" v="//;T;s|"/&gt;||;p' Stockholm-names.osm |sort -u"</p>
<p>But where is that line put into? How does it work?</p>
<p>You guys see, I am not an expert in IT, but its really on my heart now to solve this problem. I tried to go ahead as far as I can all by myself. But now I got to a point where I can't go any further without help. So I am sorry to bother you guys, but please do help me with any solutions or suggestions.</p>
<p>Thank you in advance</p>
<p>Kind regards, Tom</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '18, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/0729d376314f797f5c9fef112b505582?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J4ckaroo&#39;s gravatar image" />
<p><span>J4ckaroo</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J4ckaroo has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '18, 19:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62177" class="comments-container">
&#10;</div>
<div id="comment-tools-62177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62177-form-container" class="comment-form-container">
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

<span id="62178"></span>

<div id="answer-container-62178" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62178-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="J4ckaroo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Regarding your first question, how to create the extract you are looking for: You could download the "poly" plugin for JOSM which would allow you to save your polygon directly as a .poly file, no need for osm2poly then, followed by the appropriate osmosis (or osmium-tool) command. OR go the extracts.bbbike.org where you can draw your polygon on the web site and request an extract for exactly that polygon, no further tools needed!</p>
<p>Regarding your second question, how to get all street names in an extract, there are many different ways to do that but since you already have JOSM, you could try to load the file in JOSM, then select everything that has a highway tag and a name tag (the search box is quite informative), and save just the selected objects into a new file (you might need to create a new and empty file and copy over the selection). In the resulting XML file, find all lines that look like</p>
<pre><code>&lt;tag k=&#39;name&#39; v=&#39;something&#39; /&gt;</code></pre>
<p>and you have your names.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '18, 23:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62178" class="comments-container">
<span id="62214"></span>
<div id="comment-62214" class="comment">
<div id="post-62214-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik Ramm, thank you so much! You have no idea how much you helped me! I really appreciate it, you are my most favourite person of the month, hahah!</p>
<p>I can't thank you enough!</p>
<p>The last thing I need is only, how do I execute the code that you used? With which program and where? Remember I am a noob :p</p>
<p>Cheers!</p>
</div>
<div id="comment-62214-info" class="comment-info">
<span class="comment-age">(19 Feb '18, 17:04)</span> <span class="comment-user userinfo">J4ckaroo</span>
</div>
</div>
<span id="62217"></span>
<div id="comment-62217" class="comment">
<div id="post-62217-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If by "how do I execute the code that you used" you mean "how do I find all lines that look like ... after I have saved all highways to a separate file in JOSM" then the answer is that there are many ways to do it. On Linux I would use the "grep" utility, writing something like</p>
<pre><code>grep &quot;&lt;tag k=&#39;name&#39;&quot; my-saved-file.osm | cut -d\&#39; -f4 | sort -u &gt; allnames.txt</code></pre>
<p>but you could, for example, simply load the file you have saved into a word processor or spreadsheed program and then sort all lines, and identify the block that begins with "&lt;tag k='name'" manually...</p>
</div>
<div id="comment-62217-info" class="comment-info">
<span class="comment-age">(19 Feb '18, 21:42)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="62258"></span>
<div id="comment-62258" class="comment">
<div id="post-62258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I managed, thank you sooooo much!!!</p>
</div>
<div id="comment-62258-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 16:47)</span> <span class="comment-user userinfo">J4ckaroo</span>
</div>
</div>
</div>
<div id="comment-tools-62178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62178-form-container" class="comment-form-container">
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


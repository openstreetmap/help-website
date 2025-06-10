+++
type = "question"
title = "Problem using gosmore to rebuild a .pak file from osm data"
description = '''I&#x27;m searching for an application or API that does routing. I only need the route and length/time of the route. After doing some research I had the impression gosmore is the appropriate one. I have downloaded and built it according to the wiki http://wiki.openstreetmap.org/wiki/Gosmore#Downloading_an...'''
date = "2011-04-14T12:42:00Z"
lastmod = "2011-04-14T16:40:00Z"
weight = 4481
keywords = [ "gosmore", "routing" ]
aliases = [ "/questions/4481" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Problem using gosmore to rebuild a .pak file from osm data](/questions/4481/problem-using-gosmore-to-rebuild-a-pak-file-from-osm-data)

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
<span id="post-4481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4481-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm searching for an application or API that does routing. I only need the route and length/time of the route. After doing some research I had the impression gosmore is the appropriate one. I have downloaded and built it according to the wiki <a href="http://wiki.openstreetmap.org/wiki/Gosmore#Downloading_and_running"></a><a href="http://wiki.openstreetmap.org/wiki/Gosmore#Downloading_and_running"></a><a href="http://wiki.openstreetmap.org/wiki/Gosmore#Downloading_and_running">http://wiki.openstreetmap.org/wiki/Gosmore#Downloading_and_running</a>. I'm using ubuntu 10.04.2 but didn't take the ubuntu one because I want it to run it headless.</p>
<p>First I tried a ready made .pak file to try gosmore out. But whatever QUERY_STRING I've provided, no route is found by gosmore. Then I tried to rebuild the pak file from a german osm data file. First it ended with a 3k sized .pak file. Then I recognized it needs somehow the elemstyles.xml. The next try was to do the rebuild in the source directory of gosmore where all these files are. But doing this</p>
<pre><code>bzcat germany.osm.bz2 | ./gosmore rebuild</code></pre>
<p>I get</p>
<pre><code>488 for (pairs = 0; pairs &lt; PAIRS &amp;&amp; s2grp &lt; S2GROUP (0) + S2GROUPS; )
489 for (pairs = 0; pairs &lt; PAIRS &amp;&amp; s2grp &lt; S2GROUP (0) + S2GROUPS; )
490 for (pairs = 0; pairs &lt; PAIRS &amp;&amp; s2grp &lt; S2GROUP (0) + S2GROUPS; )
491 for (ndType *ndItr = ndBase; ndItr &lt; ndBase + hashTable[bucketsMin1 + 1]; ndItr++)
terminate called after throwing an instance of &#39;std::bad_alloc&#39;
 what():  std::bad_alloc
Building gosmore.pak using style elemstyles.xml...</code></pre>
<p>So now I'm not really sure to where head next. It is a situation like often that a lot of people seem to use it and are satisified and then there are a few where it doesn't and not much help to solve. Documentation is just not existent.</p>
<p>Did I do something terribly wrong? Is there a better library for routing then gosmore? Any hints appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gosmore" rel="tag" title="see questions tagged &#39;gosmore&#39;">gosmore</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '11, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/69ffbfbb81efe94561dbc0d9d90d7d13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Norbert%20Hartl&#39;s gravatar image" />
<p><span>Norbert Hartl</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Norbert Hartl has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4481" class="comments-container">
<span id="4489"></span>
<div id="comment-4489" class="comment">
<div id="post-4489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I got something back. Thanks, guys. The conversion of germany osm with gosmore rebuild ate happily 3GB of main memory. Before I only had a little bit more than 2GB free and thought it would be sufficient. So the thing (the error) in my question is due to memory limit. And with the self converted pak file I get routing information while I wasn't successful with the prebuilt paks.</p>
</div>
<div id="comment-4489-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 13:53)</span> <span class="comment-user userinfo">Norbert Hartl</span>
</div>
</div>
</div>
<div id="comment-tools-4481" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4481-form-container" class="comment-form-container">
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

<span id="4482"></span>

<div id="answer-container-4482" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4482-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This web site is not intended to be a bug tracking system. If you look at Gosmore's <a href="http://wiki.openstreetmap.org/wiki/Gosmore#Bugs">Wiki page</a> you will find a reference to the trac system where you can report problems.</p>
<p>If I were to guess from the error message, I'd say maybe your machine has run out of memory. Did you monitor memory usage while running the program?</p>
<p>I think gosmore is well suited for what you have in mind. There are other systems around that you could use just as well, for example <a href="http://wiki.openstreetmap.org/wiki/Routino">Routino</a> or <a href="http://wiki.openstreetmap.org/wiki/OSRM">OSRM</a>, both of which are AGPL licensed and support (only) headless operation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '11, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-4482" class="comments-container">
<span id="4485"></span>
<div id="comment-4485" class="comment">
<div id="post-4485-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, often a question looks like a ticket even if it isn't intended :) And it sometimes hard to ask the right things if you are really new to some technology. Thanks for the hint to monitor the memory. I was just assuming it can deal with low mem situation itself. I'm monitoring now</p>
</div>
<div id="comment-4485-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 13:03)</span> <span class="comment-user userinfo">Norbert Hartl</span>
</div>
</div>
</div>
<div id="comment-tools-4482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4482-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4483"></span>

<div id="answer-container-4483" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4483-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My first guess is that you created an incompatible relations.tbl file. If you did, you can delete it and rebuild without it (it is not important for routing).</p>
<p>You can also disable some of the code with the <code>ONLY_ROUTING</code> flag, e.g.</p>
<pre><code>  make CFLAGS=&#39;-O2 -DRES_DIR=\&quot;/usr/share/gosmore/\&quot; -DHEADLESS -DONLY_ROUTING&#39;</code></pre>
<p>But it can be a completely unrelated bug.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '11, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/d25927545eb18b4d577280081df5ce6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic%20Roets&#39;s gravatar image" />
<p><span>Nic Roets</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic Roets has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '11, 13:07</strong> </span></p>
</div>
</div>
<div id="comments-container-4483" class="comments-container">
<span id="4484"></span>
<div id="comment-4484" class="comment">
<div id="post-4484-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did not cerate a relations.tbl. I do not know what it is for. And the second line in the log says "Processing without relations table".</p>
</div>
<div id="comment-4484-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 12:58)</span> <span class="comment-user userinfo">Norbert Hartl</span>
</div>
</div>
<span id="4490"></span>
<div id="comment-4490" class="comment">
<div id="post-4490-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm glad I came back so I found the second option for only routing. Nice now it works. It is just strange (well) that I get only time based information per leg and not distance. Where to ask this? :)</p>
</div>
<div id="comment-4490-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 16:19)</span> <span class="comment-user userinfo">Norbert Hartl</span>
</div>
</div>
<span id="4491"></span>
<div id="comment-4491" class="comment">
<div id="post-4491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Gosmore does not produce the distance because the values used internally are not particularly accurate. Approximating the distances from lat/long is quite easy e.g. using the equirectangular projection. Or you can use the YOURS php wrapper, some versions of which will also generate instructions.</p>
<p>Note that the "time" values are not accurate for shortest route.</p>
</div>
<div id="comment-4491-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 16:40)</span> <span class="comment-user userinfo">Nic Roets</span>
</div>
</div>
</div>
<div id="comment-tools-4483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4483-form-container" class="comment-form-container">
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


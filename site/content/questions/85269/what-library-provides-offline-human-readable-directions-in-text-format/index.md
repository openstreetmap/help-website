+++
type = "question"
title = "What library provides Offline Human Readable Directions in Text format?"
description = '''Goal:  Offline Directions (No external API&#x27;s to Clouds or 2 computers connected to each other) Human Readable directions returned in a String format (no api&#x27;s that return nodes with triple nested brackets, no GUI&#x27;s that create images) It would look like, &quot;Turn left on Bobsland NW and go 100ft, ...&quot;....'''
date = "2022-08-02T03:19:00Z"
lastmod = "2022-08-02T03:19:00Z"
weight = 85269
keywords = [ "offline", "routing", "humanreadable" ]
aliases = [ "/questions/85269" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What library provides Offline Human Readable Directions in Text format?](/questions/85269/what-library-provides-offline-human-readable-directions-in-text-format)

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
<span id="post-85269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85269-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Goal:</p>
<ol>
<li>Offline Directions (No external API's to Clouds or 2 computers connected to each other)</li>
<li>Human Readable directions returned in a String format (no api's that return nodes with triple nested brackets, no GUI's that create images) It would look like, "Turn left on Bobsland NW and go 100ft, ...".</li>
<li>Can be called from C++ or Python</li>
<li>Runs on Raspberry Pi</li>
</ol>
<p>This is what sketch of what it should look like:</p>
<pre><code>/*
import selfhostedAPIthing;
&#10;selfhostedAPIthing myNav = new selfhostedAPIthing;
myNav.setOSMFile(&quot;C://Programs/MyApp/OSMExtract/planet.osm&quot;);
&#10;String destination;
String modeOfTravel= &quot;walk&quot;;
String unitSystem= &quot;metric&quot;;
sendToMyCustumAppFunction(myNav.getDirections(GPS.getXY(), destination, modeOfTravel, unitSystem));
*/</code></pre>
<p>Thanks in advance</p>
<p>Suggestions: If you maintain a library that does this, consider mentioning the term human readable directions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-humanreadable" rel="tag" title="see questions tagged &#39;humanreadable&#39;">humanreadable</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '22, 03:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ab558c17c2c46a690e7cde467dfb1f8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PhysicsArmature&#39;s gravatar image" />
<p><span>PhysicsArmature</span><br />
<span class="score" title="89 reputation points">89</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PhysicsArmature has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85269" class="comments-container">
&#10;</div>
<div id="comment-tools-85269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85269-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>


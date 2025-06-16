+++
type = "question"
title = "How to mass edit nodes with specific tags in JOSM?"
description = '''I screwed up. I did a lot of work editing Tiger data in my hometown of Homer, Alaska. Afterward I read about updating the Tiger-reviewed tag on all those ways so that subsequent Tiger imports wouldn&#x27;t overwrite my changes. Not wanting to edit each way individually I merely selected multiple ways in ...'''
date = "2013-04-14T15:25:00Z"
lastmod = "2014-11-28T00:29:00Z"
weight = 21524
keywords = [ "mass_tagging", "josm", "bulk_editing" ]
aliases = [ "/questions/21524" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to mass edit nodes with specific tags in JOSM?](/questions/21524/how-to-mass-edit-nodes-with-specific-tags-in-josm)

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
<span id="post-21524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21524-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I screwed up. I did a lot of work editing Tiger data in my hometown of Homer, Alaska. Afterward I read about updating the Tiger-reviewed tag on all those ways so that subsequent Tiger imports wouldn't overwrite my changes. Not wanting to edit each way individually I merely selected multiple ways in JOSM and changed the Tiger tags to Tiger-reviewed=yes. A dozen or so big selections later I was done.</p>
<p>Earlier this week I discovered to my surprise and chagrin that every single NODE included in my selections now carries the Tiger_reviewed=yes tag. That was certainly not expected and I would lke a way to undo those changes. A roll-back is not desirable because a ton of other useful edits would get tossed with the Tiger tags.</p>
<p>I could do what I need to do in a desktop database like Access with a fairly simple SQL statement but the OSM database is a different beast altogether.</p>
<p>My question: Is there any way to select just those nodes that have the Tiger_reviewed=yes tagging in my neighborhood and delete that tag? The ways are fine with that tagging of course. It's just the nodes I want to strip of Tiger tags.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mass_tagging" rel="tag" title="see questions tagged &#39;mass_tagging&#39;">mass_tagging</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-bulk_editing" rel="tag" title="see questions tagged &#39;bulk_editing&#39;">bulk_editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '13, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '13, 19:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-21524" class="comments-container">
&#10;</div>
<div id="comment-tools-21524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21524-form-container" class="comment-form-container">
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

<span id="21526"></span>

<div id="answer-container-21526" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21526-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Type the following in the search box in JOSM</p>
<blockquote>
<p>Tiger_reviewed:yes type:node</p>
</blockquote>
<p>More examples of search queries: <a href="https://wiki.openstreetmap.org/wiki/JOSM_search_function">https://wiki.openstreetmap.org/wiki/JOSM search function</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '13, 18:05</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-21526" class="comments-container">
<span id="21527"></span>
<div id="comment-21527" class="comment">
<div id="post-21527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried every combination of your suggested query that I could come up with.</p>
<p>Tiger_reviewed:yes type:node</p>
<p>type:node key:"tiger:reviewed=yes"</p>
<p>type:node tiger:reviewed</p>
<p>type:node key:tiger:reviewed</p>
<p>and even</p>
<p>type:node key:tiger yes</p>
<p>None of these produced results. I tried them both with and without an active selection. WTF?</p>
<p>Finally I hit on simply selecting ALL nodes, i.e., only the words type:node in the search box. I discovered that the nodes making up the ways I tagged do not inherit tags from their "parents" so when the results appeared I merely deleted the tiger:reviewed tag. It affected nodes only, which is just what I wanted.</p>
<p>Thanks for your help...</p>
</div>
<div id="comment-21527-info" class="comment-info">
<span class="comment-age">(14 Apr '13, 19:24)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="38863"></span>
<div id="comment-38863" class="comment">
<div id="post-38863-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try ("tiger:reviewed"=yes) (type:node)</p>
<p>By the way, am I doing it wrong? Instead of changing tiger:reviewed=no to yes I delete the tag.</p>
</div>
<div id="comment-38863-info" class="comment-info">
<span class="comment-age">(27 Nov '14, 03:09)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-21526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21526-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38850"></span>

<div id="answer-container-38850" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38850-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's an example of doing a mass change. Let's say you forgot to add "http://" in front of every 'website' url tag you added and now want to correct this.</p>
<p>In Overpass turbo, you can select your area/edits by modifying the following query:</p>
<pre><code>[out:xml][timeout:25];
// gather results
(
  node[&quot;website&quot;~&quot;^[^h][^t][^t][^p].*&quot;]({{bbox}});
  way[&quot;website&quot;~&quot;^[^h][^t][^t][^p].*&quot;]({{bbox}});
  relation[&quot;website&quot;~&quot;^[^h][^t][^t][^p].*&quot;]({{bbox}});
);
// print results
out meta;
&gt;;
out meta qt;</code></pre>
<p>You can then open the results of this query in JOSM, and save it to a .osm file. After it's saved, you can use xmlstarlet to modify the tag. You also need to add 'action=modify' to the nodes you changed. Finally, compare the original and your edited file.</p>
<pre><code>xmlstarlet ed -P -u &quot;//tag[@k=&#39;website&#39;]/@v&quot;  -x &#39;concat(&quot;http://&quot;, .)&#39;  ~/Desktop/websites.osm &gt; ~/Desktop/websites-edit.osm
xmlstarlet ed -L -i &quot;//tag[@k=&#39;website&#39;]/..&quot;  -t &#39;attr&#39; -n &#39;action&#39; -v &#39;modify&#39; ~/Desktop/websites-edit.osm 
diff -y -W421 ~/Desktop/websites.osm ~/Desktop/websites-edit.osm | less</code></pre>
<p>Load the edited file into JOSM, validate it, and upload.</p>
<p>Of course the usual caveats regarding mass edits apply, so make sure you are only fixing your own mistakes or have circulated you change with correct mailing list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '14, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/f221969d01bf7d2a0707c85897d84ec5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brianegge&#39;s gravatar image" />
<p><span>brianegge</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brianegge has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38850" class="comments-container">
<span id="38865"></span>
<div id="comment-38865" class="comment">
<div id="post-38865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Brian,</p>
<p>I did those edits long ago in JOSM but your answer intrigues me nonetheless. Lets say I want to substitute one sub-string for different one? These are all my own additions I'm wanting to edit. It's a special case where I used a description:en tag set to Mile Zero Milestone and want to change that to read Kilometer Zero Milestone. There is other information in the description:en that I want to keep which is why I want only to replace the word "Mile" with the word "Kilometer".</p>
</div>
<div id="comment-38865-info" class="comment-info">
<span class="comment-age">(27 Nov '14, 07:40)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="38866"></span>
<div id="comment-38866" class="comment">
<div id="post-38866-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A quick look at xmlstarlet convinced me that I don't want to learn its intricacies at the moment. So perhaps you'd be willing to provide the command line? By the way, I'm running Windows, not Unix, and there are approximately 40 nodes (no ways or relations) that need editing.</p>
<p>Thanks again Dave</p>
</div>
<div id="comment-38866-info" class="comment-info">
<span class="comment-age">(27 Nov '14, 07:40)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="38871"></span>
<div id="comment-38871" class="comment">
<div id="post-38871-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>xmlstarlet is tricky - but powerful. The two commands I wrote should have been able to have been written as one, but I couldn't figure it out. You can use a text editor to do search/replace. For 40 nodes, it might be easiest to edit them manually in JSOM. You can do 'Search Next', and then edit your tag.</p>
</div>
<div id="comment-38871-info" class="comment-info">
<span class="comment-age">(27 Nov '14, 12:01)</span> <span class="comment-user userinfo">brianegge</span>
</div>
</div>
<span id="38873"></span>
<div id="comment-38873" class="comment">
<div id="post-38873-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For JOSM the todo list plugin can also become helpful for such tasks.</p>
</div>
<div id="comment-38873-info" class="comment-info">
<span class="comment-age">(27 Nov '14, 13:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="38888"></span>
<div id="comment-38888" class="comment">
<div id="post-38888-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you both for responding. I can do this edit in JOSM, and yes, the ToDo list plugin is helpful. I've used it before in similar situations. I want to eventually learn how to download OSM data into a local postgreSQL database and manipulate it with SQL commands, with which I am already familiar. The mention of xmlstarlet got me thinking along those lines.</p>
<p>Cheers</p>
</div>
<div id="comment-38888-info" class="comment-info">
<span class="comment-age">(28 Nov '14, 00:29)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-38850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38850-form-container" class="comment-form-container">
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


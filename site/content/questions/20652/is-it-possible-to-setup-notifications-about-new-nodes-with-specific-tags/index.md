+++
type = "question"
title = "Is it possible to setup notifications about new nodes with specific tags?"
description = '''There is a problem with misusing name tag to map node types instead of proper nouns. Can I somehow setup a notification for new nodes with name=some_type ? Related: How to find a bot maintainer to suggest additional replace conditions?'''
date = "2013-03-12T01:17:00Z"
lastmod = "2013-03-12T20:37:00Z"
weight = 20652
keywords = [ "notification", "name" ]
aliases = [ "/questions/20652" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to setup notifications about new nodes with specific tags?](/questions/20652/is-it-possible-to-setup-notifications-about-new-nodes-with-specific-tags)

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
<span id="post-20652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20652-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a problem with misusing name tag to map node types instead of <a href="http://en.wikipedia.org/wiki/Proper_noun">proper nouns</a>. Can I somehow setup a notification for new nodes with name=some_type ?</p>
<p>Related: <a href="/questions/20647/how-to-find-a-bot-maintainer-to-suggest-additional-replace-conditions">How to find a bot maintainer to suggest additional replace conditions?</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-notification" rel="tag" title="see questions tagged &#39;notification&#39;">notification</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '13, 01:17</strong></p>
<img src="https://secure.gravatar.com/avatar/1aaaf77e89ed1b496cefd433400ebf27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="int_ua&#39;s gravatar image" />
<p><span>int_ua</span><br />
<span class="score" title="275 reputation points">275</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="int_ua has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20652" class="comments-container">
&#10;</div>
<div id="comment-tools-20652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20652-form-container" class="comment-form-container">
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

<span id="20662"></span>

<div id="answer-container-20662" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20662-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="int_ua has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's a good idea to improve data quality.</p>
<p>Please have a look at <a href="http://osm102.openstreetmap.fr/~zorglub/watch/">http://osm102.openstreetmap.fr/~zorglub/watch/</a></p>
<p>Another approach would be to call from your browser once a day or more often a link like</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[out:json];node[name=some_type];out;</code></pre>
<p>It will list all nodes that exist with the given tag. For example</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[out:json];node[name=highway];out;</code></pre>
<p>has two hits.</p>
<p>As in your case most likely no legitimate case exists, you can work by hand through all found objects and correct their tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '13, 07:34</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '13, 09:46</strong> </span></p>
</div>
</div>
<div id="comments-container-20662" class="comments-container">
<span id="20677"></span>
<div id="comment-20677" class="comment">
<div id="post-20677-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The Firefox addon <span>Update Scanner</span> may be useful for automatic scanning the overpass result page for changes. Be SURE to set the scan interval to daily or even weekly to avoid unnecessary load on the server. Maybe using <span>IFTTT</span> would be another option.</p>
</div>
<div id="comment-20677-info" class="comment-info">
<span class="comment-age">(12 Mar '13, 20:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20662" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20662-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20663"></span>

<div id="answer-container-20663" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20663-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-20663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have a little Unix command line skills, it is easy to do:</p>
<ul>
<li>use Osmosis with the <code>--rri</code> task to download all changes since you last ran the program;</li>
<li>run the result past the "oscgrep" program (<a href="http://svn.openstreetmap.org/applications/utils/filter/oscgrep/)">http://svn.openstreetmap.org/applications/utils/filter/oscgrep/)</a> using the flags <code>-a create -t node</code> to search only for new nodes, and the flag <code>-r 'k="name" v="Toilet"'</code> to find those where this tag has been used.</li>
</ul>
<p>Please do not use such a mechanism to indiscriminately "fix" things the world over; such editing would be subject to the <a href="wiki.openstreetmap.org/wiki/Mechanical_Edit_Policy">Mechanical Edit Policy</a> and you would have to achieve community consenus on whether your edits are desirable first.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '13, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20663" class="comments-container">
&#10;</div>
<div id="comment-tools-20663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20663-form-container" class="comment-form-container">
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


+++
type = "question"
title = "why are there changesets with no edits existing (in the OSM history dump)?"
description = '''Hi, I am exploring the history of contributions using the OSM history dump (see wiki Planet.osm/full). Looking at the provided data, I found 24707 changesets in which there were no edits.  Someone has an idea about what happened with these datasets? '''
date = "2014-10-28T18:54:00Z"
lastmod = "2014-10-30T12:28:00Z"
weight = 38057
keywords = [ "changeset", "edits", "dump", "history" ]
aliases = [ "/questions/38057" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [why are there changesets with no edits existing (in the OSM history dump)?](/questions/38057/why-are-there-changesets-with-no-edits-existing-in-the-osm-history-dump)

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
<span id="post-38057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38057-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am exploring the history of contributions using the OSM history dump (see wiki Planet.osm/full). Looking at the provided data, I found 24707 changesets in which there were no edits.</p>
<p>Someone has an idea about what happened with these datasets?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-edits" rel="tag" title="see questions tagged &#39;edits&#39;">edits</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '14, 18:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Oct '14, 23:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-38057" class="comments-container">
&#10;</div>
<div id="comment-tools-38057" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38057-form-container" class="comment-form-container">
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

<span id="38060"></span>

<div id="answer-container-38060" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38060-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-38060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The API 0.6 method <a href="http://wiki.openstreetmap.org/wiki/API_v0.6#Create:_PUT_.2Fapi.2F0.6.2Fchangeset.2Fcreate">'create changeset'</a> allows you to create a changeset without doing any subsequent additions to that changeset. Reason might be anything from broken uploads (e.g. network issues), editor bugs, etc..</p>
<p>I even remember one case where a mapper created a huge number of such empty changesets to make hostile vandalism activities a bit more difficult to deal with. Yes, strange things happen some time, but all that got sorted out fairly quickly.</p>
<p>Update: as Simon provided some editor specific insights, I thought I could add some statistics from by local DB. It's about half a year old, but you should get a rough impression, which editors created how many empty changesets (if they identify themselves by name). You could of course group the entries by editor type (ignoring different editor versions, languages) - this is left as an exercise to the reader.</p>
<pre><code>                                  created_by                                   |   c   
-------------------------------------------------------------------------------+-------
                                                                               | 50761
 Potlatch 0.11b                                                                | 46702
 Potlatch 1.4 (live en)                                                        | 42190
 Potlatch 1.0                                                                  | 39909
 Potlatch 2                                                                    | 38173
 Potlatch 0.11                                                                 | 35890
 Potlatch 1.4 (live de)                                                        | 31094
 Potlatch 1.2                                                                  | 24265
 Go Map!! 1.1                                                                  | 22264
 Potlatch 1.1a                                                                 | 16447
 Potlatch 1.2a                                                                 | 15092
 Potlatch 0.11a                                                                | 14166
 Potlatch 1.2b                                                                 | 11621
 ArcGIS Editor for OpenStreetMap (2.0)                                         | 11466
 Potlatch 1.2c (live)                                                          |  9622
 osmitter 0.1                                                                  |  9548
 Potlatch 1.3e (live en)                                                       |  9079
 JOSM                                                                          |  7920
 Potlatch 1.4 (live ru)                                                        |  7848
 Potlatch 1.4 (live fr)                                                        |  7273
 iD 1.3.7                                                                      |  7147
 iD 1.3.4                                                                      |  6990</code></pre>
<p>Statement:</p>
<pre><code>select created_by,count(*) c from changes where num_changes = 0 group by created_by order by c desc;</code></pre>
<p>Tool used to populate the Postgres database was <a href="https://github.com/zhm/osmchanges-postgres">https://github.com/zhm/osmchanges-postgres</a> Give it a try, it's not terribly difficult to set up and run this query.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '14, 21:17</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Oct '14, 18:35</strong> </span></p>
</div>
</div>
<div id="comments-container-38060" class="comments-container">
<span id="38100"></span>
<div id="comment-38100" class="comment">
<div id="post-38100-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>see <a href="https://www.openstreetmap.org/user/SimonPoole/diary/23352">https://www.openstreetmap.org/user/SimonPoole/diary/23352</a> note that the editor GoMap!, at least in the version available up to a short time ago, created an empty changeset as method of checking if the authentication worked.</p>
</div>
<div id="comment-38100-info" class="comment-info">
<span class="comment-age">(30 Oct '14, 07:51)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="38107"></span>
<div id="comment-38107" class="comment">
<div id="post-38107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the case of "Go Map!" at credentials-checking changesets are identifiable as such:</p>
<p><a href="http://www.openstreetmap.org/changeset/16640349">http://www.openstreetmap.org/changeset/16640349</a></p>
<p>Though it can create others:</p>
<p><a href="http://www.openstreetmap.org/changeset/21804635">http://www.openstreetmap.org/changeset/21804635</a></p>
<p>I also see quite a lot of empty changesets from other editors:</p>
<p><a href="http://www.openstreetmap.org/changeset/26183795">http://www.openstreetmap.org/changeset/26183795</a></p>
<p><a href="http://www.openstreetmap.org/changeset/25568455">http://www.openstreetmap.org/changeset/25568455</a></p>
<p><a href="http://www.openstreetmap.org/changeset/24536371">http://www.openstreetmap.org/changeset/24536371</a></p>
<p>but not id?</p>
<p>My apologies to the authors of all of the changesets above - you're not being singled out for any other reason than you happened to use a particular OSM editor!</p>
</div>
<div id="comment-38107-info" class="comment-info">
<span class="comment-age">(30 Oct '14, 09:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="38110"></span>
<div id="comment-38110" class="comment">
<div id="post-38110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Found an iD one too:</p>
<p><a href="http://www.openstreetmap.org/changeset/26383946">http://www.openstreetmap.org/changeset/26383946</a></p>
</div>
<div id="comment-38110-info" class="comment-info">
<span class="comment-age">(30 Oct '14, 11:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="38111"></span>
<div id="comment-38111" class="comment">
<div id="post-38111-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>I pointed it out in my blog post, it is probably helpful to think of a changeset as setting a "start* marker ..... uploading something ... setting a "stop" marker. If something goes wrong in the upload bit, for example a conflict or a crash or ... the changeset will autoclose after an hour and, hey presto, you have an empty changeset.</p>
<p>Given that opening the changeset is a seperate API operation and there is no way to cancel or otherwise undo it once you have opened one, empty changesets are not completely avoidable.</p>
</div>
<div id="comment-38111-info" class="comment-info">
<span class="comment-age">(30 Oct '14, 12:28)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-38060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38060-form-container" class="comment-form-container">
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


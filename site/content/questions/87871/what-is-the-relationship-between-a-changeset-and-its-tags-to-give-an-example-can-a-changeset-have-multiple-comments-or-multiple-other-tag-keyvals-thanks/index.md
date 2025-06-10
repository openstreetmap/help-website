+++
type = "question"
title = "What is the relationship between a changeset and its tags? to give an example; can a ChangeSet have multiple Comments? or Multiple other tag Key/Vals? thanks"
description = '''Hello There I am importing the database into one of my test servers and wanted to know if TAGs per ChangeSets are one-to-one mapped, or one-to-may?  The reason I ask is because I am developing the ChangeSet table on SQL, and wondered is it best to have a TAG with a ForeignKey pointing to the origina...'''
date = "2023-09-25T20:58:00Z"
lastmod = "2023-09-29T21:28:00Z"
weight = 87871
keywords = [ "comment", "changeset", "tag" ]
aliases = [ "/questions/87871" ]
osqa_answers = 7
osqa_accepted = true
+++

<div class="headNormal">

# [What is the relationship between a changeset and its tags? to give an example; can a ChangeSet have multiple Comments? or Multiple other tag Key/Vals? thanks](/questions/87871/what-is-the-relationship-between-a-changeset-and-its-tags-to-give-an-example-can-a-changeset-have-multiple-comments-or-multiple-other-tag-keyvals-thanks)

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
<span id="post-87871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87871-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello There</p>
<p>I am importing the database into one of my test servers and wanted to know if TAGs per ChangeSets are one-to-one mapped, or one-to-may?</p>
<p>The reason I ask is because I am developing the ChangeSet table on SQL, and wondered is it best to have a TAG with a ForeignKey pointing to the original ChangeSet, or can I have all possible tags are fields in the same ChangeSet tables?</p>
<p>I don't have any tools to see any live examples or view the data, would appreciate if I'm pointed out in the right direction.</p>
<p>Thanks &amp; Regards Heider</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-comment" rel="tag" title="see questions tagged &#39;comment&#39;">comment</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Sep '23, 20:58</strong></p>
<img src="https://secure.gravatar.com/avatar/eeed840537e064846db56fe6d3ca9bd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Heider&#39;s gravatar image" />
<p><span>Heider</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Heider has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Sep '23, 12:39</strong> </span></p>
</div>
</div>
<div id="comments-container-87871" class="comments-container">
&#10;</div>
<div id="comment-tools-87871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87871-form-container" class="comment-form-container">
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

7 Answers:

</div>

</div>

<span id="87875"></span>

<div id="answer-container-87875" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87875-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Heider has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps it would help to look at something that processes changesets and changeset discussions <a href="https://github.com/SomeoneElseOSM/ChangesetMD/blob/replication_changes_01/queries.py">These queries</a> are the ones that the <a href="https://github.com/SomeoneElseOSM/ChangesetMD/tree/replication_changes_01">ChangesetMD</a> software uses to manage its database, which stores changesets, changeset tags, and in a separate table, changeset discussions.</p>
<p>(note the original author of this is <a href="https://github.com/ToeBee">ToeBee</a>. not me!)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '23, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-87875" class="comments-container">
&#10;</div>
<div id="comment-tools-87875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87875-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87873"></span>

<div id="answer-container-87873" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87873-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As with nodes, ways and relations, a changeset can have many tags. Each key is unique, so there can only be one tag with the key "comment", for example.</p>
<p>As for approaches for storing this in a SQL database, the two main ones are to have a ChangesetTag table, with foreign keys to a Changeset table, or alternatively use a dynamic storage column (e.g. json type) called tags on the Changeset table. Both approaches are used in different parts of the ecosystem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '23, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-87873" class="comments-container">
&#10;</div>
<div id="comment-tools-87873" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87873-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87874"></span>

<div id="answer-container-87874" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87874-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you Andy</p>
<p>I appreciate getting back to me, so, from what I understand I can safely create a "comment" column field into the ChangeSet table knowing there will be always one comment per ChangeSet. Is that right?</p>
<p>i.e. there would <em>not</em> be the following scenario:</p>
<pre><code>&lt;changeset id=&quot;123&quot; key1=val1 key2=val2 ... etc&gt;
  &lt;tag k=&quot;comment&quot; v=&quot;Comment-1&quot;/&gt;
  &lt;tag k=&quot;comment&quot; v=&quot;Comment-2&quot;/&gt;
  &lt;tag k=&quot;comment&quot; v=&quot;Comment-3&quot;/&gt;
&lt;/changeset&gt;</code></pre>
<p>I think the above example explains my query better, in this case, we would only expect one comment line (which is either Comment-1, or 2, or 3) but not all Tags of similar keys getting into the same ChangeSet.</p>
<p>Thanks again Andy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '23, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/eeed840537e064846db56fe6d3ca9bd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Heider&#39;s gravatar image" />
<p><span>Heider</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Heider has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Sep '23, 16:27</strong> </span></p>
</div>
</div>
<div id="comments-container-87874" class="comments-container">
&#10;</div>
<div id="comment-tools-87874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87874-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87876"></span>

<div id="answer-container-87876" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87876-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for the info SomeoneElse, I appreciate your help.</p>
<p>From the link you sent from ToeBee's work, there is another table for "comments' therefore, I have to assume that the Change-to-Comments is a one-to-many relationship and that comments can be multiple for the same change set.</p>
<p>Thank you very much for all your help, I will proceed with my development this way in this case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '23, 16:46</strong></p>
<img src="https://secure.gravatar.com/avatar/eeed840537e064846db56fe6d3ca9bd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Heider&#39;s gravatar image" />
<p><span>Heider</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Heider has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87876" class="comments-container">
&#10;</div>
<div id="comment-tools-87876" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87876-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87883"></span>

<div id="answer-container-87883" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87883-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can only have one tag with "comment" as a key, but you can have multiple tags on a changeset, with different keys, eg :</p>
<pre><code>&lt;changeset id=&quot;123&quot; key1=val1 key2=val2 ... etc&gt;
  &lt;tag k=&quot;comment&quot; v=&quot;Comment-1&quot;/&gt;
  &lt;tag k=&quot;comment2&quot; v=&quot;Comment-2&quot;/&gt;
  &lt;tag k=&quot;source&quot; v=&quot;some sources...&quot;/&gt;
&lt;/changeset&gt;</code></pre>
<p>If you care only about the comment tag, you can store its value in your ChangeSet table. Otherwise you need to have another table with key, value and reference to the changeset (or json store as Andy said).</p>
<p>What you saw (I guess), on the ChangesetMD page are other comments, displayed on the changeset <a href="https://www.openstreetmap.org/changeset/94116627">page</a> under the header "Discussion". These are not tags, and are stored differently.</p>
<p>The xml, from the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Changesets_2">documentation</a>, looks like this :</p>
<pre><code>&lt;osm&gt;
    &lt;changeset id=&quot;10&quot; created_at=&quot;2008-11-08T19:07:39+01:00&quot; open=&quot;true&quot; user=&quot;fred&quot; uid=&quot;123&quot; min_lon=&quot;7.0191821&quot; min_lat=&quot;49.2785426&quot; max_lon=&quot;7.0197485&quot; max_lat=&quot;49.2793101&quot; comments_count=&quot;3&quot; changes_count=&quot;10&quot;&gt;
        &lt;tag k=&quot;created_by&quot; v=&quot;JOSM 1.61&quot;/&gt;
        &lt;tag k=&quot;comment&quot; v=&quot;Just adding some streetnames&quot;/&gt;
        ...
        &lt;discussion&gt;
            &lt;comment date=&quot;2015-01-01T18:56:48Z&quot; uid=&quot;1841&quot; user=&quot;metaodi&quot;&gt;
                &lt;text&gt;Did you verify those street names?&lt;/text&gt;
            &lt;/comment&gt;
            &lt;comment date=&quot;2015-01-01T18:58:03Z&quot; uid=&quot;123&quot; user=&quot;fred&quot;&gt;
                &lt;text&gt;sure!&lt;/text&gt;
            &lt;/comment&gt;
            ...
        &lt;/discussion&gt;
    &lt;/changeset&gt;
&lt;/osm&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '23, 20:27</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-87883" class="comments-container">
&#10;</div>
<div id="comment-tools-87883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87883-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87884"></span>

<div id="answer-container-87884" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87884-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you very much H_mlet</p>
<p>I think your answer is the one I was looking for, and yes I totally understand that tags can have multiple different keys.</p>
<p>I appreciate your time and effort to help.</p>
<p>Kind Regards Heider</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '23, 21:28</strong></p>
<img src="https://secure.gravatar.com/avatar/eeed840537e064846db56fe6d3ca9bd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Heider&#39;s gravatar image" />
<p><span>Heider</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Heider has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87884" class="comments-container">
&#10;</div>
<div id="comment-tools-87884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87884-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87885"></span>

<div id="answer-container-87885" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87885-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you very much H_mlet</p>
<p>I think your answer is the one I was looking for, and yes I totally understand that tags can have multiple different keys.</p>
<p>I appreciate your time and effort to help.</p>
<p>Kind Regards Heider</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '23, 21:28</strong></p>
<img src="https://secure.gravatar.com/avatar/eeed840537e064846db56fe6d3ca9bd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Heider&#39;s gravatar image" />
<p><span>Heider</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Heider has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87885" class="comments-container">
&#10;</div>
<div id="comment-tools-87885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87885-form-container" class="comment-form-container">
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


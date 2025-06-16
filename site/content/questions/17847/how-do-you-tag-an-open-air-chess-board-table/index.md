+++
type = "question"
title = "How do you tag an open air chess board table?"
description = '''Quite common in public park: tables with a checkerboard / chess board painted on it to play chess or similar games. How do you tag these boards? Example: http://commons.wikimedia.org/wiki/File:ChessTable.png'''
date = "2012-11-21T09:30:00Z"
lastmod = "2012-11-22T14:33:00Z"
weight = 17847
keywords = [ "chess", "tagging" ]
aliases = [ "/questions/17847" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do you tag an open air chess board table?](/questions/17847/how-do-you-tag-an-open-air-chess-board-table)

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
<span id="post-17847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17847-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Quite common in public park: tables with a checkerboard / chess board painted on it to play chess or similar games. How do you tag these boards? Example: <a href="http://commons.wikimedia.org/wiki/File:ChessTable.png">http://commons.wikimedia.org/wiki/File:ChessTable.png</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-chess" rel="tag" title="see questions tagged &#39;chess&#39;">chess</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Nov '12, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/3f398da25e1453020723c955139a4ec7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ALE&#39;s gravatar image" />
<p><span>ALE</span><br />
<span class="score" title="1943 reputation points"><span>1.9k</span></span><span title="41 badges"><span class="badge1">●</span><span class="badgecount">41</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ALE has 4 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '12, 09:30</strong> </span></p>
</div>
</div>
<div id="comments-container-17847" class="comments-container">
&#10;</div>
<div id="comment-tools-17847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17847-form-container" class="comment-form-container">
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

<span id="17849"></span>

<div id="answer-container-17849" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17849-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-17849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Instead of providing a quick reply like "it does not exist", I will try to show you how finding tags works in OSM.</p>
<p>First, go to the <a href="https://wiki.openstreetmap.org/wiki/Main_Page">wiki documentation</a> and use the "search" field with "chess". This will show you a <a href="https://wiki.openstreetmap.org/w/index.php?title=Special%3ASearch&amp;search=chess">list of wiki pages containing the word 'chess'</a>. Usually, only the top 2 or 3 on the list are relevant. Here, the first result is the good one : <a href="https://wiki.openstreetmap.org/wiki/Tag:sport%3Dchess">Tag:sport=chess</a>.</p>
<p>We can see on this page that "the chess board drawn onto a table" is mentionned but is empty (at the time I write this answer). Ouch ! This is not usual in the wiki. It means that this kind of objet is not formally documented on the wiki. But it does not mean that somebody did not tag such thing into the OSM database. To verify this, use the link to '<a href="http://taginfo.openstreetmap.org/tags/?key=sport&amp;value=chess">taginfo</a>', a tool collecting all tags and statistics directly from the OSM database itself. From this link, you will find statistics about "sport=chess" but you can use the 'search' field to check if a key or key/value combination already exist in the database (and how many) about chess tables.</p>
<p>Searching '<a href="http://taginfo.openstreetmap.org/search?q=chess">chess</a>' gives me one element tagged 'chess=yes'. Then I find 46 '<a href="http://taginfo.openstreetmap.org/search?q=amenity%3Dtable">amenity=table</a>' and 12 '<a href="http://taginfo.openstreetmap.org/search?q=leisure%3Dtable">leisure=table</a>' but none for "amenity=chess_table" nor "leisure=chess_table". We can conclude that such specific object has never been tagged until now (or with an uncommon wording or foreign language). It is therefore up to you to decide if you create a new one like 'leisure=chess_table' or 'amenity=chess_table' or a combination like 'leisure=table' + 'chess=yes'. You might also contact the dedicated mailing list talking about OSM tagging : <a href="https://wiki.openstreetmap.org/wiki/MailingLists">tagging@openstreetmap.org</a> and raise the question there. If a consensus is found (or nobody complains about your choice), it would be even better to add your solution back into the wiki documentation if you want that other contributors reuse your tag later.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '12, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '12, 13:46</strong> </span></p>
</div>
</div>
<div id="comments-container-17849" class="comments-container">
<span id="17858"></span>
<div id="comment-17858" class="comment">
<div id="post-17858-score" class="comment-score">
6
</div>
<div class="comment-text">
<p>Given that sport=chess already exists and is the <a href="http://taginfo.openstreetmap.org/search?q=chess#values">most common taginfo result for 'chess'</a>, leisure=table + sport=chess would be a much more sensible combination than leisure=table + chess=yes.</p>
</div>
<div id="comment-17858-info" class="comment-info">
<span class="comment-age">(21 Nov '12, 12:47)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="17899"></span>
<div id="comment-17899" class="comment">
<div id="post-17899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For a "Life-Sized" chess board use leisure=pitch + sport=chess</p>
</div>
<div id="comment-17899-info" class="comment-info">
<span class="comment-age">(22 Nov '12, 14:33)</span> <span class="comment-user userinfo">srbrook</span>
</div>
</div>
</div>
<div id="comment-tools-17849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17849-form-container" class="comment-form-container">
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


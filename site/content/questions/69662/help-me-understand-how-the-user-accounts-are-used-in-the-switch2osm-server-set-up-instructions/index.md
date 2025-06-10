+++
type = "question"
title = "Help me understand how the user accounts are used in the switch2osm server set up instructions."
description = '''I&#x27;d like to set up a tile rendering server for my own use, for educational reasons, and for messing around with alternative renderings. I&#x27;ve followed the instructions at https://switch2osm.org/manually-building-a-tile-server-18-04-lts/, and despite not understanding everything made progress. One thi...'''
date = "2019-06-18T22:43:00Z"
lastmod = "2019-06-19T01:11:00Z"
weight = 69662
keywords = [ "rendering", "renderd", "switch2osm", "local-tile-server", "tileserver" ]
aliases = [ "/questions/69662" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Help me understand how the user accounts are used in the switch2osm server set up instructions.](/questions/69662/help-me-understand-how-the-user-accounts-are-used-in-the-switch2osm-server-set-up-instructions)

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
<span id="post-69662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69662-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to set up a tile rendering server for my own use, for educational reasons, and for messing around with alternative renderings.</p>
<p>I've followed the instructions at <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a>, and despite not understanding everything made progress.</p>
<p>One thing that I didn't understand from the instructions is the intended use of user accounts. It looks like there's the default system user, which is intended to be have sudo privileges, another unix account used for rendering purposes. The instructions seem to contradict themselves as to whether this secondary rendering account (<code>renderaccount</code> in the instructions) has sudo privileges or not. When it's added the instructions say "<code>createuser renderaccount</code> #answer yes for superuser (although this isn't strictly necessary)", but then later in the instructions it says "edit the '~/src/mod_tile/debian/renderd.init' file so that “RUNASUSER” is set to the non-root account that you have used before, such as 'renderaccount'". When I ran the <code>createuser renderaccount</code> I was not provided with any options, notably not the option to say yes to superuser.</p>
<p>I'm also confused why it instructed me to change to the postgres unix user (<code>sudo -u postgres -i</code>) prior to adding the <code>renderaccount</code> user.</p>
<p>I've not yet successfully installed the server, and suspect that it may be due to an issue with user permissions, but would like to understand this before moving forward.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-local-tile-server" rel="tag" title="see questions tagged &#39;local-tile-server&#39;">local-tile-server</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '19, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-69662" class="comments-container">
&#10;</div>
<div id="comment-tools-69662" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69662-form-container" class="comment-form-container">
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

<span id="69664"></span>

<div id="answer-container-69664" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69664-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You must understand there are two different sets of accounts: The Unix user accounts, and the PostgreSQL accounts. They are not necessarily aligned, however PostgreSQL's default setting is that if you have the Unix account X you will also use the PostgreSQL account X.</p>
<p>The Unix superuser is <code>root</code> and does not (by default) exist in PostgreSQL, and the PostgreSQL superuser is <code>postgres</code>, a non-privileged account in Unix.</p>
<p>The Unix user <code>renderaccount</code> does not need sudo privileges. In order to create this account in PostgreSQL, you need to have PostgreSQL superuser rights, which you gain by becoming the Unix user <code>postgres</code>; you cannot create this account as <code>root</code> because there is no matching PostgreSQL user.</p>
<p>Giving the <code>renderaccount</code> PostgreSQL superuser rights, while not strictly needed, makes things easier down the line.</p>
<p>Indeed in more recent PostgreSQL versions, <code>createuser</code> doesn't prompt you for superuser, and you must specify <code>--interactive</code> if you want the old behaviour, or just specify <code>-s</code> to make the account a superuser. If you have created the account already but without superuser, become the Unix user <code>postgres</code> and run</p>
<pre><code>psql -c &#39;alter role renderaccount with superuser&#39;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '19, 23:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69664" class="comments-container">
&#10;</div>
<div id="comment-tools-69664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69664-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69665"></span>

<div id="answer-container-69665" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69665-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The reason why the creation of a Unix account "renderaccount" is suggested is actually because of what we'd seen happen with previous versions of the instructions. There people either used "www-data" (often used as a default web server process) or "root" (definitely not recommended. Using "renderaccount" was designed to work independently of whatever might be there on a a server and not break anything. The assumption was that people might use these instructions on a machine that already exists, and by default if you set up a Ubuntu server you're asked for an initial user account. "renderaccount" was chosen because it's new and likely won't break anything that already exists.</p>
<p>As Frederik says there are two sets of accounts involved here - Unix accounts and PostgreSQL users. The guide tries to gloss over that and uses the same name for both (hence the "createuser renderaccount" to create a postgres user of that name).</p>
<p>If there's anything that you think needs to be clarified better please let us know - either by just saying what needs to be changed at the <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">wordpress</a> site or by a pull request to the <a href="https://github.com/switch2osm/switch2osm.github.io">github</a> one. The Wordpress site is actually the "live" one, but the text content of the main pages is the same, so you can actually comment on either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '19, 00:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-69665" class="comments-container">
<span id="69666"></span>
<div id="comment-69666" class="comment">
<div id="post-69666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi SomeoneElse, I didn't realize you were involved with Switch2osm too. You're a busy guy. Thank you for the reply here.</p>
<p>That makes sense. I did realize that there are Unix and Postgres accounts involved, but I found it unclear in the instructions when we're talking about one, and when we're talking about the other.</p>
</div>
<div id="comment-69666-info" class="comment-info">
<span class="comment-age">(19 Jun '19, 01:11)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-69665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69665-form-container" class="comment-form-container">
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


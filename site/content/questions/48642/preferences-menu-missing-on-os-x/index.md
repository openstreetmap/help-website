+++
type = "question"
title = "Preferences menu missing on OS X"
description = '''Hi, Working on a MAC (OSX 10.11.1 - EL Captain) with Wireshark 2.0.0. I&#x27;m trying to setup WLAN packet decryption. Strangely the Preferences menu-entry underneath the Edit menu is missing. Underneath the Configuration Profiles... menu-entry (where the Preferences menu-entry is suppose to be) I do hav...'''
date = "2015-12-19T15:02:00Z"
lastmod = "2015-12-19T20:36:00Z"
weight = 48642
keywords = [ "menu", "entry", "preferences", "missing" ]
aliases = [ "/questions/48642" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Preferences menu missing on OS X](/questions/48642/preferences-menu-missing-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48642-score" class="post-score" title="current number of votes">0</div><span id="post-48642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Working on a MAC (OSX 10.11.1 - EL Captain) with Wireshark 2.0.0. I'm trying to setup WLAN packet decryption. Strangely the <strong><em>Preferences</em></strong> menu-entry underneath the <strong><em>Edit</em></strong> menu is missing. Underneath the <strong><em>Configuration Profiles...</em></strong> menu-entry (where the <strong><em>Preferences</em></strong> menu-entry is suppose to be) I do have <strong><em>Start dictation</em></strong> and <strong><em>Emoji &amp; Symbols</em></strong>. Anyone has a clue why?</p><p>tx,</p><p>RC</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-menu" rel="tag" title="see questions tagged &#39;menu&#39;">menu</span> <span class="post-tag tag-link-entry" rel="tag" title="see questions tagged &#39;entry&#39;">entry</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '15, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/72e273677d7b7c4dc7386a5d3014d487?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spd&#39;s gravatar image" /><p><span>spd</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Dec '15, 20:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-48642" class="comments-container"></div><div id="comment-tools-48642" class="comment-tools"></div><div class="clear"></div><div id="comment-48642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48643"></span>

<div id="answer-container-48643" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48643-score" class="post-score" title="current number of votes">1</div><span id="post-48643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="spd has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The standard location for preferences on OS X is under the application menu. The toolkit we're using (Qt) follows this convention by placing them under under <em>Wireshark→Preferences</em> as well as making them accessible via the command-comma (⌘-,) keyboard shortcut. Qt places the <code>About Wireshark</code> menu item under the <code>Wireshark</code> menu as well.</p><p>The traditional location for preferences on other platforms has been <em>Edit→Preferences</em> and that was where they ended up on OS X in earlier versions of Wireshark. We'll probably keep using that location on other platforms, although the Windows design guidelines now seems to recommend <em>Tools→Options</em> and the GNOME HIG recommends <em>[Application menu]→Preferences</em>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '15, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-48643" class="comments-container"><span id="48644"></span><div id="comment-48644" class="comment"><div id="post-48644-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Qt places the About Wireshark menu item under the Wireshark menu as well.</p></blockquote><p>...which is where it's supposed to be in OS X applications.</p><p>(Presumably spd noted that the menu bar isn't where it used to be, either. :-))</p><blockquote><p>the Windows design guidelines now seems to recommend <em>Tools</em>→<em>Options</em> and the GNOME HIG recommends [<em>Application menu</em>]→<em>Preferences</em>.</p></blockquote><p>And the KDE HIG <a href="https://techbase.kde.org/Projects/Usability/HIG/Menu_Bar">says</a></p><blockquote><p>Use these standard menu categories if they apply to your application: File, Edit, View, Insert, Format, Tools, Settings, Window, Help.</p></blockquote><p>so I guess they'd go in some item under the Settings menu.</p></div><div id="comment-48644-info" class="comment-info"><span class="comment-age">(19 Dec '15, 20:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-48643" class="comment-tools"></div><div class="clear"></div><div id="comment-48643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Setting and getting a preference of an existing protocol from Lua"
description = '''Hi, Would anyone know if it&#x27;s possible to get or set a preference of an existing protocol from Lua ?  thanks'''
date = "2011-06-27T10:22:00Z"
lastmod = "2011-06-29T23:48:00Z"
weight = 4770
keywords = [ "lua", "preferences" ]
aliases = [ "/questions/4770" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Setting and getting a preference of an existing protocol from Lua](/questions/4770/setting-and-getting-a-preference-of-an-existing-protocol-from-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4770-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Would anyone know if it's possible to get or set a preference of an existing protocol from Lua ?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">lua preferences</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '11, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-4770" class="comments-container"><span id="4778"></span><div id="comment-4778" class="comment"><div id="post-4778-score" class="comment-score"></div><div class="comment-text"><p>By "existing protocol", do you mean a protocol that was not registered from Lua (e.g., "ip")?</p></div><div id="comment-4778-info" class="comment-info"><span class="comment-age">(27 Jun '11, 19:08)</span> helloworld</div></div><span id="4781"></span><div id="comment-4781" class="comment"><div id="post-4781-score" class="comment-score"></div><div class="comment-text"><p>Yes, For example wireshark preferences file contains following attribute ip.defragment: TRUE Is there a way I can get or set this preference ?</p><p>I'm aware of the ability to get/set preferences if I define my own protocol in lua but I'm looking for a way of doing the same thing for protocols like IP/TCP/UDP or any other not registered from Lua.</p></div><div id="comment-4781-info" class="comment-info"><span class="comment-age">(28 Jun '11, 02:16)</span> izopizo</div></div><span id="4794"></span><div id="comment-4794" class="comment"><div id="post-4794-score" class="comment-score"></div><div class="comment-text"><p>There's not even a documented, supported way of doing that from <em>C</em>, much less from Lua.</p><p>Why do you want to know the settings of some other protocol's preferences? By doing so, you're making an assumption about what its preferences <em>are</em>, and that can change over time.</p></div><div id="comment-4794-info" class="comment-info"><span class="comment-age">(28 Jun '11, 11:03)</span> Guy Harris ♦♦</div></div><span id="4800"></span><div id="comment-4800" class="comment"><div id="post-4800-score" class="comment-score"></div><div class="comment-text"><p>Looks simple from C. I know you need Lua, but since Guy mentioned it, I thought I'd list it in case someone cares:</p><ul><li><a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/prefs.c?revision=37696&amp;view=markup#l1359"><code>read_prefs()</code></a> or <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/prefs.c?revision=37696&amp;view=markup#l1481"><code>read_prefs_file()</code></a></li><li><a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/prefs.c?revision=37696&amp;view=markup#l1662"><code>prefs_set_pref()</code></a> or <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/prefs.c?revision=37696&amp;view=markup#l1982"><code>set_pref()</code></a></li></ul></div><div id="comment-4800-info" class="comment-info"><span class="comment-age">(28 Jun '11, 19:47)</span> helloworld</div></div><span id="4801"></span><div id="comment-4801" class="comment not_top_scorer"><div id="post-4801-score" class="comment-score"></div><div class="comment-text"><p>Since all prefs are read from and written to a file, it <em>is</em> possible from Lua to read/set a preference of a protocol that wasn't originally registered from Lua. It's kind of a pain though...</p></div><div id="comment-4801-info" class="comment-info"><span class="comment-age">(28 Jun '11, 19:50)</span> helloworld</div></div><span id="4802"></span><div id="comment-4802" class="comment not_top_scorer"><div id="post-4802-score" class="comment-score"></div><div class="comment-text"><p>But then there are command-line overrides (the <code>-o</code> flag) that aren't written to file, so Lua can't know about those...</p></div><div id="comment-4802-info" class="comment-info"><span class="comment-age">(28 Jun '11, 19:53)</span> helloworld</div></div><span id="4803"></span><div id="comment-4803" class="comment not_top_scorer"><div id="post-4803-score" class="comment-score"></div><div class="comment-text"><p>Exactly. Those routines were not intended to be used by dissectors; they're intended to be used by programs when starting up or, in the case of read_prefs_file(), by the code that maintains the "recents" file. They may or may not do what you want when used elsewhere, and they may or may not continue to exist with the current interface or even continue to exist at all.</p></div><div id="comment-4803-info" class="comment-info"><span class="comment-age">(28 Jun '11, 20:07)</span> Guy Harris ♦♦</div></div><span id="4814"></span><div id="comment-4814" class="comment"><div id="post-4814-score" class="comment-score">1</div><div class="comment-text"><p>Thanks for all your responses. What I was hoping to do was to change preferences on the fly. For example MTP3 protocol can come in different version ITU/ANSI I wanted to implement autodetection in LUA and change preferences on the fly accordingly</p><p>Thanks again</p></div><div id="comment-4814-info" class="comment-info"><span class="comment-age">(29 Jun '11, 09:52)</span> izopizo</div></div><span id="4815"></span><div id="comment-4815" class="comment not_top_scorer"><div id="post-4815-score" class="comment-score"></div><div class="comment-text"><p>"Autodetection" in what sense? Are you, in effect, trying to enhance the MTP3 dissector in a Lua add-on, so that, rather than requiring the user to determine whether the MTP3 traffic is ITU or ANSI, the Lua script will look at the traffic, attempt to determine whether it's ITU or ANSI, and then change the preference accordingly?</p></div><div id="comment-4815-info" class="comment-info"><span class="comment-age">(29 Jun '11, 09:56)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-4770" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-4770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4842"></span>

<div id="answer-container-4842" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4842-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The fast answer is <strong>no</strong>.</p><p>AFAIK, setting prefs of non-Lua protocols on-the-fly from Wireshark's Lua API is <em>not</em> possible. As a hack, Lua can "stage" a pref setting by writing to the <code>preferences</code> file, which Wireshark would read at startup or on profile change (<em>the Lua API alone can't trigger either of these events</em>). Still, nothing prevents the user from changing your setting in the meantime.</p><p>Lua can read a pref that was set from the GUI as soon as the user changes it because updates are written to <code>preferences</code> immediately. The problem here is determining which <code>preferences</code> to read, since each configuration profile can have its own, and Lua can't know which is active. And as mentioned in comments, Lua can't detect pref overrides from the command line's <code>-o</code> flag (which are not reflected in <code>preferences</code>).</p><p>Your best bet is to <a href="http://bugs.wireshark.org">submit</a> an enhancement request for the Lua API (and vote!).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 23:48</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-4842" class="comments-container"></div><div id="comment-tools-4842" class="comment-tools"></div><div class="clear"></div><div id="comment-4842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4780"></span>

<div id="answer-container-4780" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4780-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check this out: http://sharkfest.wireshark.org/sharkfest.09/DT06_Bjorlykke_Lua%20Scripting%20in%20Wireshark.pdf Page 33 is about Prefs..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '11, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/6fe350be1625b29d7944d6ab430e57ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hiftu&#39;s gravatar image" /><p>Hiftu<br />
<span class="score" title="44 reputation points">44</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hiftu has no accepted answers">0%</span></p></div></div><div id="comments-container-4780" class="comments-container"></div><div id="comment-tools-4780" class="comment-tools"></div><div class="clear"></div><div id="comment-4780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


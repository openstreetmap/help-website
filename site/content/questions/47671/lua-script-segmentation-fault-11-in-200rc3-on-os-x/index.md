+++
type = "question"
title = "Lua script - Segmentation fault 11 in 2.0.0rc3 on OS X"
description = '''On OS X, a very simple script was running in 1.12.3, just upgraded to 2.0.0rc3 and it fails after a few time: local wlan = Listener.new(&quot;wlan&quot;) local wlan_mgt_ssid_f = Field.new(&quot;wlan_mgt.ssid&quot;) function wlan.packet(pinfo,tvb,tapinfo)  if (wlan_mgt_ssid_f() ~= nil) then  print(tostring(wlan_mgt_ssid...'''
date = "2015-11-17T08:57:00Z"
lastmod = "2015-11-17T12:17:00Z"
weight = 47671
keywords = [ "lua", "crash", "tshark" ]
aliases = [ "/questions/47671" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Lua script - Segmentation fault 11 in 2.0.0rc3 on OS X](/questions/47671/lua-script-segmentation-fault-11-in-200rc3-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47671-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On OS X, a very simple script was running in 1.12.3, just upgraded to 2.0.0rc3 and it fails after a few time:</p><pre><code>local wlan = Listener.new(&quot;wlan&quot;)
local wlan_mgt_ssid_f = Field.new(&quot;wlan_mgt.ssid&quot;)
function wlan.packet(pinfo,tvb,tapinfo)
    if (wlan_mgt_ssid_f() ~= nil) then
        print(tostring(wlan_mgt_ssid_f()))
    end
end</code></pre><p>I run it in monitor mode with tshark:</p><pre><code>/Applications/Wireshark\ 2.0.0rc3.app/Contents/MacOS/tshark -I -q -i en0 -X lua_script:wlan_probe_req.lua</code></pre><p>I have a dozen of results before it crashes systematically with a segmentation fault 11</p><p>At one point, I had an error saying a variable was mutated:</p><pre><code>tshark(42188,0x7fff76185000) malloc: * error for object 0x7fe53ca9b348: incorrect checksum for freed object - object was probably modified after being freed.
    * set a breakpoint in malloc_error_break to debug</code></pre><p>Is my field mutated? How can I protect it? I've followed sample examples ...</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">lua crash tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '15, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p>TomLaBaude<br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div></div><div id="comments-container-47671" class="comments-container"></div><div id="comment-tools-47671" class="comment-tools"></div><div class="clear"></div><div id="comment-47671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47677"></span>

<div id="answer-container-47677" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47677-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Thomas,</p><p>This seems to be a regression and I just filled <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11722">bug 11722</a>.</p><p>Edit: and Stig just fixed it. It will be in official 2.0 release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '15, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Nov '15, 13:58</p></div></div><div id="comments-container-47677" class="comments-container"><span id="47691"></span><div id="comment-47691" class="comment"><div id="post-47691-score" class="comment-score">1</div><div class="comment-text"><p>This issue was related to the new "Reload Lua Plugins" UI functionality in 2.0. A fix to the bug report has been committed.</p><p>As a temporary workaround for RC3 you can try removing "local" in front of wlan to avoid the listener to go out of scope (being garbage collected).</p></div><div id="comment-47691-info" class="comment-info"><span class="comment-age">(17 Nov '15, 14:04)</span> stig ♦</div></div><span id="47697"></span><div id="comment-47697" class="comment"><div id="post-47697-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys for your reactivity! The temporary workaround work as well. Can I already download a release with the fix, or I wait for an official 2.0.0rc4?</p></div><div id="comment-47697-info" class="comment-info"><span class="comment-age">(18 Nov '15, 00:57)</span> TomLaBaude</div></div><span id="47700"></span><div id="comment-47700" class="comment"><div id="post-47700-score" class="comment-score">1</div><div class="comment-text"><p>There are automated builds available for OSX <a href="https://www.wireshark.org/download/automated/osx/">here</a> but it's a bit tricky to work out if they include the change.</p><p>Tricky as in I can't see how to relate the build revisions (which have a git hash) to the commit for the change (which also has a git hash).</p><p>Maybe just pick the most recent one that has a timestamp a few hours after the timestamp of the commit.</p></div><div id="comment-47700-info" class="comment-info"><span class="comment-age">(18 Nov '15, 02:26)</span> grahamb ♦</div></div><span id="47701"></span><div id="comment-47701" class="comment"><div id="post-47701-score" class="comment-score">1</div><div class="comment-text"><p>You can use <code>git describe $commit_hash</code> to find out the release where it ended up. For 2.0 and 2.1 respectively: v2.0.0rc3-75-g290601a and v2.1.0rc0-620-g1329743. The versions currently listed on the automated builds page are up-to-date with the LUA fix.</p></div><div id="comment-47701-info" class="comment-info"><span class="comment-age">(18 Nov '15, 02:55)</span> Lekensteyn</div></div><span id="47703"></span><div id="comment-47703" class="comment"><div id="post-47703-score" class="comment-score"></div><div class="comment-text"><p>@Lekensteyn</p><p>Doesn't that command require you to have installed git and cloned the repo in the first place? If so, that's not usable for non-devs.</p><p>We should have a simple method for non-devs to determine if a build includes a change. Maybe a web page that does that command on behalf of the user, extra credit for allowing a Gerrit change number as the reference to check for.</p></div><div id="comment-47703-info" class="comment-info"><span class="comment-age">(18 Nov '15, 04:08)</span> grahamb ♦</div></div><span id="47706"></span><div id="comment-47706" class="comment not_top_scorer"><div id="post-47706-score" class="comment-score"></div><div class="comment-text"><p>One can compare the CommitDate with the items listed at the gitweb interface: for <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=shortlog">master (Development)</a> and <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=shortlog;h=master-2.0">master-2.0</a>. Perhaps Gerrit can be taught to print this description too in the review messages ("cherry-picked as XXX" " (v2.0.0-nnn-gXXX)")</p></div><div id="comment-47706-info" class="comment-info"><span class="comment-age">(18 Nov '15, 04:41)</span> Lekensteyn</div></div></div><div id="comment-tools-47677" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-47677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47681"></span>

<div id="answer-container-47681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47681-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Could be a bug in the memory management of the Lua code.</p><p>Can you please try the following code? Does that cause a segfault as well?</p><pre><code>local wlan = Listener.new(&quot;wlan&quot;)
local wlan_mgt_ssid_f = Field.new(&quot;wlan_mgt.ssid&quot;)
function wlan.packet(pinfo,tvb,tapinfo)
    local wlan_mgt_ssid = wlan_mgt_ssid_f() 
    if (wlan_mgt_ssid ~= nil) then
        print(tostring(wlan_mgt_ssid_f))
    end
end</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '15, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47681" class="comments-container"><span id="47682"></span><div id="comment-47682" class="comment"><div id="post-47682-score" class="comment-score"></div><div class="comment-text"><p>I did not see the post of @Pascal Quantin as there was no connection in the train ;-)</p></div><div id="comment-47682-info" class="comment-info"><span class="comment-age">(17 Nov '15, 12:18)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-47681" class="comment-tools"></div><div class="clear"></div><div id="comment-47681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


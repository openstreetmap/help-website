+++
type = "question"
title = "How to fully uninstall wireshark from a Mac?"
description = '''Hello, loved the product. However, I&#x27;m done messing around and now cannot figure out how to fully uninstall from my mac? I&#x27;ve tried searching the documentation as well as this question area and cannot find any step by step guide on how to safely and easily uninstall? Any help would be much appreciat...'''
date = "2011-01-18T16:11:00Z"
lastmod = "2016-02-16T09:00:00Z"
weight = 1797
keywords = [ "macintosh", "uninstall" ]
aliases = [ "/questions/1797" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to fully uninstall wireshark from a Mac?](/questions/1797/how-to-fully-uninstall-wireshark-from-a-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1797-score" class="post-score" title="current number of votes">1</div><span id="post-1797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, loved the product. However, I'm done messing around and now cannot figure out how to fully uninstall from my mac? I've tried searching the documentation as well as this question area and cannot find any step by step guide on how to safely and easily uninstall?</p><p>Any help would be much appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macintosh" rel="tag" title="see questions tagged &#39;macintosh&#39;">macintosh</span> <span class="post-tag tag-link-uninstall" rel="tag" title="see questions tagged &#39;uninstall&#39;">uninstall</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '11, 16:11</strong></p><img src="https://secure.gravatar.com/avatar/89eecd11b7ca790bd5f1723e083b83d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pblocked&#39;s gravatar image" /><p><span>Pblocked</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pblocked has no accepted answers">0%</span></p></div></div><div id="comments-container-1797" class="comments-container"></div><div id="comment-tools-1797" class="comment-tools"></div><div class="clear"></div><div id="comment-1797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="5176"></span>

<div id="answer-container-5176" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5176-score" class="post-score" title="current number of votes">2</div><span id="post-5176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The installer .dmg contains a file called "Read me first.rtf" with the following info/instructions:</p><blockquote><p>What changes does the installer make?</p><p>The installer writes to the following locations:</p><p>• /Applications/Wireshark. The main Wireshark application. • /Library/StartupItems/ChmodBPF. A script which adjusts permissions on the system's packet capture devices (/dev/bpf*) when the system starts up. • /Library/Wireshark. A wrapper script and symbolic links which will let you run Wireshark and its associated utilities from the command line. You can access them directly or by adding /Library/Wireshark to your PATH.</p><p>Additionally a group named access_bpf is created. The user who opened the package is added to the group.</p><p>How do I uninstall?</p><ol><li>Remove /Applications/Wireshark</li><li>Remove /Library/Wireshark</li><li>Remove /Library/StartupItems/ChmodBPF</li><li>Remove the access_bpf group.</li></ol></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '11, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/bbc29923a51667df304615d3ee35491f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="charris&#39;s gravatar image" /><p><span>charris</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="charris has no accepted answers">0%</span></p></div></div><div id="comments-container-5176" class="comments-container"><span id="5189"></span><div id="comment-5189" class="comment"><div id="post-5189-score" class="comment-score"></div><div class="comment-text"><p>yes, but how do you uninstall the virtual ports it creates?</p></div><div id="comment-5189-info" class="comment-info"><span class="comment-age">(24 Jul '11, 07:33)</span> <span class="comment-user userinfo">bwanaaa</span></div></div><span id="5195"></span><div id="comment-5195" class="comment"><div id="post-5195-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "virtual ports"? What are examples of these virtual ports?</p></div><div id="comment-5195-info" class="comment-info"><span class="comment-age">(24 Jul '11, 15:37)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="5308"></span><div id="comment-5308" class="comment"><div id="post-5308-score" class="comment-score"></div><div class="comment-text"><p>vmnet1 and vmnet8 are still there when you issue ifconfig on a mac in terminal</p></div><div id="comment-5308-info" class="comment-info"><span class="comment-age">(27 Jul '11, 05:14)</span> <span class="comment-user userinfo">bwanaaa</span></div></div><span id="5323"></span><div id="comment-5323" class="comment"><div id="post-5323-score" class="comment-score">1</div><div class="comment-text"><p>That's because they're <em>NOT</em> created by Wireshark (really - they are <em>NOT</em> created by Wireshark), they're created by VMware Fusion; to get rid of them, you'll have to uninstall VMware Fusion.</p></div><div id="comment-5323-info" class="comment-info"><span class="comment-age">(27 Jul '11, 10:19)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="5329"></span><div id="comment-5329" class="comment"><div id="post-5329-score" class="comment-score"></div><div class="comment-text"><p>oops. sry. tnx.</p></div><div id="comment-5329-info" class="comment-info"><span class="comment-age">(27 Jul '11, 15:11)</span> <span class="comment-user userinfo">bwanaaa</span></div></div><span id="6560"></span><div id="comment-6560" class="comment not_top_scorer"><div id="post-6560-score" class="comment-score"></div><div class="comment-text"><p>Hi, but how do I remove the access_bpf group? or more correctly, where do I find the group?</p><p>Thx</p></div><div id="comment-6560-info" class="comment-info"><span class="comment-age">(26 Sep '11, 05:44)</span> <span class="comment-user userinfo">Ant</span></div></div></div><div id="comment-tools-5176" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-5176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1828"></span>

<div id="answer-container-1828" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1828-score" class="post-score" title="current number of votes">0</div><span id="post-1828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You just need to drag the application to the TrashCan. The only other two files I've found that lie outside of the application itself are pref folders. I'll assume that you did NOT manually install the command-line tools. If your local username is Pblocked then these would be: /Users/Pblocked/.wireshark/ /Users/Pblocked/.wireshark-etc</p><p>You can delete them by opening a terminal window and typing rm -rf ~/.wireshark*</p><p>Once you've deleted the application and those two directories you can scan your drive for any leftovers - but again, I haven't found any on mine and I've gone through several versions of WireShark on my system.</p><p>You can scan your drive with this command: sudo find / -iname "*ireshark*" -print | grep -v denied</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '11, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p><span>GeonJay</span><br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jan '11, 07:03</strong> </span></p></div></div><div id="comments-container-1828" class="comments-container"><span id="1965"></span><div id="comment-1965" class="comment"><div id="post-1965-score" class="comment-score"></div><div class="comment-text"><p>Note that "drag-uninstalling" any app won't get rid of preferences for the app; some might consider that a feature (as in "if I later decide I want the app again, I don't lose my preferences). That's not unique to Wireshark.</p><p><a href="http://appzapper.com/">AppZapper</a> supposedly cleans up other stuff for apps, including preferences, when you uninstall them; whether it knows about Wireshark, which follows UN*X dotfile/dotdirectory conventions rather than NeXTStEP/OS X .plist conventions for its preferences, is another matter.</p></div><div id="comment-1965-info" class="comment-info"><span class="comment-age">(26 Jan '11, 19:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="1979"></span><div id="comment-1979" class="comment"><div id="post-1979-score" class="comment-score"></div><div class="comment-text"><p>I searched far and wide for hidden prefs, application support files, etc. I'm thinking that because of WireShark's "ported" nature it doesn't behave in the same manner as usual Mac applications. I'd bet that I missed something though.</p></div><div id="comment-1979-info" class="comment-info"><span class="comment-age">(27 Jan '11, 12:07)</span> <span class="comment-user userinfo">GeonJay</span></div></div><span id="5177"></span><div id="comment-5177" class="comment"><div id="post-5177-score" class="comment-score"></div><div class="comment-text"><p>Yes - as I noted, Wireshark stores the personal configuration files in traditional UN*X style; that means that various personal configuration are stored in ~/.wireshark rather than ~/Library/Preferences etc.</p></div><div id="comment-5177-info" class="comment-info"><span class="comment-age">(22 Jul '11, 11:21)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-1828" class="comment-tools"></div><div class="clear"></div><div id="comment-1828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50241"></span>

<div id="answer-container-50241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50241-score" class="post-score" title="current number of votes">0</div><span id="post-50241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I had Wireshark 2 RC and a legacy GTK dev version. I wanted to delete everything and start from scratch with latest W2.</p><p>I uninstalled the following files</p><pre><code>/Applications/Wireshark.app
/Applications/Wireshark [dev build].app
/Library/Application Support/Wireshark
/Library/LaunchDaemons/org.wireshark.ChmodBPF.plist
/Library/LaunchDaemons/org.wireshark.XQuartzFixer.plist
/Library/Receipts/boms/org.wireshark.ChmodBPF.pkg.bom
/Library/Receipts/boms/org.wireshark.cli.pkg.bom
/Library/Receipts/boms/org.wireshark.Wireshark.pkg.bom
/private/var/db/BootCaches/*/app.org.wireshark.Wireshark.playlist
/private/var/db/receipts/org.wireshark.ChmodBPF.pkg.bom
/private/var/db/receipts/org.wireshark.ChmodBPF.pkg.plist
/private/var/db/receipts/org.wireshark.cli.pkg.bom
/private/var/db/receipts/org.wireshark.cli.pkg.plist
/private/var/db/receipts/org.wireshark.Wireshark.pkg.bom
/private/var/db/receipts/org.wireshark.Wireshark.pkg.plist
/private/var/db/receipts/org.wireshark.XQuartzFixer.pkg.bom
/private/var/db/receipts/org.wireshark.XQuartzFixer.pkg.plist
/private/var/folders/mr/*/T/wireshark_pcapng_*
~/.wireshark
~/.wireshark-etc
~/Library/Application Support/CrashReporter/wireshark-bin_*.plist
~/Library/Logs/DiagnosticReports/.wireshark-bin_*.crash.plist
~/Library/Logs/DiagnosticReports/wireshark-bin_*.crash
~/Library/Preferences/org.wireshark.Wireshark.plist
~/Library/Saved Application State/org.wireshark.Wireshark.savedState
/usr/local/bin/capinfos
/usr/local/bin/dftest
/usr/local/bin/dumpcap
/usr/local/bin/editcap
/usr/local/bin/mergecap
/usr/local/bin/randpkt
/usr/local/bin/rawshark
/usr/local/bin/text2pcap
/usr/local/bin/tshark
/usr/local/bin/wireshark</code></pre><p>Since I was reinstalling I didn't need to remove <code>access_bpf</code>, but in <a href="https://ask.wireshark.org/questions/10914/how-do-i-remove-access_bpf-group">this other topic</a> is explained how to.</p><pre><code>sudo dscl . -delete /Groups/access_bpf</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '16, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/24e4a6e495369e0c1ba6a2466a8a720b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wsk&#39;s gravatar image" /><p><span>wsk</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wsk has no accepted answers">0%</span></p></div></div><div id="comments-container-50241" class="comments-container"></div><div id="comment-tools-50241" class="comment-tools"></div><div class="clear"></div><div id="comment-50241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


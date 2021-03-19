+++
type = "question"
title = "Wireshark not installing on OSX Mavericks"
description = '''Last month I had Wireshark 1.10.8 working on my Macbook Pro with no problems. I foolishly (as it happens) decided to give the QT+ version a try so uninstalled, as per the instructions in the attached Readme file in the installation package, my existing version of Wireshark and installed the QT+ vers...'''
date = "2014-07-22T05:50:00Z"
lastmod = "2015-02-15T07:48:00Z"
weight = 34826
keywords = [ "osx", "installation", "install", "mavericks", "failure" ]
aliases = [ "/questions/34826" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not installing on OSX Mavericks](/questions/34826/wireshark-not-installing-on-osx-mavericks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34826-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Last month I had Wireshark 1.10.8 working on my Macbook Pro with no problems. I foolishly (as it happens) decided to give the QT+ version a try so uninstalled, as per the instructions in the attached Readme file in the installation package, my existing version of Wireshark and installed the QT+ version (1.99.0 I believe). It worked for a short period but constantly had to be restarted because it would lose half its open window above the top of my screen and then it lost access to the interfaces. I uninstalled it (again, as per the Readme in the installation package) and installed X11 and Wireshark 1.10.8. This installation did not work. The error I received can only be described as "vague" at best;</p><pre><code>Jul 22 08:17:08 Johns-MacBook.local installd[615]: PackageKit: Install Failed: Error Domain=PKInstallErrorDomain Code=112 &quot;An error occurred while running scripts from the package “Wireshark 1.10.8 Intel 64.pkg”.&quot; UserInfo=0x7ff893d17e80 {NSFilePath=./postinstall, NSURL=file://localhost/Volumes/Wireshark/Wireshark%201.10.8%20Intel%2064.pkg#chmodbpf.pkg, PKInstallPackageIdentifier=org.wireshark.ChmodBPF.pkg, NSLocalizedDescription=An error occurred while running scripts from the package “Wireshark 1.10.8 Intel 64.pkg”.} {
    NSFilePath = &quot;./postinstall&quot;;
    NSLocalizedDescription = &quot;An error occurred while running scripts from the package \U201cWireshark 1.10.8 Intel 64.pkg\U201d.&quot;;
    NSURL = &quot;file://localhost/Volumes/Wireshark/Wireshark%201.10.8%20Intel%2064.pkg#chmodbpf.pkg&quot;;
    PKInstallPackageIdentifier = &quot;org.wireshark.ChmodBPF.pkg&quot;;
}</code></pre><p>...but seems to imply that there's a problem with ChmodBPF. When I look in /Library/LaunchDaemons org.wireshark.ChmodBPF.plist is there and appears to have the correct permissions (system, wheel, me) however there are no helper scripts in /usr/local/bin. Needless to say although Wireshark starts correctly (or appears to do so) there are no interfaces in the interface list.</p><p>Does anyone have any ideas on how I can get this working? ...and no, multiple uninstalls, cleans and installs do not work.</p><p>John</p></div><div id="question-tags" class="tags-container tags">osx installation install mavericks failure</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '14, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/bd4ed9c86ace0b38c93b28524427ae01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jcheriton&#39;s gravatar image" /><p>jcheriton<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jcheriton has no accepted answers">0%</span></p></div></div><div id="comments-container-34826" class="comments-container"></div><div id="comment-tools-34826" class="comment-tools"></div><div class="clear"></div><div id="comment-34826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34857"></span>

<div id="answer-container-34857" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34857-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try running the following commands first:</p><pre><code>sudo rm -f \
    /usr/local/bin/capinfos \
    /usr/local/bin/dftest \
    /usr/local/bin/dumpcap \
    /usr/local/bin/editcap \
    /usr/local/bin/mergecap \
    /usr/local/bin/randpkt \
    /usr/local/bin/rawshark \
    /usr/local/bin/text2pcap \
    /usr/local/bin/tshark \
    /usr/local/bin/wireshark
sudo pkgutil --forget org.wireshark.cli.pkg
sudo rm -rf /Library/StartupItems/ChmodBPF
sudo rm -rf &quot;/Library/Application Support/Wireshark&quot;
sudo launchctl unload /Library/LaunchDaemons/org.wireshark.ChmodBPF.plist
sudo rm -f /Library/LaunchDaemons/org.wireshark.ChmodBPF.plist
sudo pkgutil --forget org.wireshark.ChmodBPF.pkg
sudo rm -rf /Applications/Wireshark.app
sudo pkgutil --forget org.wireshark.Wireshark.pkg</code></pre><p>That should remove all traces of both versions of Wireshark from the system <em>AND</em> make the OS X packaging system completely forget about it, so that, the next time you try installing Wireshark, the packaging system thinks you're doing a fresh installation.</p><p>Then try installing 1.10.8 again. (Note that 1.10.8 doesn't install ChmodBPF; instead, it removes ChmodBPF and installs a launchd launch daemon instead, to make the same permission change on the BPF devices that the ChmodBPF startup item did.)</p><p>If it <em>still</em> fails, report a bug at <a href="http://bugs.wireshark.org/">the Wireshark bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '14, 15:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34857" class="comments-container"><span id="34875"></span><div id="comment-34875" class="comment"><div id="post-34875-score" class="comment-score"></div><div class="comment-text"><p>Thanks for that Guy but it still refuses to install. It seems to be an issue with installing ChmodBPF in /Library/Application Support/Wireshark however even changing the permission on that directory and reinstalling make no difference.</p></div><div id="comment-34875-info" class="comment-info"><span class="comment-age">(24 Jul '14, 04:50)</span> jcheriton</div></div><span id="34902"></span><div id="comment-34902" class="comment"><div id="post-34902-score" class="comment-score"></div><div class="comment-text"><p>Then try running those commands again, start up the Wireshark installer and, before answering any questions, select "Installer Log" from the "Windows" menu, select "Show All Logs" rather than "Show Errors Only" in that window, and continue the install. Then, if the install fails, make a copy of the <em>entire</em> contents of that window - in case we need more information later - and look for any messages concerning the ChmodBPF package and paste them here. (I just tried removing it from a Mavericks virtual machine I have, rebooting to get the BPF devices back to "normal", and installing 1.10.8, and everything worked.)</p></div><div id="comment-34902-info" class="comment-info"><span class="comment-age">(24 Jul '14, 16:32)</span> Guy Harris ♦♦</div></div><span id="34967"></span><div id="comment-34967" class="comment"><div id="post-34967-score" class="comment-score"></div><div class="comment-text"><p>Ok, so after a good clean reboot and reinstall (or not, as it happens) I have, for ChmodBPF;</p><pre><code>    Jul 29 08:15:25 Johns-MacBook.local Installer[1171]:        Wireshark 1.10.8 Intel 64.pkg#chmodbpf.pkg : org.wireshark.ChmodBPF.pkg : 1.0
Jul 29 08:15:25 Johns-MacBook.local Installer[1171]: -[IFDInstallController(Private) _buildInstallPlan]: file://localhost/Volumes/Wireshark/Wireshark%201.10.8%20Intel%2064.pkg#chmodbpf.pkg
Jul 29 08:15:25 Johns-MacBook.local installd[1184]: PackageKit: packages=(
        &quot;PKLeopardPackage &lt;file://localhost/Volumes/Wireshark/Wireshark%201.10.8%20Intel%2064.pkg#wireshark.pkg&gt;&quot;,
        &quot;PKLeopardPackage &lt;file://localhost/Volumes/Wireshark/Wireshark%201.10.8%20Intel%2064.pkg#chmodbpf.pkg&gt;&quot;,
        &quot;PKLeopardPackage &lt;file://localhost/Volumes/Wireshark/Wireshark%201.10.8%20Intel%2064.pkg#utilitylauncher.pkg&gt;&quot;
    )
Jul 29 08:15:25 Johns-MacBook.local installd[1184]: PackageKit: Extracting file://localhost/Volumes/Wireshark/Wireshark%201.10.8%20Intel%2064.pkg#chmodbpf.pkg (destination=/var/folders/zz/zyxvpxvq6csfxvn_n0000000000000/C/PKInstallSandboxManager/84E912AD-3F3E-4EA4-9C1B-4931E586AD21.activeSandbox/Root/Library/Application Support/Wireshark, uid=0)
Jul 29 08:15:26 Johns-MacBook.local installd[1184]: PackageKit: Executing script &quot;./postinstall&quot; in /private/tmp/PKInstallSandbox.Gfd4Z1/Scripts/org.wireshark.ChmodBPF.pkg.DjNEh4
Jul 29 08:15:26 Johns-MacBook.local installd[1184]: PackageKit: Install Failed: Error Domain=PKInstallErrorDomain Code=112 &quot;An error occurred while running scripts from the package “Wireshark 1.10.8 Intel 64.pkg”.&quot; UserInfo=0x7fda52d60850 {NSFilePath=./postinstall, NSURL=file://localhost/Volumes/Wireshark/Wireshark%201.10.8%20Intel%2064.pkg#chmodbpf.pkg, PKInstallPackageIdentifier=org.wireshark.ChmodBPF.pkg, NSLocalizedDescription=An error occurred while running scripts from the package “Wireshark 1.10.8 Intel 64.pkg”.} {
        NSFilePath = &quot;./postinstall&quot;;
        NSLocalizedDescription = &quot;An error occurred while running scripts from the package \U201cWireshark 1.10.8 Intel 64.pkg\U201d.&quot;;
        NSURL = &quot;file://localhost/Volumes/Wireshark/Wireshark%201.10.8%20Intel%2064.pkg#chmodbpf.pkg&quot;;
        PKInstallPackageIdentifier = &quot;org.wireshark.ChmodBPF.pkg&quot;;
    }
Jul 29 08:15:26 Johns-MacBook.local Installer[1171]: install:didFailWithError:Error Domain=PKInstallErrorDomain Code=112 &quot;An error occurred while running scripts from the package “Wireshark 1.10.8 Intel 64.pkg”.&quot; UserInfo=0x7fce124f9880 {NSFilePath=./postinstall, NSURL=file://localhost/Volumes/Wireshark/Wireshark%201.10.8%20Intel%2064.pkg#chmodbpf.pkg, PKInstallPackageIdentifier=org.wireshark.ChmodBPF.pkg, NSLocalizedDescription=An error occurred while running scripts from the package “Wireshark 1.10.8 Intel 64.pkg”.}</code></pre><p>Again, thanks for the help with this. The full log can be found <a href="https://dl.dropboxusercontent.com/u/19705767/Wireshark%20Installer%20Log%2029-Jul-2014.txt">here</a></p></div><div id="comment-34967-info" class="comment-info"><span class="comment-age">(29 Jul '14, 05:26)</span> jcheriton</div></div><span id="34975"></span><div id="comment-34975" class="comment"><div id="post-34975-score" class="comment-score"></div><div class="comment-text"><p>OK, here's the contents of org.wireshark.chmodbpf.pkg's post-install script:</p><pre><code>#!/bin/sh

CHMOD_BPF=&quot;/Library/LaunchDaemons/org.wireshark.ChmodBPF.plist&quot;
BPF_GROUP=&quot;access_bpf&quot;
BPF_GROUP_NAME=&quot;BPF device access ACL&quot;

dscl . -read /Groups/&quot;$BPF_GROUP&quot; &gt; /dev/null 2&gt;&amp;1 || \
    dseditgroup -q -o create &quot;$BPF_GROUP&quot;
dseditgroup -q -o edit -a &quot;$USER&quot; -t user &quot;$BPF_GROUP&quot;

cp &quot;/Library/Application Support/Wireshark/ChmodBPF/org.wireshark.ChmodBPF.plist&quot; \
    &quot;$CHMOD_BPF&quot;
chmod 755 &quot;$CHMOD_BPF&quot;
chown root:wheel &quot;$CHMOD_BPF&quot;

rm -rf /Library/StartupItems/ChmodBPF

launchctl load &quot;$CHMOD_BPF&quot;</code></pre><p>Try copying that to a script file, giving it execute permission, running it with <code>sudo</code>, and see what it prints.</p></div><div id="comment-34975-info" class="comment-info"><span class="comment-age">(29 Jul '14, 10:56)</span> Guy Harris ♦♦</div></div><span id="35000"></span><div id="comment-35000" class="comment"><div id="post-35000-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Before failing to install Wireshark (and not surprisingly I guess) I get a lot of;</p><pre><code>chmod: /Library/LaunchDaemons/org.wireshark.ChmodBPF.plist: No such file or directory</code></pre><p>After failing to install Wireshark I simply get;</p><pre><code>nothing found to load</code></pre><p>This seems to imply that the Wireshark directory in /Library/Application Support is deficient in something. I have been here before - even changing the permissions for that directory and all it contains makes no difference.</p><p>Having said that, if I request information for the directory using Finder's Get Info menu the Permissions list shows "Fetching..." for the Read/Write owner.</p><p>Who should own this directory? root:wheel again?</p></div><div id="comment-35000-info" class="comment-info"><span class="comment-age">(30 Jul '14, 05:56)</span> jcheriton</div></div><span id="35001"></span><div id="comment-35001" class="comment not_top_scorer"><div id="post-35001-score" class="comment-score"></div><div class="comment-text"><p>@jcheriton</p><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-35001-info" class="comment-info"><span class="comment-age">(30 Jul '14, 06:23)</span> grahamb ♦</div></div><span id="35007"></span><div id="comment-35007" class="comment not_top_scorer"><div id="post-35007-score" class="comment-score"></div><div class="comment-text"><p>What do the commands</p><pre><code>ls -ld &quot;/Library/Application Support/Wireshark&quot;

ls -ld &quot;/Library/Application Support/Wireshark/ChmodBPF&quot;</code></pre><p>and</p><pre><code>ls -ld &quot;/Library/Application Support/Wireshark/ChmodBPF/org.wireshark.ChmodBPF.plist&quot;</code></pre><p>(complete with quotes) print?</p></div><div id="comment-35007-info" class="comment-info"><span class="comment-age">(30 Jul '14, 09:50)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-34857" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-34857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39868"></span>

<div id="answer-container-39868" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39868-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This problem is easily reproduced if the user uses the <code>-w</code> argument to "Unload the org.wireshark.ChmodBPF.plist launchd job."</p><pre><code># launchctl unload -w /Library/LaunchDaemons/org.wireshark.ChmodBPF.plist</code></pre><p>The <code>-w</code> argument overrides the Disabled key and sets it to true. On OS X 10.9.5, the state of the Disabled key is stored in /var/db/launchd.db/com.apple.launchd/overrides.plist.</p><p>Therefore, the user needs to remove the following lines from <code>/var/db/launchd.db/com.apple.launchd/overrides.plist</code> or else the installer will not complete successfully.</p><pre><code>&lt;key&gt;org.wireshark.ChmodBPF&lt;/key&gt;
&lt;dict&gt;
    &lt;key&gt;Disabled&lt;/key&gt;
    &lt;true/&gt;
&lt;/dict&gt;</code></pre><p>Once the override has been successfully removed, installation using "Wireshark 1.10.8 Intel 64", "Wireshark 1.12.3 Intel 64" and "Wireshark 1.99.1 Intel 64" should work (only tested on OS X 10.9.5).</p><p>This issue could also be mitigated from the installer by modifying chmodbpf's postinstall script to also use the <code>-w</code> argument when loading <code>$CHMOD_BPF</code>.</p><p>Another way to mitigate this issue would be by modifying the "Read me first.rtf" document supplied with Wireshark to directly state the command that was intended for use when unloading the org.wireshark.ChmodBPF.plist launchd job. The problem is that if a user were to search Google for, "Unload the org.wireshark.ChmodBPF.plist launchd" the <a href="https://ask.wireshark.org/questions/34826/wireshark-not-installing-on-osx-mavericks">first result is this help page</a> and the <a href="http://tim.vanwerkhoven.org/post/2011/11/17/OSX-launchd-and-launchctl-issues">second is a page that has the user use the <code>-w</code> option</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '15, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/8cf36cad28912051afc57f054a4621f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paretech&#39;s gravatar image" /><p>paretech<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paretech has no accepted answers">0%</span></p></div></div><div id="comments-container-39868" class="comments-container"></div><div id="comment-tools-39868" class="comment-tools"></div><div class="clear"></div><div id="comment-39868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


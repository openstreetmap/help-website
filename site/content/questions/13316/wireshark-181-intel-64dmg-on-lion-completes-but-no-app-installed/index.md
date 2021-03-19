+++
type = "question"
title = "Wireshark 1.8.1 Intel 64.dmg on Lion completes but no app installed"
description = '''OS X Lion: I have an older version of Wireshark 1.2.1 which I installed in ~/Applicaitons/ and it still launches correctly. Today I decided to upgrade to the latest Wireshark 1.8.1 and although the installer says it is successful, I noticed (a) it does not let me choose to install in my own ~/Applic...'''
date = "2012-08-02T07:50:00Z"
lastmod = "2012-08-02T07:50:00Z"
weight = 13316
keywords = [ "lion", "wireshark", "entitlement", "permissions" ]
aliases = [ "/questions/13316" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.8.1 Intel 64.dmg on Lion completes but no app installed](/questions/13316/wireshark-181-intel-64dmg-on-lion-completes-but-no-app-installed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13316-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OS X Lion: I have an older version of Wireshark 1.2.1 which I installed in ~/Applicaitons/ and it still launches correctly. Today I decided to upgrade to the latest Wireshark 1.8.1 and although the installer says it is successful, I noticed (a) it does not let me choose to install in my own ~/Applications folder and (b) there is no app installed to /Applications/Wireshark nor /Library/Wireshark. My account has admin rights. There seems to be some system.install.app-store-software entitlement or authorization problem. Any ideas?</p><p>Here is the console output:</p><pre><code>8/2/12 10:23:45.029 AM Installer: @(#)PROGRAM:Install  PROJECT:Install-690
8/2/12 10:23:45.029 AM Installer: @(#)PROGRAM:Installer  PROJECT:Installer-537
8/2/12 10:23:45.029 AM Installer: Hardware: MacBookPro3,1 @ 2.40 GHz (x 2), 6144 MB RAM
8/2/12 10:23:45.030 AM Installer: Running OS Build: Mac OS X 10.7.4 (11E53)
8/2/12 10:23:45.084 AM Installer: Wireshark 1.8.1 Intel 64  Installation Log
8/2/12 10:23:45.084 AM Installer: Opened from: /Volumes/Wireshark/Wireshark 1.8.1 Intel 64.pkg
8/2/12 10:23:51.216 AM Installer: InstallerStatusNotifications plugin loaded
8/2/12 10:23:57.812 AM Installer: ================================================================================
8/2/12 10:23:57.812 AM Installer: User picked Standard Install
8/2/12 10:23:57.812 AM Installer: Choices selected for installation:
8/2/12 10:23:57.812 AM Installer:   Install: &quot;Wireshark 1.8.1 Intel 64&quot;
8/2/12 10:23:57.812 AM Installer:   Install: &quot;Wireshark&quot;
8/2/12 10:23:57.812 AM Installer:   Install: &quot;Set capture permissions at startup&quot;
8/2/12 10:23:57.815 AM Installer:   Install: &quot;Command line utilities&quot;
8/2/12 10:23:57.815 AM Installer: ================================================================================
8/2/12 10:23:57.967 AM Installer: Configuring volume &quot;MacintoshSSD&quot;
8/2/12 10:23:57.969 AM Installer: Free space on &quot;MacintoshSSD&quot;: 111.29 GB (111287685120 bytes).
8/2/12 10:23:57.969 AM Installer: Create temporary directory &quot;/var/folders/vl/f_2h77yd65gdzs1v0s39nfrw0000gn/T//Install.19457DktKY3&quot;
8/2/12 10:23:57.976 AM Installer: IFPKInstallElement (3 packages)
8/2/12 10:23:58.036 AM authorizationhost: SFBuiltinEntitled: Installer.app is not entitled for system.install.apple-software
8/2/12 10:23:58.068 AM authorizationhost: SFBuiltinEntitled: Installer.app is not entitled for system.install.app-store-software
8/2/12 10:23:58.099 AM authorizationhost: SFBuiltinEntitled: Installer.app is not entitled for system.install.app-store-software
8/2/12 10:23:58.100 AM com.apple.SecurityServer: Failed to authorize right &#39;system.install.app-store-software&#39; by client &#39;/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/Resources/installd&#39; [19467] for authorization created by &#39;/System/Library/CoreServices/Installer.app&#39; [19457]
8/2/12 10:23:58.107 AM installd: PackageKit: ----- Begin install -----
8/2/12 10:23:59.613 AM SystemStarter: &quot;/Library/StartupItems&quot; failed sanity check: path was created after boot up
8/2/12 10:24:01.156 AM installd: Installed &quot;Wireshark 1.8.1 Intel 64&quot; ()
8/2/12 10:24:01.197 AM installd: PackageKit: ----- End install -----
8/2/12 10:24:02.116 AM Installer: Running install actions
8/2/12 10:24:02.117 AM Installer: Removing temporary directory &quot;/var/folders/vl/f_2h77yd65gdzs1v0s39nfrw0000gn/T//Install.19457DktKY3&quot;
8/2/12 10:24:02.126 AM Installer: Finalize disk &quot;MacintoshSSD&quot;
8/2/12 10:24:02.130 AM Installer: Notifying system of updated components
8/2/12 10:24:02.130 AM Installer: **** Summary Information ****
8/2/12 10:24:02.130 AM Installer:   Operation      Elapsed time
8/2/12 10:24:02.130 AM Installer: -----------------------------
8/2/12 10:24:02.130 AM Installer:        disk      0.01 seconds
8/2/12 10:24:02.130 AM Installer:      script      0.00 seconds
8/2/12 10:24:02.131 AM Installer:        zero      0.03 seconds
8/2/12 10:24:02.131 AM Installer:     install      4.14 seconds
8/2/12 10:24:02.131 AM Installer:     -total-      4.18 seconds
8/2/12 10:24:02.299 AM Installer: IFDInstallController 3950BB00 state = 5
8/2/12 10:24:02.300 AM Installer: Displaying &#39;Install Succeeded&#39; UI.</code></pre></div><div id="question-tags" class="tags-container tags">lion wireshark entitlement permissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '12, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/b29d817ac6609b67ccc9790ae58d89e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dferrero&#39;s gravatar image" /><p>dferrero<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dferrero has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Aug '12, 09:23</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-13316" class="comments-container"></div><div id="comment-tools-13316" class="comment-tools"></div><div class="clear"></div><div id="comment-13316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


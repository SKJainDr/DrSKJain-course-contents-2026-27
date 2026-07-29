# Appendix B: Frequently Asked Questions and Troubleshooting {: #appendix-b }

**परिशिष्ट ब: सामान्य प्रश्न एवं समस्या-समाधान**

## B.1 Installation and Startup Issues {: #sec-b-1 }

> •   Q: MS-Office asks for a Product Key / will not activate. What should I do? — A: Ensure you are signed in with the Microsoft account linked to a genuine licence, and that your internet connection is active during activation; contact your institution's IT support if using an institutional licence.
>
> •   Q: Word/Excel/PowerPoint opens very slowly. — A: Disable unnecessary Add-ins (File → Options → Add-ins → Manage: COM Add-ins → Go), and check that the computer meets minimum RAM requirements.
>
> •   Q: I cannot find an installed application. — A: Use the Windows search bar (Windows key, then type the app name) rather than searching only the Desktop.
>
> •   Q: An Office application opens but shows a blank/white screen. — A: Restart the computer; if it persists, run Office Repair via Control Panel → Programs → Microsoft Office → Change → Quick Repair (or Online Repair if that fails).
>
> •   Q: 'Safe Mode' appears in the title bar every time I open Word/Excel. — A: A faulty add-in is usually crashing the app on normal start-up; go to File → Options → Add-ins → Manage: COM Add-ins → Go, and untick recently added add-ins.
>
> •   Q: Office is installed but Outlook/Access is missing. — A: Not all Microsoft 365 plans include every application; check your plan's included apps, or install the missing app individually via Office.com → Install Apps.
>
> •   Q: The installation is stuck at a certain percentage for a long time. — A: Check your internet connection speed; a slow or interrupted connection is the most common cause. Pause and resume the installer, or restart it after ensuring a stable connection.
>
> •   Q: 'This app can't run on your PC' appears during installation. — A: You may be trying to install the 32-bit version on an incompatible setup, or vice versa; download the correct version matching your Windows edition (32-bit/64-bit) from your Microsoft 365 account.
>
> •   Q: How do I check which version of MS-Office is installed? — A: Open any Office app → File → Account (or Help) → it displays the product name and version/build number.
>
> •   Q: My trial version of Office has expired. — A: Purchase a genuine licence or use a free alternative (e.g., Office Online, Google Docs) until a licence is available; do not use unauthorised/cracked copies, as they pose security risks.
>
> •   Q: Office keeps asking me to sign in repeatedly. — A: Go to File → Account → Sign Out, then sign in again with the correct Microsoft account; also check the system date/time is correct, as an incorrect clock can break authentication.
>
> •   Q: Should I install the 32-bit or 64-bit version of Office? — A: 64-bit is recommended for most modern computers (better performance with very large files); use 32-bit only if you rely on an old add-in that does not support 64-bit.

## B.2 File Saving and Recovery {: #sec-b-2 }

> •   Q: The application crashed before I could save — is my work lost? — A: Reopen the application; a Document Recovery pane usually appears automatically offering the last AutoRecover version. Also check File → Info → Manage Document → Recover Unsaved Documents.
>
> •   Q: I saved my file but cannot find it. — A: Use File → Open → Recent to see recently used files, or search the file name (including its extension, e.g. .docx) in File Explorer's search box.
>
> •   Q: My .docx file will not open on an older computer. — A: Older Office versions (2003 and earlier) use .doc; use Save As to export a compatible copy, or ask the recipient to install the free 'Compatibility Pack' or update Office.
>
> •   Q: How often does AutoRecover save my work? — A: By default every 10 minutes; this interval can be shortened via File → Options → Save → 'Save AutoRecover information every \_\_ minutes' for extra safety.
>
> •   Q: I get 'Permission Denied' when trying to save a file. — A: The file may be open elsewhere (e.g., on another device or by another user), marked Read-Only, or saved in a protected system folder; use Save As to save a copy to your Documents folder instead.
>
> •   Q: My file shows 'Read-Only' in the title bar. — A: Go to File → Info → Protect Document and check if 'Always Open Read-Only' is enabled; alternatively another user may have the file open on a shared drive.
>
> •   Q: How do I recover an earlier version of a file I have overwritten? — A: File → Info → Version History (if the file is stored on OneDrive/SharePoint) lets you view and restore previous saved versions.
>
> •   Q: What is the difference between AutoSave and AutoRecover? — A: AutoSave (available only for files stored on OneDrive/SharePoint) continuously saves changes to the actual file in real time; AutoRecover periodically saves a separate temporary backup copy used only to recover unsaved work after a crash.
>
> •   Q: My USB drive file won't open and shows 'file is corrupt'. — A: Try Open → browse to the file → click the drop-down arrow next to the Open button → 'Open and Repair'; always safely eject USB drives to avoid corruption in the first place.
>
> •   Q: How can I make sure I never lose work again? — A: Save early and often (Ctrl+S), enable AutoSave/OneDrive syncing where possible, and keep a secondary backup (e.g., email a copy to yourself or use a USB drive) for important files.
>
> •   Q: I accidentally deleted a file — can I get it back? — A: Check the Recycle Bin first (right-click → Restore); if already emptied, check File History/Previous Versions in Windows, or OneDrive's Recycle Bin if the file was cloud-stored.
>
> •   Q: Why does Word warn me the file format is not supported when I try to open a file? — A: The file extension may not match its actual content (e.g., a renamed file), or the file is genuinely corrupted; try opening it with 'Open and Repair', or ask the sender to resend it.

## B.3 Common Word Issues {: #sec-b-3 }

> •   Q: My Table of Contents shows the wrong page numbers after editing. — A: Click inside the TOC and press F9, or right-click → Update Field → Update entire table.
>
> •   Q: Extra blank pages appear at the end of my document. — A: Usually caused by an extra paragraph mark or a manual page break; turn on Home → Show/Hide (¶) to reveal and delete the hidden marks.
>
> •   Q: My mail merge is only producing ONE letter instead of one-per-recipient. — A: Ensure Finish & Merge → Edit Individual Documents (not simply Print) is used to view all merged copies, and confirm the recipient list is not filtered to a single row.
>
> •   Q: My text has red or blue wavy underlines. — A: Red indicates a possible spelling error and blue/green a possible grammar issue; right-click the underlined word for suggestions, or ignore it if the word is correct (e.g., a proper noun).
>
> •   Q: Autocorrect keeps changing a word I type correctly. — A: Go to File → Options → Proofing → AutoCorrect Options and remove the specific auto-replacement rule, or click the small blue box that appears after the change and choose 'Undo AutoCorrect'.
>
> •   Q: My page numbers restart from 1 in the wrong section. — A: This is controlled per Section; go to Insert → Page Number → Format Page Numbers and choose 'Continue from previous section' instead of 'Start at 1'.
>
> •   Q: I cannot get the header/footer to be different on the first page. — A: Go to Header & Footer Tools → Design tab and tick 'Different First Page'.
>
> •   Q: My bulleted/numbered list has inconsistent indentation. — A: Select the list, right-click → Adjust List Indents, and set the same 'Text indent' and 'Bullet position' values for all items.
>
> •   Q: Track Changes marks are cluttering my document. — A: Go to Review tab → Display for Review, and switch from 'All Markup' to 'Simple Markup' or 'No Markup' for a cleaner view (the tracked changes remain saved).
>
> •   Q: My picture will not move where I drag it. — A: Select the picture, go to Picture Format → Wrap Text, and choose an option other than 'In Line with Text' (e.g., 'Square' or 'Tight') to allow free positioning.
>
> •   Q: Word keeps hyphenating words at the end of lines. — A: Go to Layout tab → Hyphenation → None to disable automatic hyphenation.
>
> •   Q: My document's margins printed differently from what I see on screen. — A: Check the printer's own margin/scaling settings are set to 'Actual Size' (not 'Fit to Page'), and confirm Page Setup margins in Word match the intended values.

## B.4 Common Excel Issues {: #sec-b-4 }

> •   Q: My formula shows \#DIV/0! — A: This means the formula is dividing by zero or by an empty cell; check that the denominator cell contains a valid non-zero number.
>
> •   Q: My formula shows \#REF! — A: A cell referenced by the formula has been deleted; re-enter the correct reference.
>
> •   Q: My formula shows \#NAME? — A: The function name is misspelt, or a required argument/quote mark is missing.
>
> •   Q: VLOOKUP returns \#N/A. — A: The lookup value does not exist in the first column of the table array, or there is a leading/trailing space mismatch; use TRIM() or check spelling.
>
> •   Q: My numbers appear as \##### in a cell. — A: The column is too narrow for the value; double-click the column border to AutoFit the width.
>
> •   Q: My formula shows \#VALUE! — A: One of the cells referenced in the formula contains text instead of a number where a number is expected; check every cell used in the calculation.
>
> •   Q: A cell shows a formula (e.g., =A1+B1) instead of the calculated result. — A: The cell is likely formatted as Text, or 'Show Formulas' is switched on (Formulas tab → Show Formulas); change the cell format to General/Number and re-enter the formula.
>
> •   Q: My dates are showing as serial numbers (e.g., 45123) instead of dates. — A: Select the cell(s) → Home → Number Format drop-down → choose 'Short Date' or 'Long Date'.
>
> •   Q: Sorting my data has mixed up rows so related information no longer matches. — A: Always select the entire data range (not just one column) before sorting, and ensure 'Expand the selection' is chosen when Excel prompts, so full rows move together.
>
> •   Q: My Pivot Table does not update after I add new data. — A: Right-click the Pivot Table → Refresh, or update the source range via PivotTable Analyze → Change Data Source if new rows fall outside the original range.
>
> •   Q: Conditional Formatting is not highlighting cells as expected. — A: Check Home → Conditional Formatting → Manage Rules to confirm the correct cell range is selected and the rule's condition is written correctly.
>
> •   Q: My chart is not updating when I change the underlying data. — A: Confirm the chart's data range still includes the changed cells (Chart Design → Select Data); if rows were added beyond the original range, extend the range or convert the data to an Excel Table first.
>
> •   Q: I cannot see gridlines on my worksheet. — A: Go to View tab and tick the Gridlines checkbox; this is a display setting only and does not affect printing (control that separately via Page Layout → Sheet Options → Gridlines → Print).
>
> •   Q: Excel is very slow with a large file. — A: Reduce the number of volatile functions (e.g., NOW, TODAY, RAND), remove unused formatting/blank rows-columns, and consider switching calculation to Manual (Formulas → Calculation Options) while editing.
>
> •   Q: My formula copied to other cells but always refers to the same first cell. — A: The reference is Absolute (\$A\$1) where it should be Relative (A1); remove the \$ signs or press F4 to cycle the reference type.
>
> •   Q: SUM is giving the wrong (usually zero) total. — A: The 'numbers' being summed may actually be stored as Text (left-aligned by default); convert them to numbers using Data → Text to Columns, or multiply by 1 in a helper column.
>
> •   Q: I accidentally deleted a row/column of formulas. — A: Press Ctrl+Z immediately to undo; if already saved and closed, check File → Info → Version History (OneDrive) for a recoverable earlier copy.
>
> •   Q: Freeze Panes is not keeping the correct row/column visible. — A: Click the cell just below and to the right of where you want the freeze to occur, then apply View → Freeze Panes → Freeze Panes again.

## B.5 Common PowerPoint Issues {: #sec-b-5 }

> •   Q: My embedded video will not play on another computer. — A: Ensure the video was inserted from 'This Device' (embedded) rather than linked from an external drive; keep the video file in the same folder if using a linked file, or use File → Info → 'Optimize Compatibility' before sharing.
>
> •   Q: Fonts look different when I open my presentation on another computer. — A: The custom font is likely not installed there; use File → Options → Save → 'Embed fonts in the file' before sharing, or stick to common system fonts.
>
> •   Q: My animations play in the wrong order. — A: Open the Animation Pane (Animations tab) and drag the numbered entries into the desired order.
>
> •   Q: My slide show will not advance when I click the mouse. — A: Check Transitions tab → Advance Slide settings; ensure 'On Mouse Click' is ticked (and 'After' is not overriding it unintentionally).
>
> •   Q: Pictures look blurry/pixelated after inserting. — A: The source image resolution is too low for its displayed size; use a higher-resolution image, or check File → Options → Advanced → Image Size and Quality is not set to compress too aggressively.
>
> •   Q: My presentation file size is very large. — A: Compress pictures via Picture Format → Compress Pictures, and avoid embedding very large/uncompressed video files; link to an external video instead if size is critical.
>
> •   Q: The slide show opens on the wrong monitor during a projector presentation. — A: Go to Slide Show tab → Monitor, and select the correct display; use Presenter View on your laptop and the actual slide show on the projector.
>
> •   Q: My SmartArt text is too small/overflowing its shape. — A: Click the SmartArt, go to Format → Text Fill/Effects, or simply shorten the text; SmartArt auto-shrinks text but very long text may still overflow — split it into fewer words per point.
>
> •   Q: I cannot find the Speaker Notes for a slide. — A: Go to View tab → Notes, or use Notes Page view, to see and edit the notes area below each slide.
>
> •   Q: My hyperlink to another slide does not work during the slide show. — A: Re-check the link via Insert → Link → Place in This Document, ensuring the correct slide/section is selected; links to deleted slides will break.
>
> •   Q: Text is spilling outside its placeholder box. — A: Use Format Shape → Text Options → 'Shrink text on overflow', or manually reduce the font size / shorten the content.
>
> •   Q: My presentation looks different when exported to PDF. — A: Some animations/transitions and embedded fonts do not carry over to PDF; check the PDF preview and, if needed, use File → Export → 'Create PDF/XPS' with 'Standard' quality for the best fidelity.

## B.6 Common Internet, Browser and Email Issues {: #sec-b-6 }

> •   Q: A website shows 'Not Secure' in the address bar. — A: The site is not using HTTPS; avoid entering passwords or payment details on it.
>
> •   Q: Pages load very slowly or not at all. — A: Check the Wi-Fi/data connection first; also try clearing the browser's cache and cookies (Settings → Privacy → Clear browsing data).
>
> •   Q: An email with an attachment is stuck 'Sending...' and never completes. — A: The attachment likely exceeds the provider's size limit (commonly 25 MB); compress the file or share it via a cloud-storage link instead.
>
> •   Q: A genuine email from a known sender has gone to Spam. — A: Open the Spam/Junk folder, select the email, and click 'Not Spam' (or 'Report not spam') so future emails from that sender are not filtered.
>
> •   Q: Forgot the password to an email account. — A: Use the 'Forgot password' link on the sign-in page; the account's recovery phone number/email (set during account creation, Section 4.10) is required to reset it.
>
> •   Q: My browser keeps showing pop-up ads. — A: Enable the browser's built-in pop-up blocker (Settings → Privacy and Security → Pop-ups and redirects → Blocked), and run a malware scan if pop-ups persist even on trusted sites.
>
> •   Q: A downloaded file is blocked with a warning message. — A: The browser suspects the file may be unsafe; only proceed ('Keep' or 'Keep anyway') if you fully trust the source, and always scan downloads with antivirus software before opening.
>
> •   Q: I sent an email to the wrong recipient — can I unsend it? — A: Some providers (e.g., Gmail) offer a short 'Undo Send' window (5-30 seconds, configurable in Settings) immediately after sending; beyond that, send a prompt follow-up email clarifying the mistake.
>
> •   Q: My inbox says 'Storage full' and I cannot receive new mail. — A: Delete large old emails/attachments (search 'has:attachment larger:10M' style filters), empty Trash/Spam, or upgrade the account's storage plan.
>
> •   Q: A web page will not display properly / looks broken. — A: Try refreshing (Ctrl+R), or open the page in a different browser; also check if the browser needs updating to its latest version.
>
> •   Q: I cannot open an attachment because 'there is no app to open this file'. — A: The file type (e.g., .accdb, .psd) may need specific software installed; alternatively, ask the sender to resend it in a common format such as PDF.
>
> •   Q: My video call keeps freezing/lagging. — A: Close other bandwidth-heavy applications and browser tabs, move closer to the Wi-Fi router, and consider turning off your own video temporarily to save bandwidth.
>
> •   Q: I am not sure if a link in an email is safe to click. — A: Hover the mouse over the link (without clicking) to preview the actual destination URL shown at the bottom of the browser/email client; if it looks suspicious or mismatched, do not click it.
>
> •   Q: My account shows a login attempt from an unfamiliar location. — A: Immediately change your password, review 'Recent Security Activity' in account settings, and enable Two-Factor Authentication if not already active.
>
> •   Q: How do I know if my Wi-Fi is actually the problem versus the website itself? — A: Try loading a different well-known website (e.g., google.com); if that also fails, the issue is your connection, not the original site.
>
> •   Q: My browser opens with an unfamiliar homepage or extra toolbar I didn't install. — A: This usually indicates unwanted software (adware) was installed alongside another program; check Settings → Extensions and remove unrecognised ones, then reset the browser's homepage/search engine.
>
> •   Q: I want to attach a very large video file to an email — what should I do? — A: Upload it to a cloud-storage service (e.g., Google Drive) and share the link in the email instead of attaching the file directly.
>
> •   Q: Two-Factor Authentication (2FA) codes are not arriving. — A: Check the registered phone number/authenticator app is correct and has network signal; most services also provide backup codes generated at 2FA setup — keep these saved safely.

## B.7 Common MS Access Issues {: #sec-b-7 }

> •   Q: Access refuses to save a table without a Primary Key. — A: This is a warning, not an error; either click Yes to let Access add an AutoNumber ID field automatically, or manually set a Primary Key (Section 5.5) before saving.
>
> •   Q: A relationship cannot be created between two tables. — A: Ensure the two linked fields (Primary Key and Foreign Key) use matching/compatible Data Types, e.g., both Number, not one Number and one Short Text.
>
> •   Q: A query returns zero records unexpectedly. — A: Double-check the Criteria row for typing errors, extra spaces, or incorrect capitalisation/quotation marks around text criteria.
>
> •   Q: A report shows \#Error instead of a total. — A: The expression in the text box (e.g., =Sum(\[Fees\])) likely references a field name that is spelt incorrectly or does not exist in the underlying table/query.
>
> •   Q: 'The database needs to be repaired or converted' message appears when opening. — A: Click Yes/OK to let Access run its built-in Compact and Repair utility, or run it manually via Database Tools → Compact and Repair Database.
>
> •   Q: My database file has become very large over time. — A: Regularly run Database Tools → Compact and Repair Database to reclaim wasted space left behind by deleted records/objects.
>
> •   Q: I cannot delete a record because of a 'related records' error. — A: Referential Integrity is preventing an orphaned record; delete or reassign the related records in the linked table first, or delete from the 'many' side before the 'one' side.
>
> •   Q: My Form shows blank/no data even though the table has records. — A: Check the Form's Record Source (Form Design → Property Sheet → Data tab) is correctly set to the intended table/query, and confirm no filter is silently applied.
>
> •   Q: Multiple users editing the same database at once causes 'File already in use' errors. — A: Access is primarily designed for small numbers of simultaneous users on a shared network drive; ensure the database is not set to 'Exclusive' open mode, or consider splitting the database (Database Tools → Access Database) into a back-end (data) and front-end (forms/reports) for smoother multi-user use.
>
> •   Q: A Yes/No field is displaying as -1 and 0 instead of a checkbox. — A: This occurs when the field is viewed/exported outside Access (e.g., in Excel); within Access Datasheet/Form view it correctly displays as a checkbox tick.
>
> •   Q: My AutoNumber field has skipped some numbers (gaps in sequence). — A: This is normal Access behaviour — numbers used by deleted or cancelled (Undo'd) records are not reused, so small gaps in the sequence do not indicate an error.
>
> •   Q: I cannot type into a field in Datasheet View. — A: The field may be set as a Calculated field, or the table/query may be Read-Only due to it not being a directly updatable query (e.g., it uses aggregate functions like SUM/COUNT with GROUP BY).
>
> •   Q: My Report's grouping is not sorting correctly. — A: In Report Design View, open the Group, Sort, and Total pane (Design tab) and confirm the correct field and sort order (A-Z / Z-A) are selected for each grouping level.
>
> •   Q: Access shows 'You entered an expression that has an invalid reference to the property FormatConditions'. — A: This typically happens with corrupted Conditional Formatting rules; delete and recreate the formatting rule via Home → Conditional Formatting on the affected control.
>
> •   Q: How do I prevent users from accidentally editing the design of my tables/forms? — A: Distribute the database as an .accde file (File → Save As → Make ACCDE), which locks the VBA code and prevents design changes while still allowing normal data entry and use.

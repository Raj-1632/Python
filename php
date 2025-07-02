<?php
$servername = "localhost";
$username = "root";
$password = "";
$db_name = "practice";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $db_name);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// DELETE operation
if (isset($_GET['delete'])) {
    $delete_id = $_GET['delete'];
    mysqli_query($conn, "DELETE FROM abc WHERE id=$delete_id");
    header("Location: ".$_SERVER['PHP_SELF']);
    exit();
}

// UPDATE operation - form prefill
$edit_id = "";
$edit_data = ['id' => '', 'name' => '', 'number' => '', 'city' => ''];
if (isset($_GET['edit'])) {
    $edit_id = $_GET['edit'];
    $edit_result = mysqli_query($conn, "SELECT * FROM abc WHERE id=$edit_id");
    $edit_data = mysqli_fetch_assoc($edit_result);
}

// INSERT or UPDATE logic
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $id = $_POST['id'];
    $name = $_POST['name'];
    $number = $_POST['number'];
    $city = $_POST['city'];

    if (isset($_POST['update'])) {
        // Update query
        $sql = "UPDATE abc SET name='$name', number='$number', city='$city' WHERE id='$id'";
    } else {
        // Insert query
        $sql = "INSERT INTO abc (id, name, number, city) VALUES ('$id', '$name', '$number', '$city')";
    }

    if (mysqli_query($conn, $sql)) {
        echo "<p style='color:green;'>Record saved successfully</p>";
    } else {
        echo "<p style='color:red;'>Error: " . $sql . "<br>" . mysqli_error($conn) . "</p>";
    }
}

// Fetch all data
$sql = "SELECT * FROM abc";
$result = mysqli_query($conn, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PHP CRUD Demo</title>
</head>
<body>
<center>
    <h2><?php echo isset($_GET['edit']) ? "Update" : "Insert"; ?> Data</h2>
    <form method="POST">
        <label>ID:</label>
        <input type="number" name="id" value="<?php echo $edit_data['id']; ?>" placeholder="ID" <?php if(isset($_GET['edit'])) echo "readonly"; ?> required><br><br>
        <label>Name:</label>
        <input type="text" name="name" value="<?php echo $edit_data['name']; ?>" placeholder="Name" required><br><br>
        <label>Number:</label>
        <input type="number" name="number" value="<?php echo $edit_data['number']; ?>" placeholder="Number" required><br><br>
        <label>City:</label>
        <input type="text" name="city" value="<?php echo $edit_data['city']; ?>" placeholder="City" required><br><br>

        <?php if (isset($_GET['edit'])): ?>
            <button type="submit" name="update">Update</button>
            <a href="<?php echo $_SERVER['PHP_SELF']; ?>">Cancel</a>
        <?php else: ?>
            <button type="submit" name="insert">Insert</button>
        <?php endif; ?>
    </form>

    <h2>View Data</h2>
    <table border="1" cellpadding="8">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Number</th>
            <th>City</th>
            <th>Action</th>
        </tr>
        <?php
        if (mysqli_num_rows($result) > 0):
            while($row = mysqli_fetch_assoc($result)):
        ?>
        <tr>
            <td><?php echo $row['id']; ?></td>
            <td><?php echo $row['name']; ?></td>
            <td><?php echo $row['number']; ?></td>
            <td><?php echo $row['city']; ?></td>
            <td>
                <a href="?edit=<?php echo $row['id']; ?>">Edit</a> |
                <a href="?delete=<?php echo $row['id']; ?>" onclick="return confirm('Are you sure?');">Delete</a>
            </td>
        </tr>
        <?php endwhile; else: ?>
            <tr><td colspan="5">No data found</td></tr>
        <?php endif; ?>
    </table>
</center>
</body>
</html>